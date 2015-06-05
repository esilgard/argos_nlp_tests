#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 6 -verify JSON higher level structure - controlInfo, reports, errors

'''

test_num='6'
test_desc='verify JSON higher level structure - controlInfo, reports, errors, their types and that there is at least one report'
import json

def get(json_file_name):
    try:
        json_data=open(json_file_name)        
        data = json.load(json_data)
        json_data.close()
        
        if ('controlInfo' in data and 'reports' in data and 'errors' in data) and\
          ( type(data['controlInfo'])==dict and type(data['reports'])==list and type(data['errors'])==list) and \
          len(data['reports'])>0:   
           
            return test_num,'Pass',test_desc
        else:
            return test_num,'Fail',test_desc
    except:        
        return test_num,'Fail',test_desc
