# -*- coding: utf-8 -*-
"""

    Visioboard Client API


    Example Usage::

        >>> from visioboardclient import send
        >>> data = {'options': {'src': "http://image/source"}}
        >>> result = send('<Dashbord>', '<Widget>', '<Access Key>', data)

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
