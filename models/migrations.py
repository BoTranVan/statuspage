"""
Using to define a migration
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class migration(db.Model):
    """
    All data being storage on table "migrations"

    id        | integer                | not null
    migration | character varying(255) | not null

    batch     | integer                | not null
    """

    __tablename__ = "migrations"


    id = db.Column(db.Integer, primary_key=True)
    migration = db.Column(db.String(255), nullable=False)
    batch = db.Column(db.Integer, nullable=False)

    # def __init__(self, id, migration, batch):
    #     self.id = id
    #     self.migration = migration
    #     self.batch = batch
