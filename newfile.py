import sys
import os

# اضافه کردن مسیر فعلی به سیستم
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ایمپورت ربات تو - نام فایل تو newfile.py هست
from newfile import application

# تابع اصلی برای Passenger
def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ["Bot is Running!"]