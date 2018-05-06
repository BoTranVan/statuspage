#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: ministry

try:

    from config import app, db

except BaseException as e:
    raise e

try:
    # app.run(host="0.0.0.0", port=8080, debug="True")
    from models import *

    db.create_all()

    obj = incidents.incident().get()
    print(obj)


except BaseException as e:
    raise e
