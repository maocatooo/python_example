import os
import flask
from flask_mongoengine import MongoEngine
import whoosh.fields
from whoosh.fields import Schema
import whoosh.index
from whoosh.analysis import StemmingAnalyzer
from jieba.analyse import ChineseAnalyzer
from mongoengine import StringField
DEFAULT_WHOOSH_INDEX_NAME = 'whoosh_index'
from whoosh.qparser import OrGroup
from whoosh.qparser import AndGroup
from whoosh.qparser import MultifieldParser


def _get_analyzer(app, model):
    analyzer = getattr(model, 'whoosh_analyzer', None)

    if not analyzer and app.config.get('WHOOSH_ANALYZER'):
        analyzer = app.config.get('WHOOSH_ANALYZER')

    if not analyzer:
        analyzer = StemmingAnalyzer

    return analyzer()


def is_instance_or_subclass(val, class_):
    """Return True if ``val`` is either a subclass or instance of ``class_``."""
    try:
        return issubclass(val, class_)
    except TypeError:
        return isinstance(val, class_)


def _create_index(app, document):
    # a schema is created based on the fields of the model. Currently we only
    # support primary key -> whoosh.ID, and sqlalchemy.(String, Unicode, Text)
    # -> whoosh.TEXT.

    if not app.config.get('WHOOSH_BASE'):

        app.config['WHOOSH_BASE'] = DEFAULT_WHOOSH_INDEX_NAME

    # we index per model.
    wi = os.path.join(app.config.get('WHOOSH_BASE'),
            document.__name__)

    analyzer = _get_analyzer(app, document)
    schema, primary_key = _get_whoosh_schema_and_primary_key(document, analyzer)

    if whoosh.index.exists_in(wi):
        indx = whoosh.index.open_dir(wi)
    else:
        if not os.path.exists(wi):
            os.makedirs(wi)
        indx = whoosh.index.create_in(wi, schema)
    if 'whoosh_indexes' not in app.extensions:
        app.extensions['whoosh_indexes'] = {}
    app.extensions['whoosh_indexes'][document.__name__] = indx

    document._meta['pure_whoosh'] = _Searcher(primary_key, indx)
    # document.whoosh_primary_key = primary_key

    return indx


def whoosh_index(app, document):

    if app.extensions.get('whoosh_indexes'):
        app.extensions['whoosh_indexes'] = {}

    return app.whoosh_indexes.get(document.__name__,
                _create_index(app, document))


class _Searcher(object):
    ''' Assigned to a Model class as ``pure_search``, which enables
    text-querying to whoosh hit list. Also used by ``query.whoosh_search``'''

    def __init__(self, primary, indx):
        self.primary_key_name = primary
        self._index = indx
        self._index.reader()
        self.searcher = indx.searcher()
        self._all_fields = list(set(indx.schema._fields.keys()) -
                                {self.primary_key_name})

    def __call__(self, query, limit=None, fields=None, or_=False):
        self.ref_index()
        if fields is None:
            fields = self._all_fields
        print('fields', fields)

        group = OrGroup if or_ else AndGroup
        parser = MultifieldParser(fields, self._index.schema, group=group)

        return self._index.searcher().search(parser.parse(query),
                limit=limit)

    def ref_index(self):
        schema = self._index.schema
        wi = self._index.storage.folder
        if whoosh.index.exists_in(wi):
            self._index = whoosh.index.open_dir(wi)
        else:
            if not os.path.exists(wi):
                os.makedirs(wi)
            self._index = whoosh.index.create_in(wi, schema)


def _get_whoosh_schema_and_primary_key(document, analyzer):
    schema = {}
    primary = None
    abstract = document._meta.get('abstract')

    if not abstract:

        searchable = set(document._meta.get('searchable', set()))
        for field in document._fields.values():
            if field.primary_key:
                schema[field.name] = whoosh.fields.ID(stored=True, unique=True)
                primary = field.name
            if hasattr(field, 'whoosh_search') and hasattr(field, 'whoosh_search') and is_instance_or_subclass(field, (StringField,)):
                schema[field.name] = whoosh.fields.TEXT(analyzer=analyzer)
            if field.name in searchable and is_instance_or_subclass(field, (StringField,)):
                schema[field.name] = whoosh.fields.TEXT(analyzer=analyzer)
        if not primary:
            primary = document._meta.get('id_field')
            schema[primary] = whoosh.fields.ID(stored=True, unique=True)
    # print('schema', schema)
    return Schema(**schema), primary


def whoosh_search(self, query, limit=None, fields=None, or_=False):
    document = self._document
    queryset = self.clone()
    data = queryset.all()

    Searcher = document._meta['pure_whoosh']
    # print(Searcher.__dict__)
    pk = Searcher.primary_key_name
    indx = Searcher._index
    with indx.writer() as writer:
        for da in data:
            print(da)
            attrs = {pk: str(da.pk)}
            for field in Searcher._all_fields:
                attrs[field] = getattr(da, field, "")
            print(attrs)
            writer.update_document(**attrs)
    print(query)
    results = Searcher(query, limit, fields, or_)
    print(len(results))
    results_pks = (i[pk] for i in results)


def reg():
    # print(MM._db_field_map)
    # print(MM._meta)

    from mongoengine.base.common import _document_registry
    from mongoengine.signals import post_save
    from mongoengine.signals import post_delete
    # print(_document_registry, )
    for document in _document_registry.values():
        _create_index(app, document)

    from flask_mongoengine import BaseQuerySet
    setattr(BaseQuerySet, whoosh_search.__name__, whoosh_search)
    MM.objects.whoosh_search('我')


mongo = MongoEngine()


class MM(mongo.Document):
    meta = {"searchable": [
        'aaa'
    ]}
    aaa = StringField(whoosh_search=True)


app = flask.Flask(__name__)


@app.route('/')
def index():
    # MM.objects.a()
    print(MM._db_field_map)
    print(MM._meta)

    # for i in ['asdasda', '我']:
    #     MM(aaa=i).save()
    #
    print(MM.objects.whoosh_search('asdasda'))
    # print(MM.objects.update())
    return ''


if __name__ == '__main__':
    mongo.init_app(app, {"MONGODB_DB": 'test11112222'})
    reg()
    app.run(debug=True, port=5001)

