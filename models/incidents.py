"""
Using define a incidents
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')

class incident(db.Model):
    """
    All data being storage on table "incidents"

    id           | integer                        | not null

    component_id | integer                        | not null default 0

    name         | character varying(255)         | not null

    status       | integer                        | not null

    message      | text                           | not null

    created_at   | timestamp(0) without time zone |

    updated_at   | timestamp(0) without time zone |

    deleted_at   | timestamp(0) without time zone |

    scheduled_at | timestamp(0) without time zone |

    visible      | boolean                        | not null default true
    """
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, default=0, index=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, index=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    update_at = db.Column(db.String(26), default=now)
    delete_at = db.Column(db.String(26), default="null")
    scheduled_at = db.Column(db.String(26), default="null")
    visible = db.Column(db.Boolean, default=True)

    def __init__(self, id, component_id, name, status, message, created_at, updated_at, deleted_at, scheduled_at, visible):
        self.id = id
        self.component_id = component_id
        self.name = name
        self.status = status
        self.message = message
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
        self.scheduled_at = scheduled_at
        self.visible = visible


class incident_template(db.Model):
    """
    All data being storage on tables "incident_templates"

    id         | integer                        | not null

    name       | character varying(255)         | not null

    slug       | character varying(255)         | not null

    template   | text                           | not null

    created_at | timestamp(0) without time zone |

    updated_at | timestamp(0) without time zone |

    deleted_at | timestamp(0) without time zone |
    """

    __tablename__ = "incident_templates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    template = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))

    def __init__(self, id, name, slug, template, created_at, updated_at, deleted_at):
        self.id = id
        self.name = name
        self.slug = slug
        self.template = template
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
