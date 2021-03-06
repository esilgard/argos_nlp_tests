#
# Copyright (c) 2015 Fred Hutchinson Cancer Research Center
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


'''
    initial script for automated testingof the Argos/NLP engine output
    input is the path to the version of the nlp_engine being tested and the name of the input file to the nlp_engine
    output is single text file written to the argos_nlp_tester directory with all tests run and outcomes
    (one per line, tab delimited)
    test_name<tab>outcome(success or failure)<tab>description
    author@esilgard
    
'''
import os,sys
path= os.path.dirname(os.path.realpath(__file__))+'/'

try:
    args=dict((x.split('=')[0],x.split('=')[1].strip()) for x in open(path+'args.txt','r').readlines())
    print 'file arguments for testing:'
    for k,v in args.items():
        print k,v
    print ''
except:
    print 'FATAL ERROR, args.txt does not exist in the argos_nlp_tester directory or is not formatted correctly, refer to the README file for more info'
    sys.exit(1)


from Tests import test1,test2,test3,test4,test5,test6,test7

print ',\t'.join(test1.get(args['engine_path']+'nlp_engine.py'))
print ',\t'.join(test2.get(args['input_file_name']))
print ',\t'.join(test3.get(args['json_output_file']))
print ',\t'.join(test4.get(args['input_file_name']))
print ',\t'.join(test5.get(args['json_output_file']))
print ',\t'.join(test6.get(args['json_output_file']))
print ',\t'.join(test7.get(args['engine_path']+'metadata.json'))
