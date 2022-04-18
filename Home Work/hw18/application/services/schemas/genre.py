from marshmallow import Schema, fields
from marshmallow.validate import Length


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    # name = fields.Str()
    name = fields.Str(validate=Length(min=1))  # Length - валидатор длинны


