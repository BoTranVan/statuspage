#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: ministry

try:

    from config import app, db


except BaseException as e:
    raise e



try:
    # app.run(host="0.0.0.0", port=8080, debug="True")

    # from models import *

    # db.create_all()

    # obj = cache.cache(key="This is key", value="This is value", expiration=9)

    # db.session.add(obj)
    # db.session.commit()

except BaseException as e:
    raise e
