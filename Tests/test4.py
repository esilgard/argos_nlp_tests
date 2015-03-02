#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
#

'''author@esilgard'''

'''
test 4 -make sure accession numbers of txt files match number of input records and that there is some text in each file
'''

test_num='4'
test_desc='make sure accession numbers of txt files match number of input records and that there is some text in each file'
import os,os.path

def get(input_file_name):
    OBX=open(input_file_name,'r').readlines()
    OBX=[a.strip().split('\t') for a in OBX]   
    headers=dict((k,v) for v,k in enumerate(OBX[0]))    
    accessions=set([line[headers.get('FillerOrderNo')] for line in OBX[1:]])
    records=set([])  
    for directory, path, files in os.walk(input_file_name.split('.nlp')[0]+'/'):
        for f in files:            
            if len(open(directory+'/'+f,'r').read())>1:
                records.add(f.strip('.txt'))             
    if records==accessions:        
        return test_num,'Pass',test_desc
    else:        
        return test_num,'Fail',test_desc
