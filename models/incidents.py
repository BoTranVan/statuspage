#!/usr/bin/python
# -*- coding: utf-8 -*-
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

    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, db.ForeignKey('components.id'),
                    index=True)
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
            if type(self.id) is int and self.id >= 0:
                return self.query.get(self.id)
        except Exception, e:
            print ('ERROR: ', e)
            return {'error': {'message': 'Not found incident(s).'}}

    def get_json(self, limit=25, index=None, deleted=False, ):
        """Return a json response

        [description]
        """

        try:
            if bool(deleted) is True:
                if self.id is None:
                    (res, data) = ({}, [])
                    for i in self.query.all():
                        incident = i.get_fields()
                        data.append(incident)
                    res['total_count'] = len(data)
                    if limit is not None:
                        if index is not None:
                            res['data'] = data[int(index):int(limit)
                                + int(index)]
                        else:
                            res['data'] = data[:int(limit)]
                        res['record_count'] = len(res['data'])
                    if limit is None:
                        if index is not None:
                            res['data'] = data[int(index):]
                        else:
                            res['data'] = data
                        res['record_count'] = len(res['data'])
                    return res
                if type(self.id) is int and self.id >= 0:
                    res = self.get_fields()
                    return res
            else:
                if self.id is None:
                    (res, data) = ({}, [])
                    for i in self.query.all():
                        if i.deleted_at is None:
                            incident = i.get_fields()
                            data.append(incident)
                    res['total_count'] = len(data)
                    if limit is not None:
                        if index is not None:
                            res['data'] = data[int(index):int(limit)
                                + int(index)]
                        else:
                            res['data'] = data[:int(limit)]
                        res['record_count'] = len(res['data'])
                    if limit is None:
                        if index is not None:
                            res['data'] = data[int(index):]
                        else:
                            res['data'] = data
                        res['record_count'] = len(res['data'])
                    return res
                if self.id is not None:
                    if self.deleted_at is None:
                        res = self.get_fields()
                    else:
                        res = \
                            {'error': {'message': 'Not found incident(s).'}}

                    return res
        except Exception, e:
            print ('ERROR: ', e)
            return {'error': {'message': 'Not found incident(s).'}}

    def insert(self):
        """Create a new Incident.

        [description]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """

        try:
            db.session.add(self)
            db.session.commit()
            return {'data': {'Add successed ': str(self.id) + ' - '
                    + str(self.name)}}
        except Exception, e:
            print ('ERROR: ', e)
            return {'error': {'message': 'Not found incident(s).'}}

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
        except Exception, e:
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
                data = []
                for i in self.query.all():
                    if i.deleted_at is None:
                        i.deleted_at = now
                        data.append({'message': "incident '"
                            + str(i.name) + "' deleted at "
                            + str(i.deleted_at)})
                db.session.commit()
                return {'data': data}
            if type(self.id) is int and self.id >= 0:
                target = self.query.get(self.id)
                if target.deleted_at is None:
                    target.deleted_at = now
                    db.session.commit()
                    res = {'data': {'message': "incident '" \
                           + str(target.name) + "' deleted at " \
                           + str(target.deleted_at)}}
                else:

                    res = {'error': {'message': 'Not found incident.'}}

                return res
        except Exception, e:
            print ('ERROR: ', e)
            return {'error': {'message': 'Not found incident(s).'}}

    def get_fields(self):
        try:
            res = {
                'id': self.id,
                'name': self.get().name,
                'component_id': self.get().component_id,
                'status': self.get().status,
                'visible': self.get().visible,
                'message': self.get().message,
                'scheduled_at': self.get().scheduled_at,
                'created_at': self.get().created_at,
                'updated_at': self.get().updated_at,
                'deleted_at': self.get().deleted_at,
                }
            return res
        except Exception, e:
            print ('ERROR: ', e)
            return {'error': {'message': 'Not found incident(s).'}}


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

    __tablename__ = 'incident_templates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    template = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))
