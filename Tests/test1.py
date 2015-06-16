#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 1 - make sure that the path to the nlp_engine is valid (the python script exists)

'''

test_num='1'
test_desc='make sure that the path to the nlp_engine is valid'


def get(engine_path):
    try:        
        python_script=open(engine_path,'r').read()
        return test_num,'Pass',test_desc
    except:
        return test_num,'Fail',test_desc
    
