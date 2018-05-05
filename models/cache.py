"""Using to create a session for users and references

[description]

Variables:
    now {[string]} -- [About now datetime]
"""

from config import db
import datetime as dt
now = dt.datetime.today().isoformat(' ')


class cache(db.Model):
    """Using to create a cache

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [table name in database]
        id {[int]} -- [The id of cache]
        key {[string(255)]} -- [The key value of cache]
        value {[text]} -- [The value of key in cache]
        expiration {[int]} -- [The expiration]
    """

    __tablename__ = "cache"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), nullable=False, unique=True)
    value = db.Column(db.Text, nullable=False)
    expiration = db.Column(db.Integer, nullable=False)

    # def __init__(self, id, key, value, expiration):
    #     self.id = id
    #     self.key = key
    #     self.value = value
    #     self.expiration = expiration

    def get(self, id=None):
        """[summary]

        [description]

        Keyword Arguments:
            id {[type]} -- [description] (default: {None})

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if id is None:
                return self.query.all()
            if id is not None and type(id) is int and id >= 0:
                return self.query.get(id)
        except Exception as e:
            return e.__cause__.args[1]

    def insert(self, key, value, expiration):
        """[summary]

        [description]

        Arguments:
            key {[type]} -- [description]
            value {[type]} -- [description]
            expiration {[type]} -- [description]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            db.session.add(self)
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]

    def delete(self, id):
        """[summary]

        [description]

        Arguments:
            id {[type]} -- [description]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            target = self.query.get(id)
            db.session.delete(target)
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]


class session(db.Model):
    """Using to create a session in database

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [table name in database]
        id {[int]} -- [The id of session]
        user_id {[int]} -- [The user_id have this session]
        ip_address {[sring(17)]} -- [The ip address of person have user_id]
        user_agent {[text]} -- [The user agent of person]
        payload {[text]} -- [The payload]
        last_activity {[string]} -- [The about last activity of person]
    """

    __tablename__ = "sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    ip_address = db.Column(db.String(17))
    user_agent = db.Column(db.Text)
    payload = db.Column(db.Text, nullable=False)
    last_activity = db.Column(db.String(26), nullable=False)

    # def __init__(self, id, user_id, ip_address,
    #               user_agent, payload, last_activity):
    #     self.id = id
    #     self.user_id = user_id
    #     self.ip_address = ip_address
    #     self.user_agent = user_agent
    #     self.payload = payload
    #     self.last_activity = last_activity

    def get(self, id):
        """[summary]

        [description]

        Arguments:
            id {[type]} -- [description]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            if id is None:
                return self.query.all()
            if id is not None and type(id) is int and id >= 0:
                return self.query.get(id)
        except Exception as e:
            return e.__cause__.args[1]

    def insert(self):
        """[summary]

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

    def delete(self, id):
        """[summary]

        [description]

        Arguments:
            id {[type]} -- [description]

        Returns:
            [None] -- [When successed]
            [Message] -- [When failed]
        """
        try:
            target = self.query.get(id)
            db.session.delete(target)
            return db.session.commit()
        except Exception as e:
            return e.__cause__.args[1]
