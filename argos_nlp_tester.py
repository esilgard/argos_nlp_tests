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
    last updated October 2014
'''

argos_nlp_engine_path='C:/users/esilgard/Documents/NLPStaples/Repositories/labkey_dev/argos_nlp/nlp_engine.py'
input_file_name='C:/users/esilgard/Documents/NLPStaples/Repositories/Data/lung_training_path_data.nlp.txt'
output_file='C:\Users\esilgard\Documents\NLPStaples\Repositories\json_output.txt'

from Tests import test1,test2,test3,test4,test5,test6

print ',\t'.join(test1.get(argos_nlp_engine_path))
print ',\t'.join(test2.get(input_file_name))
print ',\t'.join(test3.get(output_file))
print ',\t'.join(test4.get(input_file_name))
print ',\t'.join(test5.get(output_file))
print ',\t'.join(test6.get(output_file))
