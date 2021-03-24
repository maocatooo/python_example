from whoosh.analysis import StemmingAnalyzer, SimpleAnalyzer

import datetime
import flask
import flask_sqlalchemy
app = flask.Flask(__name__)
db = flask_sqlalchemy.SQLAlchemy()
# set the location for the whoosh index
app.config['WHOOSH_BASE'] = 'path/to/whoosh/base'
# set the global analyzer, defaults to StemmingAnalyzer.
app.config['WHOOSH_ANALYZER'] = StemmingAnalyzer()


class BlogPost(db.Model):
  __tablename__ = 'user'
  __searchable__ = ['name', 'email']  # these fields will be indexed by whoosh
  __analyzer__ = SimpleAnalyzer()        # configure analyzer; defaults to
                                         # StemmingAnalyzer if not specified

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)  # Indexed fields are either String,
  password = db.Column(db.String)   # Unicode, or Text
  email = db.Column(db.String)   # Unicode, or Text
  created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  status = db.Column(db.Integer)


@app.route('/')
def index():
    results = BlogPost.query.whoosh_search('user')
    print(results)
    return ''


if __name__ == '__main__':
    import flask_whooshalchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/blog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    app.run(debug=True, port=5002)
