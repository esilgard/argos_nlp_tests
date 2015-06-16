#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 7 -verify appropriate JSON structure in metadata dictionary
'''

test_num='7'
test_desc='verify JSON structure of metadata dictionary along with some expected data types'
import json

def get(metadata_file_name):   
    try:
        metadata_file=open(metadata_file_name,'r')
        data = json.load(metadata_file)       
        metadata_file.close()
        
        if ( 'cytogenetics' in data and 'clinical' in data and 'pathology' in data) and\
          ( type(data['cytogenetics'])==dict and type(data['clinical'])==dict and type(data['pathology'])==dict) and \
          ( len(data['cytogenetics'])>0 and len(data['clinical'])>0 and len(data['pathology'])>0 ):   
           
            return test_num,'Pass',test_desc
        else:
            return test_num,'Fail',test_desc
    except:        
        return test_num,'Fail',test_desc
