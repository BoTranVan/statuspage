"""
Using a define component and reference it
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class component(db.Model):
    """
    All data being storage on table "components"

    id          | integer                        |

    name        | character varying(255)         |

    description | text                           |

    link        | text                           |

    status      | integer                        | default 0

    order       | integer                        | default 0

    group_id    | integer                        | default 0

    created_at  | timestamp(0) without time zone |

    updated_at  | timestamp(0) without time zone |

    deleted_at  | timestamp(0) without time zone |

    enabled     | boolean                        |
    """

    __tablename__ = "components"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    link = db.Column(db.Text)
    status = db.Column(db.Integer, default=0, index=True)
    order = db.Column(db.Integer, default=0, index=True)
    group_id = db.Column(db.Integer, default=0, index=True)
    enabled = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))

    # def __init__(self, name, description, link, status, order, group_id, enabled, created_at, updated_at, deleted_at):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.link = link
    #     self.status = status
    #     self.order = order
    #     self.group_id = group_id
    #     self.enabled = enabled
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.deleted_at = deleted_at

    def insert(self):
        db.session.add(self)
        return db.session.commit()



class component_group(db.Model):
    """
    All data being storage on table "component_groups"

    id         | integer                        |

    name       | character varying(255)         |

    created_at | timestamp(0) without time zone |

    updated_at | timestamp(0) without time zone |

    order      | integer                        | default 0

    collapsed  | integer                        | default 1
    """

    __tablename__ = "component_groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    order = db.Column(db.Integer, default=0, index=True)
    collapsed = db.Column(db.Integer, default=1)

    # def __init__(self, id, name, created_at, updated_at, order, collapsed):
    #     self.id = id
    #     self.name = name
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.order = order
    #     self.collapsed = collapsed


class component_tag(db.Model):
    """
    All data being storage on table "component_tag"

    id           | integer | not null

    component_id | integer | not null

    tag_id       | integer | not null
    """

    __tablename__ = "component_tag"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, nullable=False, index=True)
    tag_id = db.Column(db.Integer, nullable=False, index=True)

    # def __init__(self, id, component_id, tag_id):
    #     self.id = id
    #     self.component_id = component_id
    #     self.tag_id = tag_id
