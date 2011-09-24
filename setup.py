# -*- coding: utf-8 -*-
"""

    Visioboard Client API


    Example Usage::

        >>> from visioboardclient import send
        >>> dashboard_id = "ID of your dashboard"
        >>> widget_id = "ID of your widget"
        >>> access_key = "Your access key"
        >>> # Setting the image src of a picture widget
        >>> data = {'options': {'src': "http://image/source"}}
        >>> result = send(dashboard_id, widget_id, access_key, data)

    :copyright: (c) 2011 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from setuptools import setup

import client 

setup(
    name = 'VisioboardClient',
    version = client.__version__,
    description = __doc__,

    author = 'Openlabs Technologies & Consulting (P) Limited',
    website = 'http://openlabs.co.in/',
    email = 'info@openlabs.co.in',

    install_requires = [
        "requests",
    ],
    packages = [
        'visioboardclient',
    ],
    package_dir = {
        'visioboardclient': 'client',
    },
    zip_safe = False
)
