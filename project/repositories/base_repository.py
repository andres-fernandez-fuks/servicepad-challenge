from project.models.base_model import BaseModel
from project import db


class BaseRepository:
    __abstract__ = True
    object_class = BaseModel

    @classmethod
    def load_all(cls):
        return cls.object_class.query.all()

    @classmethod
    def load_by_id(cls, id):
        return cls.object_class.query.get(id)

    @classmethod
    def save(cls, obj):
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def delete(cls, obj):
        db.session.delete(obj)
        db.session.commit()
        return obj

    @classmethod
    def update(cls, obj_id: int, **kwargs):
        obj = cls.load_by_id(obj_id)
        obj.update(**kwargs)
        db.session.commit()
        return obj

    @classmethod
    def exists(cls, id):
        return cls.object_class.query.filter_by(id=id).first() is not None
