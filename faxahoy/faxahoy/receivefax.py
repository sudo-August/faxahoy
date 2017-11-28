#!/usr/bin/env python
"""Fax snippet."""

from flask.ext.script import Manager
from flask import Flask, Response, request

@app.route('/fax/sent', methods=['POST'])
def fax_sent():
    twiml = """
        <Response>
            <Receive action="/fax/received"/>
        </Response>
    """

    return Response(twiml, mimetype='text/xml')


@app.route('/fax/received', methods=['POST'])
def fax_received():
    """ Will put email send function in here """
    print(request.form.get('MediaUrl'))

    return '', 200