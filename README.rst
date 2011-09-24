Visioboard Client API
=====================

A python client based on the requests library to send data to
visioboard widgets.

Example Usage
-------------

::

        from visioboardclient import send
        # Set the src of an image widget
        data = {'options': {'src': "http://image/source"}}
        result = send('<Dashbord>', '<Widget>', '<Access Key>', data)
