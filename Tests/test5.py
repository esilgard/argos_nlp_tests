#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 5 -make sure JSON file is JSON object

'''

test_num='5'
test_desc='make sure JSON file is JSON object'
import json

def get(json_file_name):
             
    try:
        json_data=open(json_file_name)
        data = json.load(json_data)
        json_data.close()
        return test_num,'Pass',test_desc
    except:        
        return test_num,'Fail',test_desc
