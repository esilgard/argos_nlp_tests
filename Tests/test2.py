#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 2 - make sure that the path to the nlp_engine is valid

'''

test_num='2'
test_desc='make sure that the input file name is valid'


def get(input_file_name):
    try:
        python_script=open(input_file_name,'r').read()
        return test_num,'Pass',test_desc
    except:
        return test_num,'Fail',test_desc
