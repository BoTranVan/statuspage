"""
Using to define reference with metrics
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class Metric(db.Model):
    """[summary]

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [description]
        id {[type]} -- [description]
        name {[type]} -- [description]
        suffix {[type]} -- [description]
        description {[type]} -- [description]
        default_value {[type]} -- [description]
        calc_type {[type]} -- [description]
        display_chart {[type]} -- [description]
        created_at {[type]} -- [description]
        updated_at {[type]} -- [description]
        places {[type]} -- [description]
        default_view {[type]} -- [description]
        threshold {[type]} -- [description]
        order {[type]} -- [description]
    """

    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    suffix = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    default_value = db.Column(db.Integer, nullable=False)
    calc_type = db.Column(db.Integer, nullable=False)
    display_chart = db.Column(db.Boolean, default=True, index=True)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    places = db.Column(db.Integer, default=2)
    default_view = db.Column(db.Boolean, default=True)
    threshold = db.Column(db.Integer, default=5)
    order = db.Column(db.Integer, default=0)

    # def __init__(self, id, name, suffix, description, default_value, calc_type, display_chart, created_at, updated_at, places, default_view, threshold, order):
    #     self.id = id
    #     self.name = name
    #     self.suffix = suffix
    #     self.description = description
    #     self.default_value = default_value
    #     self.calc_type = calc_type
    #     self.display_chart = display_chart
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.places = places
    #     self.default_view = default_view
    #     self.threshold = threshold
    #     self.order = order


class MetricPoint(db.Model):
    """[summary]

    [description]

    Extends:
        db.Model

    Variables:
        __tablename__ {str} -- [description]
        id {[type]} -- [description]
        metric_id {[type]} -- [description]
        value {[type]} -- [description]
        created_at {[type]} -- [description]
        updated_at {[type]} -- [description]
        counter {[type]} -- [description]
    """

    __tablename__ = "metric_points"

    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(26), default=now)
    updated_at = db.Column(db.String(26), default=now)
    counter = db.Column(db.Integer, default=1)

    # def __init__(self, id, metric_id, value, created_at, updated_at, counter):
    #     self.id = id
    #     self.metric_id = metric_id
    #     self.value = value
    #     self.created_at = created_at
    #     self.updated_at = updated_at
    #     self.counter = counter
