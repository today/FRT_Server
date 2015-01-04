# -*- coding: utf-8 -*-  

import codecs 
import json
import os
import sys
import shutil
import web



urls = (
    '/', 'index',
    '/add', 'add',
    '/getBooking', 'getBooking',
    '/saveBooking', 'saveBooking'
)

class getBooking:
    def POST(self):
        return "[]"

    def GET(self):
        i = web.input()
        filename = "data/booking/" + i.filename
        #filename = i.filename
        print filename
        json_str = '[]'
        if(os.path.exists(filename)):
            f = codecs.open( filename,'r','utf-8')
            json_str = f.read()
            f.close()  
        return json_str

class saveBooking:
    def POST(self):
        #i = web.input()
        data = web.data()
        # 从上送数据中获得预约日期
        json_obj = json.loads( data )
        booking_date = json_obj["BookingDate"]
        filename = "data/booking/booking_"+ booking_date +".json" 
        f = codecs.open( filename,'w')
        f.write(data)
        f.close() 
        return "{flag:'successful'}"

    def GET(self):
        return "[]"

class add:
    def POST(self):
        i = web.input()
        json_data = i.json_data
        #n = db.insert('todo', title=i.title)
        return "Welcome to FRT!" + json_data

    def GET(self):
    	#return "Welcome to FRT! GET"
        raise web.seeother('/')


class index:
    def GET(self):
        return "Welcome to FRT!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
