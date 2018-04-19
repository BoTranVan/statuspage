#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: ministry

try:
    from os import system, getuid

    try:
        if getuid() == 0:
            system('apt install python3-dev libmysqlclient-dev && \
                    pip3 install -r requirements.txt')
    except Exception as e:
        print('You must run with root permission.')
except Exception as e:
    raise e
