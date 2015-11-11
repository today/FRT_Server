# -*- coding: utf-8 -*-  

import codecs 
import json
import os
import sys
import shutil
import web

web.config.debug = False

urls = (
    '/', 'index',
    '/getBooking', 'getBooking',
    '/saveBooking', 'saveBooking',

    '/getBooking', 'getBooking',
    '/saveBooking', 'saveBooking',

    '/getBooking', 'getBooking',
    '/saveBooking', 'saveBooking',

    '/getBooking', 'getBooking',
    '/saveBooking', 'saveBooking',

    '/getBooking', 'getBooking',
    '/saveBooking', 'saveBooking',

    "/ping", "ping",
    "/count", "count",
    "/reset", "reset"
)

class ping:
    def GET(self):
        return "flag:'successful'"


class count:
    def GET(self):
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return ""

class getBooking:
    def POST(self):
        return "[]"

    def GET(self):
        i = web.input()
        filename = "data/booking/" + i.filename
        #filename = i.filename
        print filename
        json_str = '[]'
        json_str = readJson(filename) 
        return json_str

class saveBooking:
    def POST(self):
        #i = web.input()
        data = web.data()
        # 从上送数据中获得预约日期
        json_obj = json.loads( data )
        booking_date = json_obj["BookingDate"]
        filename = "data/booking/booking_"+ booking_date +".json" 
        writeJson(filename, data):
        return "flag:'successful'"

    def GET(self):
        return "[]"

def writeJson(filename, data):
    if( not os.path.exists(filename) ):
        makeFile(filename)

    f = codecs.open( filename,'w')
    f.write(data)
    f.close() 
    return "flag:'successful'"

def readJson(filename):
    json_str = ""
    if(os.path.exists(filename)):
        f = codecs.open( filename,'r','utf-8')
        json_str = f.read()
        f.close()
    else
        json_str = "flag:'error', error_no=1,msg:'file not exists.'"
    return json_str





class index:
    def GET(self):
        return "Welcome to FRT!"

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})
    app.run()
