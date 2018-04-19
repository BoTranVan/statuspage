#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: ministry

try:

    from config import app, db

except BaseException as e:
    raise e



try:
    # app.run(host="0.0.0.0", port=8080, debug="True")

    from models import models

    db.create_all()

    # obj = components.component(name='name')

    obj = components.component()
    obj.update(id=1, name="name", enabled=True)
    # db.session.add(obj)
    # db.session.commit()

except BaseException as e:
    raise e
