# -*- coding: utf-8 -*-  

import codecs 
import json
import os
import sys
import shutil
import web

web.config.debug = False

FLAG_SUCCESS = '{"flag":"successful"}'

FLAG_ERROR_FILE_NOT_FOUND = '{"flag":"error","error_no":"10001","msg":"File not found."}'
FLAG_ERROR_TYPE_INVALID = '{"flag":"error","error_no":"10002","msg":"Type invalid."}'

urls = (
    '/', 'index',
    '/getBooking', 'getBooking',
    '/saveBooking', 'saveBooking',

    '/getCustomer', 'getCustomer',
    '/newCustomer', 'newCustomer',

    '/getAllMedicine', 'getAllMedicine',

    '/getRecipe', 'getRecipe',
    '/saveRecipe', 'saveRecipe',

    "/ping", "ping",
    "/count", "count",
    "/reset", "reset"
)


class getRecipe:
    def POST(self):
        return "[]"

    def GET(self):
        i = web.input()
        filename = "data/recipe/" + i.filename
        print "filename:" + filename
        json_str = '[]'
        json_str = readJson(filename)
        #print json_str
        return json_str

class saveRecipe:
    def POST(self):
        data = web.data()
        json_obj = json.loads(data, "UTF-8")
        #print json_obj

        if type({}) == type(json_obj):
            case_no = json_obj.get('case').get('case_no')
            filename = "data/recipe/c" + case_no + ".json"
            print filename

            str_temp = json.dumps(json_obj, ensure_ascii=False, indent=2)
            #print(str_temp)
            writeJson(filename, str_temp)
            return FLAG_SUCCESS
        else:
            print FLAG_ERROR_TYPE_INVALID
            return FLAG_ERROR_TYPE_INVALID

    def GET(self):
        return "[]"

class getAllMedicine:
    def POST(self):
        return "[]"

    def GET(self):
        i = web.input()
        filename = "data/medicine/allMedicine.json"
        print "filename:" + filename
        json_str = '[]'
        json_str = readJson(filename)
        #print json_str
        return json_str

class getCustomer:
    def POST(self):
        return "[]"

    def GET(self):
        i = web.input()
        filename = "data/customer/allCustomer.json"
        print "filename:" + filename
        json_str = '[]'
        json_str = readJson(filename)
        #print json_str
        return json_str

class newCustomer:
    def POST(self):
        data = web.data()
        json_obj = json.loads(data, "UTF-8")
        filename = "data/customer/new_custom.json"
        json_str = readJson(filename)

        try:
            customers = json.loads(json_str, "UTF-8")
        except:
            customers = []

        if type({}) == type(customers):
            customers = []

        if type([]) == type(customers):
            customers.append(json_obj)

            str_temp = json.dumps(customers, ensure_ascii=False, indent=2)
            #print(str_temp)
            writeJson(filename, str_temp)
            return FLAG_SUCCESS
        else:
            return FLAG_ERROR_TYPE_INVALID

    def GET(self):
        return "[]"

class getBooking:
    def POST(self):
        return "[]"

    def GET(self):
        i = web.input()
        filename = "data/booking/" + i.filename
        print "filename:" + filename
        json_str = '[]'
        json_str = readJson(filename)
        #print json_str
        return json_str

class saveBooking:
    def POST(self):
        #i = web.input()
        data = web.data()
        # 从上送数据中获得预约日期
        json_obj = json.loads( data )
        booking_date = json_obj["BookingDate"]
        filename = "data/booking/booking_"+ booking_date +".json"
        str_temp = json.dumps(json_obj, ensure_ascii=False, indent=2)
        writeJson(filename, str_temp)
        return FLAG_SUCCESS

    def GET(self):
        return "[]"

class ping:
    def GET(self):
        return FLAG_SUCCESS


class count:
    def GET(self):
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return ""

def writeJson(filename, data):
    # if( not os.path.exists(filename) ):
    #     makeFile(filename)

    f = codecs.open(filename,'w+','utf-8')
    f.write(data)
    f.close() 
    return FLAG_SUCCESS

def readJson(filename):
    json_str = ""
    #print os.path.exists(filename)
    if(os.path.exists(filename)):
        f = codecs.open( filename,'r','utf-8')
        json_str = f.read()
        f.close()
        # 为了去除BOM 不得不做的检查。
        if codecs.BOM_UTF8 == json_str[:3]:
            json_str = json_str[3:]
    else:
        json_str = FLAG_ERROR_FILE_NOT_FOUND
    return json_str


class index:
    def GET(self):
        return "Welcome to FRT!"




if __name__ == "__main__":
    
    app = web.application(urls, globals())
    session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})
    app.run()
