#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 3 - make sure that the path to the JSON output file is valid

'''

test_num='3'
test_desc='make sure that the JSON output file name is valid'


def get(json_file_name):
    try:
        json_output=open(json_file_name,'r').read()
        return test_num,'Pass',test_desc
    except:
        return test_num,'Fail',test_desc
