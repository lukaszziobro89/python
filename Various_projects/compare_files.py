"""----------------------------------------------------------------------------------

Script compares two .TXT files (line by line) and saves differences in separate file.
Script file and input files to compare needs to be in the same directory, as path to 
file is generated as 'os.cwd (currend working directory)'.

In STEP 1) put names of files which needs to be compared:
- put first file name in line 18 (without .TXT extension)
- put second file name in line 19 (without .TXT extension)
- put output file name in line 20 (without .TXT extension)

---------------------------------------------------------------------------------"""

import time
import os
import sys

# -----------------------------------------------------------------------------------
# put files names (WITHOUT .TXT EXTENSION) here
first_file_name = "first"
second_file_name = "second"
output_file_name = "output"


# -----------------------------------------------------------------------------------

# function creates path to file
def path_to_file(input_filename):
    current_directory = str(os.getcwd())
    initial_path = current_directory + '\\' + str(input_filename) + '.txt'
    first_replace = initial_path.replace('\\\\', '\\')
    final_path = first_replace.replace('\\', '//')
    return str(final_path)


# create paths to both files
first_file_path = path_to_file(first_file_name)
second_file_path = path_to_file(second_file_name)
output_file_path = path_to_file(output_file_name)

# start time counter
start_time = time.time()

# open both files and look for differences (by lines)
try:
    with open(first_file_path, 'r') as first_file:
        with open(second_file_path, 'r') as second_file:
            diff = set(first_file).symmetric_difference(second_file)
    with open(output_file_path, 'w') as output_file:
        for line in diff:
            output_file.write(line)
except FileNotFoundError:
    print("File does not exist.")
    sys.exit("Script execution aborted.")

# create output file and save difference into it

try:
    with open(first_file_path, 'r') as first_file:
        lines_number_first_file = sum(1 for line in first_file)
    with open(second_file_path, 'r') as second_file:
        lines_number_second_file = sum(1 for line in second_file)
    with open(output_file_path, 'r') as output_file:
        lines_number_output_file = sum(1 for line in output_file)
    print("Number of lines in first file: " + str(lines_number_first_file))
    print("Number of lines in second file: " + str(lines_number_second_file))
    print("Number of lines in output file: " + str(lines_number_output_file))
except FileNotFoundError:
    print("File does not exist.")
except NameError:
    print("Variable not defined.")

# stop time counter and print summary
end_time = time.time()
process_time = int(end_time - start_time)
print("Process completed!")
print("Processing time: " + str(process_time) + " seconds.")
