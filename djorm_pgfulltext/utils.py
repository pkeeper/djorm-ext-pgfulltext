from __future__ import unicode_literals
import psycopg2
import psycopg2.extensions

from django.db import connection
from django.utils.text import force_text


def adapt(text):
    # make sure connection is open
    connection.cursor()
    connection.connection.set_client_encoding('UNICODE')
    text=text
    print type(force_text(text))
    # use Unicode
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE, connection.connection)
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY, connection.connection)
    a = psycopg2.extensions.adapt(force_text(text))
    a.prepare(connection.connection)
    return unicode(a.getquoted(),'utf-8')
