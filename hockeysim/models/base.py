import typing
import datetime
from hockeysim.database import db
from sqlalchemy.sql import func

class BaseModel():
    def timestampColumn(updates=False) -> db.Column:
        if updates:
            return db.Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())
        return db.Column(db.DateTime, nullable=False, default=func.now())

    def _repr(self, **fields: typing.Dict[str, typing.Any]) -> str:
        '''
        Helper for __repr__
        '''
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                if (isinstance(field, datetime.datetime)):
                    field = field.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    field = field
                field_strings.append(f'{key}={field!r}')
            except db.orm.exc.DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"