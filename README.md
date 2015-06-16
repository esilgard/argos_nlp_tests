# argos_nlp_tests
testing code for the argos NLP pipeline

entry point is argos_nlp_tester.py 
all the individual tests are imported from the Tests directory as modules
paths to the engine version being tested, the input and output files should be put in the args.txt file
args.txt (within the main argos_nlp_tests directory) should be in the form:


engine_path=<path to the folder containing the version of nlp_engine.py being tested>
input_file_name=<path to input file>
json_output_file=<path to output file (this will vary depending on the cwd at runtime)>

the test suite can then be run simply by instantiating argos_nlp_tester.py

test results print to std out
