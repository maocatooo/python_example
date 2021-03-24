from datetime import date, datetime
from pprint import pprint

from marshmallow import Schema, fields
from json import JSONEncoder
import json


class ArtistSchema(Schema):
    name = fields.Str()


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

    class Meta:

        fields = (
            "release_date1",
        )

class CJsonEncoder(JSONEncoder):

    def default(self, obj):

        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, str):
            return str("123")
        else:
            return JSONEncoder.default(self, obj)
class A():
    pass

bowie = dict(name="David Bowie")
album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17), release_date1=datetime.now())


class User():
    def __init__(self):
        self.release_date1 = A()

schema = AlbumSchema()
result = schema.dump(User())
pprint(result.data, indent=2)