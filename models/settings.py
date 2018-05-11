"""
Using to define settings and reference
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class Setting(db.Model):
    """
    All data being storage on table "settings"

    id         | integer                        | not null

    name       | character varying(255)         | not null

    value      | text                           | not null

    created_at | timestamp(0) without time zone |

    updated_at | timestamp(0) without time zone |
    """

    __tablename__ = "settings"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)

    # def __init__(self, id, name, value, created_at, updated_at):
    #     self.id = id
    #     self.name = name
    #     self.value = value
    #     self.created_at = created_at
    #     self.updated_at = updated_at
