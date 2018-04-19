"""
Using a define a user and reference ...
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class user(db.Model):
    """
    All data being storage on table "users"

    id                | integer                        | not null

    username          | character varying(255)         | not null

    password          | character varying(255)         | not null

    remember_token    | character varying(100)         |

    email             | character varying(255)         | not null

    api_key           | character varying(255)         | not null

    active            | boolean                        | not null default true

    level             | smallint                       | not null

    created_at        | timestamp(0) without time zone |

    updated_at        | timestamp(0) without time zone |

    google_2fa_secret | character varying(255)         |
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    remember_token = db.Column(db.String(100), index=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    api_key = db.Column(db.String(255), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True, index=True)
    level = db.Column(db.Integer, default=2)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    google_2fa_secret = db.Column(db.String(255))

    # def __init__(self, id, username, password, remember_token, email, api_key, active, level, created_at, updated_at, google_2fa_secret):
    #     self.id = id
    #     self.username = username
    #     self.password = password
    #     self.remember_token = remember_token
    #     self.email = email
    #     self.api_key = api_key
    #     self.active = active
    #     self.level = level
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.google_2fa_secret = google_2fa_secret
