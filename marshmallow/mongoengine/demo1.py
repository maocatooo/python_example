
import mongoengine as me
me.connect(db='123123')


class Book(me.Document):
    title = me.StringField()
    author = me.ReferenceField('Author')


class Author(me.Document):
    id = me.IntField(primary_key=True, default=1)
    name = me.StringField()
    books = me.ListField(me.ReferenceField(Book))

    def __repr__(self):
        return '<Author(name={self.name!r})>'.format(self=self)



from marshmallow_mongoengine import ModelSchema


class AuthorSchema(ModelSchema):
    class Meta:
        model = Author


class BookSchema(ModelSchema):
    class Meta:
        model = Book

author_schema = AuthorSchema()


author = Author(name='Chuck Paluhniuk').save()
book = Book(title='Fight Club', author=author).save()

dump_data = author_schema.dump(author).data
# {'id': 1, 'name': 'Chuck Paluhniuk', 'books': ['5578726b7a58012298a5a7e2']}

author_schema.load(dump_data).data