"""Using to create a incident and reference it

[description]

Variables:
    now {[string]} -- [About now datetime]
"""
from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class Incident(db.Model):
    """Using to create a incident

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [table name in database]
        id {[int]} -- [The id]
        component_id {[int]} -- [The id of component that this incident was in
        cluded]
        name {[type]} -- [description]
        status {[type]} -- [description]
        message {[type]} -- [description]
        created_at {[type]} -- [description]
        updated_at {[type]} -- [description]
        deleted_at {[type]} -- [description]
        scheduled_at {[type]} -- [description]
        visible {[type]} -- [description]
    """
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, db.ForeignKey('components.id'), index=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, index=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))
    scheduled_at = db.Column(db.String(26))
    visible = db.Column(db.Boolean, default=True)

    # def __init__(self, id, component_id, name, status, message, created_at,
    #               updated_at, deleted_at, scheduled_at, visible):
    #     self.id = id
    #     self.component_id = component_id
    #     self.name = name
    #     self.status = status
    #     self.message = message
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.deleted_at = deleted_at
    #     self.scheduled_at = scheduled_at
    #     self.visible = visible

    def get(self):
        """Using get all incidents or get a single incident.

        [description]

        Keyword Arguments:
            id {[int]} -- [Incident ID] (default: {None})

        Returns:
            [Information about incident(s)] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if self.id is None:
                return self.query.all()
            if self.id is not None and type(self.id) is int and self.id >= 0:
                return self.query.get(self.id)
        except Exception as e:
            return e.__cause__.args[1]

    def get_json(self, lim=None, index=None):
        """Return a json response

        [description]
        """
        try:
            if self.id is None:
                res, data = {}, []
                for i in self.query.all():
                    incident = {
                            "id": i.id,
                            "component_id": i.component_id,
                            "name": i.name,
                            "status": i.status,
                            "visible": i.visible,
                            "message": i.message,
                            "scheduled_at": i.scheduled_at,
                            "created_at": i.created_at,
                            "updated_at": i.updated_at,
                            "deleted_at": i.deleted_at
                        }
                    data.append(incident)
                res['total_count'] = len(data)
                if lim is not None:
                    if index is not None:
                        res['data'] = data[int(index): int(lim) + int(index)]
                    else:
                        res['data'] = data[:int(lim)]
                    res['record_count'] = len(res['data'])
                if lim is None:
                    if index is not None:
                        res['data'] = data[int(index):]
                    else:
                        res['data'] = data
                    res['record_count'] = len(res['data'])
                return res
            if self.id is not None and type(self.id) is int and self.id >= 0:
                res = {
                    "data": {
                        "id": self.get().id,
                        "component_id": self.get().component_id,
                        "name": self.get().name,
                        "status": self.get().status,
                        "visible": self.get().visible,
                        "message": self.get().message,
                        "scheduled_at": self.get().scheduled_at,
                        "created_at": self.get().created_at,
                        "updated_at": self.get().updated_at,
                        "deleted_at": self.get().deleted_at
                    }
                }
                return res
        except Exception as e:
            print("ERROR: ", e)
            res = {
                    "error": {
                        "message": "Not found object"
                    }
                }
            return res

    def insert(self):
        """Create a new Incident.

        [description]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            db.session.add(self)
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]

    def update(self, **arguments):
        """Update a Incident

        [description]

        Arguments:
            id {[int]} -- [The id of component]
            **arguments {[dict]} -- [Maybe include: name, message,
            status, visible, component_id, component_status, notify]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]

        """
        try:
            target = self.query.get(self.id)
            for i in arguments:
                target.__setattr__(i, arguments[i])
            target.updated_at = now
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]

    def delete(self):
        """Delete a incident.

        Actually, data forever stored in database.
        Only difference is deleted_at have value

        Arguments:
            id {[int]} -- [The id of component]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if self.id is None:
                for i in self.query.all():
                    i.delete_at = now
                return db.session.commit()
            if self.id is not None and type(self.id) is int and self.id >= 0:
                target = self.query.get(self.id)
                target.deleted_at = now
                return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]


class IncidentTemplate(db.Model):
    """Using to create a incident template

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [table name in database]
        id {[int]} -- [The id]
        name {[str(255)]} -- [The name of incident template]
        slug {[str(255)]} -- [Content of tag in incidents]
        template {[text]} -- [description]
        created_at {[string]} -- [description]
        updated_at {[string]} -- [description]
        deleted_at {[string]} -- [description]
    """

    __tablename__ = "incident_templates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    template = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))

    # def __init__(self, id, name, slug, template, created_at, updated_at, deleted_at):
    #     self.id = id
    #     self.name = name
    #     self.slug = slug
    #     self.template = template
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.deleted_at = deleted_at
