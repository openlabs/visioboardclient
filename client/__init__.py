# -*- coding: utf-8 -*-
"""
    __init__

    A simple webservices client for visioboard

    :copyright: (c) 2011 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import json

import requests

__version__ = "0.1"


def send(dashboard, widget, access_key, data):
    """A utility to send data to a dashboard widget in Visioboard

    :param dashboard: ID of the dashboard
    :param widget: ID of the widget
    :param access_key: Access key for visioboard
    :param data: A data string or dictionary
    """
    url = "http://visioboard.com/api/dashboard/%s/send" % dashboard

    if not isinstance(data, basestring):
        data = json.dumps(data)

    return requests.post(url, {
        'widget': widget,
        'access_key': access_key,
        'data': data,
    })
