import datetime
from db import db


class BaseModel:
    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    # Soft delete
    def delete_from_db(self) -> None:
        self.deleted_at = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()