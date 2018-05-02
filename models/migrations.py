"""
Using to define a migration
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class migration(db.Model):
    """Save all activity

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [description]
        id {[type]} -- [description]
        migration {[type]} -- [description]
        batch {[type]} -- [description]
    """

    __tablename__ = "migrations"

    id = db.Column(db.Integer, primary_key=True)
    migration = db.Column(db.String(255), nullable=False)
    batch = db.Column(db.Integer, nullable=False)

    # def __init__(self, id, migration, batch):
    #     self.id = id
    #     self.migration = migration
    #     self.batch = batch
