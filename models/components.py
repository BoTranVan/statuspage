"""Using to create a component and reference it

[description]

Variables:
    now {[string]} -- [About now datetime]
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class Component(db.Model):
    """Using a create a component

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [table name in database]
        id {[int]} -- [the id of a component]
        name {[string(255)]} -- [the name of a component]
        description {[text]} -- [Description of the component]
        link {[text]} -- [A hyperlink to the component]
        status {[int]} -- [Status of the component; 1-4]
        order {[int]} -- [Order of the component]
        group_id {[int]} -- [The group id that the component is within]
        enabled {[boolean]} -- [Whether the component is enabled]
        created_at {[string]} -- [description]
        updated_at {[string]} -- [description]
        deleted_at {[string]} -- [description]
    """

    __tablename__ = "components"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    link = db.Column(db.Text)
    status = db.Column(db.Integer, default=0, index=True)
    order = db.Column(db.Integer, default=0, index=True)
    group_id = db.Column(db.Integer, db.ForeignKey('component_groups.id'), index=True)
    enabled = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))

    # def __init__(self, name, description, link, status, order,
    #               group_id, enabled, created_at, updated_at, deleted_at):
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

    def get(self):
        """Using get all component or get a single component.

        [description]

        Keyword Arguments:
            id {[int]} -- [Component ID] (default: {None})

        Returns:
            [Information about component(s)] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if self.id is None:
                return self.query.all()
            if self.id is not None and type(self.id) is int and self.id >= 0:
                return self.query.get(self.id)
        except Exception as e:
            return e.__cause__.args[1]

    def insert(self):
        """Create a new component.

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
        """Update a component.

        [description]

        Arguments:
            id {[int]} -- [The id of component]
            **arguments {[dict]} -- [Maybe include: name, description,
            link, status, order, group_id, enabled]

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
        """Delete a component.

        Actually, data forever stored in database.
        Only difference is deleted_at have value

        Arguments:
            id {[int]} -- [The id of component]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            target = self.query.get(self.id)
            target.deleted_at = now
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]


class ComponentGroup(db.Model):
    """Using to create a component group

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [table name in database]
        id {[int]} -- [description]
        name {[type]} -- [Name of the component group]
        order {[type]} -- [Order of the component group]
        collapsed {[type]} -- [Collapse the group? 0 = No. 1 = Yes.
        2 = If a component is not Operational.]
        created_at {[type]} -- [description]
        updated_at {[type]} -- [description]
        deleted_at {[type]} -- [description]
    """
    __tablename__ = "component_groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    deleted_at = db.Column(db.String(26))
    order = db.Column(db.Integer, default=0, index=True)
    collapsed = db.Column(db.Integer, default=1)

    # def __init__(self, id, name, created_at, updated_at, order, collapsed):
    #     self.id = id
    #     self.name = name
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.order = order
    #     self.collapsed = collapsed

    def get(self):
        """Using get all component groups or get a single component group.

        [description]

        Keyword Arguments:
            id {[int]} -- [Component group ID] (default: {None})

        Returns:
            [Information about component(s)] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if self.id is None:
                return self.query.all()
            if self.id is not None and type(self.id) is int and self.id >= 0:
                return self.query.get(self.id)
        except Exception as e:
            return e.__cause__.args[1]

    def insert(self):
        """Create a new Component Group.

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
        """Update a Component Group.

        [description]

        Arguments:
            id {[int]} -- [The id of component group]
            **arguments {[dict]} -- [Maybe include: name, order, collapsed]

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
        """Delete a Component Group.

        Actually, data forever stored in database.
        Only difference is deleted_at have value

        Arguments:
            id {[int]} -- [The id of component]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            target = self.query.get(self.id)
            target.deleted_at = now
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]


class ComponentTag(db.Model):
    """Using to create a component tag

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [table name in database]
        id {[int]} -- [The id of component tag]
        component_id {[int]} -- [The id of component]
        tag_id {[int]} -- [The tag id]
    """

    __tablename__ = "component_tag"

    id = db.Column(db.Integer, primary_key=True)
    component_id = db.Column(db.Integer, db.ForeignKey('components.id'), nullable=False, index=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False, index=True)

    # def __init__(self, id, component_id, tag_id):
    #     self.id = id
    #     self.component_id = component_id
    #     self.tag_id = tag_id

    def get(self):
        """Using get all component tags or get a single component tag.

        [description]

        Keyword Arguments:
            id {[int]} -- [Component group ID] (default: {None})

        Returns:
            [Information about component(s)] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if self.id is None:
                return self.query.all()
            if self.id is not None and type(self.id) is int and self.id >= 0:
                return self.query.get(self.id)
        except Exception as e:
            return e.__cause__.args[1]

    def insert(self):
        """Create new component tag

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

    def delete(self):
        """Delete component tag

        Actually, data forever stored in database.
        Only difference is deleted_at have value

        Arguments:
            id {[int]} -- [The id of component]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            target = self.query.get(self.id)
            db.session.delete(target)
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]
