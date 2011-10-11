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


class Data(object):
    """A base class helper to facilitate easy data entry
    """

    #: Options for the ocnfiguration of widgets
    options = None

    #: Series - the raw data series to be pushed for rendering
    series = None

    def __init__(self):
        self.options = {}
        self.series = []

    @property
    def data_dict(self):
        return {
            'options': self.options,
            'series': self.series,
            }


class GeoChart(Data):
    """Data for a Geo Chart"""

    def __init__(self, region='world', resolution='countries'):
        """
        :param region: The area to display on the map. (Surrounding areas will 
                       be displayed as well.) Can be either a country code (in
                       uppercase ISO-3166 format), or a one of the following 
                       strings:
                        * world - (Whole world -- Default)
                        * 005 - (South America)
                        * 013 - (Central America)
                        * 021 - (North America)
                        * 002 - (All of Africa)
                        * 017 - (Central Africa)
                        * 015 - (Northern Africa)
                        * 018 - (Southern Africa)
                        * 030 - (Eastern Asia)
                        * 034 - (Southern Asia)
                        * 035 - (Asia/Pacific region)
                        * 143 - (Central Asia)
                        * 145 - (Middle East)
                        * 150 - (Europe)
                        * 151 - (Northern Asia)
                        * 154 - (Northern Europe)
                        * 155 - (Western Europe)
                        * 039 - (Southern Europe)
        :param resolution:  The resolution of the map borders. 
                            Choose one of the following values:
                            * 'countries'
                            * 'provinces' - Not supported for all countries; 
                                please test a country to see whether this 
                                option is supported.
                            * 'metros' - USA only.
        """
        super(GeoChart, self).__init__()
        self.options['resolution'] = resolution
        self.options['region'] = region
        self.options['cols'] = []

    def add_column(self, id, label, type):
        """Add a column
        """
        self.options['cols'].append({'id': id, 'label': label, 'type': type})

    def add_row(self, values):
        """Adds a row
        """
        self.series.append({'c': [{'v': v} for v in values]})


class Client(object):
    """A client class which provides widget specific functionality
    """

    def __init__(self, dashboard, access_key):
        """
        :param dashboard: ID of the dashboard
        :param access_key: Access key for visioboard
        """
        self.dashboard = dashboard
        self.access_key = access_key

    def picture(self, widget, source, href=None):
        """Send data to a picture widget.

        :param source: The uri of the image that has to be displayed
        :param href: The link that has to be opened when the image is clicked
        """
        pass

    def geo_chart(self, widget, data):
        """Sends data to a Geo Chart widget on dashboard
        """
        if isinstance(data, Data):
            data = data.data_dict
        return send(self.dashboard, widget, self.access_key, data)
