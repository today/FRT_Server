# -*- coding: utf-8 -*-  

import codecs
import glob
import json
import os
import sys
import shutil

FLAG_SUCCESS = '{"flag":"successful"}'
FLAG_ERROR_FILE_NOT_FOUND = '{"flag":"error","error_no":"10001","msg":"File not found."}'
FLAG_ERROR_TYPE_INVALID = '{"flag":"error","error_no":"10002","msg":"Type invalid."}'

def getAllRecipe():
    # 筛选出 json 文件
    json_files = glob.glob('data/recipe/*.json')

    all_json = []
    for filename in json_files:
        print "FILENAME:" + filename
        json_str = readJson(filename)
        json_obj = json.loads(json_str, "UTF-8")
        #print json_str
        all_json.append(json_obj)
    return  all_json

def getAllBooking():
    # 筛选出 json 文件
    json_files = glob.glob('data/booking/*.json')

    all_json = []
    for filename in json_files:
        print "FILENAME:" + filename
        json_str = readJson(filename)
        json_obj = json.loads(json_str, "UTF-8")
        #print json_str
        all_json.append(json_obj)
    return  all_json


def saveRecipe(recipe_obj):
    #print json_obj
    if type({}) == type(recipe_obj):
        case_no = recipe_obj.get('case').get('case_no')
        filename = "data/temp/c" + case_no + ".json"
        print filename
        str_temp = json.dumps(recipe_obj, ensure_ascii=False, indent=2)
        #print(str_temp)
        writeJson(filename, str_temp)
        print FLAG_SUCCESS
        return FLAG_SUCCESS
    else:
        print FLAG_ERROR_TYPE_INVALID
        return FLAG_ERROR_TYPE_INVALID

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
        if codecs.BOM_UTF8 == json_str[:3] :
            json_str = json_str[3:]
    else:
        json_str = FLAG_ERROR_FILE_NOT_FOUND
    return json_str





if __name__ == "__main__":
    all_booking = getAllBooking()
    all_recipe = getAllRecipe()

    all_booking_detail = []
    for booking_by_date in all_booking :
        #print booking_by_date
        for booking in booking_by_date.get('bookinglist'):
            all_booking_detail.append(booking)

    for recipe in all_recipe:
        if recipe.has_key('patient_name'):
            print recipe.get('patient_name')
        else:
            case_no_in_recipe = recipe.get('case').get('case_no')
            print 'patient lost. case_no:' + case_no_in_recipe
            for booking_detail in all_booking_detail:
                #print booking_detail
                case_no_in_booking = booking_detail.get('case_no')
                if case_no_in_booking == case_no_in_recipe:
                    print booking_detail.get('name')
                    recipe['case']['patient_name'] = booking_detail.get('name')
                    recipe['case']['patient_no'] = booking_detail.get('patient_no')
                    recipe['case']['sex'] = booking_detail.get('sex')
                    recipe['case']['age'] = booking_detail.get('age')
                    recipe['case']['mobile'] = booking_detail.get('mobile')
                    saveRecipe(recipe)
                    break




