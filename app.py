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
    from routes.api import *
    db.create_all()

except BaseException as e:
    raise e
