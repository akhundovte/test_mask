
from marshmallow import Schema, fields


class NewsSchema(Schema):
    link = fields.String(required=True)
    title = fields.String(required=True)
    content = fields.String(required=True)


news_schema = NewsSchema()
