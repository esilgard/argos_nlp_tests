#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 7 -verify existence of all expected tables  (at least one of each)

'''
expected_tables=set([u'Pathology',u'PathologyStageGrade',u'PathologyFinding'])
#exptected_fields=set(u'PathFindHistology',u'PathHistology',u'PathSide',u'PathStageT',u'Pathologist',u'PathSpecimenType'
test_num='7'
test_desc='verify existence of all expected tables  (at least one of each)'
import json

def get(json_file_name):
    #try:
    json_data=open(json_file_name)        
    data = json.load(json_data)
    json_data.close()
    table_set=set([])
    field_set=set([])
    num_fields=0
    print len(data['reports'])
    for r in data['reports']:
        #print 'report'
        
        for tables in r['tables']:   ##tabls is a list of dictionaries
            table_set.add(tables['table'])
            for field in tables['fields']:
                field_set.add(field['name'])
                num_fields+=1
    print num_fields,'total field values'
    print table_set
    print field_set
    if table_set==expected_tables:
        return test_num,'Pass',test_desc
    else:
        return test_num,'Fail',test_desc
    #except:        
    #    return test_num,'Fail',test_desc
