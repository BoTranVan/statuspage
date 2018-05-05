"""
Using to define a tags
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class tag(db.Model):
    """
    All data being storage on table "tags"

    id         | integer                        | not null
    name       | character varying(255)         | not null

    slug       | character varying(255)         | not null

    created_at | timestamp(0) without time zone |

    updated_at | timestamp(0) without time zone |
    """

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    db.UniqueConstraint(name, slug)
    created_at = db.Column(db.String(26), default=now)

    # def __init__(self, id, name, slug, created_at, updated_at):
    #     self.id = id
    #     self.name = name
    #     self.slug = slug
    #     self.created_at = created_at
    #     self.updated_at = updated_at

    def get(self, id):
        """[summary]

        [description]

        Arguments:
            id {[type]} -- [description]

        Returns:
            [Information about incident(s)] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if id is None:
                return self.query.all()
            if id is not None and type(id) is int and id >= 0:
                return self.query.get(id)
        except Exception as e:
            return e.__cause__.args[1]

    def insert(self):
        """[summary]

        [description]

        Returns:
            [Information about incident(s)] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            db.session.add(self)
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]

    def delete(self):
        """[summary]

        [description]

        Returns:
            [Information about incident(s)] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            target = self.query.get(id)
            target.deleted_at = now
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]
