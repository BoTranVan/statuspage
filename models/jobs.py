"""
Using to defined jobs
"""

from config import db
from datetime import datetime as dt
now = dt.today().isoformat(' ')


class Job(db.Model):
    """
    All data being storage on table "jobs"

    id           | bigint                 | not null

    queue        | character varying(255) | not null

    payload      | text                   | not null

    attempts     | smallint               | not null

    reserved     | smallint               | not null

    reserved_at  | integer                |

    available_at | integer                | not null

    created_at   | integer                | not null
    """

    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    queue = db.Column(db.String(255), nullable=False)
    payload = db.Column(db.Text, nullable=False)
    attempts = db.Column(db.Integer, nullable=False)
    reserved = db.Column(db.Integer, nullable=False)
    reserved_at = db.Column(db.String(26), nullable=False)
    available_at = db.Column(db.String(26), nullable=False)
    created_at = db.Column(db.String(26), default=now)

    # def __init__(self, id, queue, payload, attempts, reserved, reserved_at, available_at, created_at):
    #     self.id = id
    #     self.queue = queue
    #     self.payload = payload
    #     self.attempts = attempts
    #     self.reserved = reserved
    #     self.reserved_at = reserved_at
    #     self.available_at = available_at
    #     self.created_at = created_at


class FailedJob(db.Model):
    """
    All data being storage on table "failed_jobs"

    id         | integer                        | not null default

    connection | text                           | not null

    queue      | text                           | not null

    payload    | text                           | not null

    failed_at  | timestamp(0) without time zone | not null
    """

    __tablename__ = "failed_jobs"

    id = db.Column(db.Integer, primary_key=True)
    connection = db.Column(db.Text, nullable=False)
    queue = db.Column(db.Text, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    failed_at = db.Column(db.String(26), nullable=False)

    # def __init__(self, id, connection, queue, payload, failed_at):
    #     self.id = id
    #     self.connection = connection
    #     self.queue = queue
    #     self.payload = payload
    #     self.failed_at = failed_at
