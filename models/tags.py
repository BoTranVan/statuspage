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
    updated_at = db.Column(db.String(26), default=now)

    # def __init__(self, id, name, slug, created_at, updated_at):
    #     self.id = id
    #     self.name = name
    #     self.slug = slug
    #     self.created_at = created_at
    #     self.updated_at = updated_at
