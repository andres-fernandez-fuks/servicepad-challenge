
from project import ma
from marshmallow_sqlalchemy import fields

DATE_FORMAT = "%d/%m/%y"
DATE_HOUR_FORMAT = "%d/%m/%y %H:%M:%S"

class BaseModelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "created_at", "updated_at")
        include_relationships = True
        load_instance = True

    created_at = fields.fields.DateTime(format=DATE_HOUR_FORMAT)
    updated_at = fields.fields.DateTime(format=DATE_HOUR_FORMAT)

class UserSchema(BaseModelSchema):
    class Meta:
        fields = BaseModelSchema.Meta.fields + (
            "fullname",
            "email",
            "photo",
        )
        include_relationships = True
        load_instance = True

class PublicationSchema(BaseModelSchema):
    class Meta:
        fields = BaseModelSchema.Meta.fields + (
            "title",
            "description",
            "priority",
            "status",
            "user",
        )
        include_relationships = True
        load_instance = True

    user = fields.Nested(UserSchema)