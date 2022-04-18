from marshmallow import Schema, fields, validates, ValidationError, validates_schema
from marshmallow.validate import Length


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    # title = fields.Str()
    title = fields.Str(validate=Length(min=1))  # Length - валидатор длинны
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()

    # вариант проверки через ValidationError (от marshmallow)
    @validates('year')
    def validate_year(self, value):
        if value < 1700:
            raise ValidationError('Year mast be greater than 1700')
        return value

    # вариант проверки через validates_schema (от marshmallow)
    @validates_schema(pass_many=True)
    def root_validate(self, data, **kwargs):
        if data['title'] == 'test':
            raise ValidationError('Title cannot be "test"', field_name='title')
        return data
