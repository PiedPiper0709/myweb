#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Guan Ming'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user':'root',
        'password': '123456',
        'db': 'guanming'
    },
    'session': {
        'secret': 'admistrator'
    }
}
