import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from newfile import application

def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ["Bot is Running!"]