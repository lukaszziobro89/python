# ===================================================================
# ===================================================================
import sys
from tqdm import *
import time
import re
import os
# ===================================================================
# PUT FILE NAME (WITHOUT .TXT EXTENSION) INTO BELOW LINE BETWEEN " "
# ===================================================================

current_arcout_filename = "arc_august"

# ========================================================================================
# DO NOT CHANGE CODE IN 'def' PARTS
# ========================================================================================


def path_to_file(input_filename):
    current_directory = str(os.getcwd())
    initial_path = current_directory + '\\' + str(input_filename) + '.txt'
    first_replace = initial_path.replace('\\\\', '\\')
    final_path = first_replace.replace('\\', '//')
    return str(final_path)


def delimiter_change(file_path, current_delimiter, new_delimiter):
    """ open file, read data from it, replace and close"""
    print("Changing delimiter from '@@' into ',' in progress ...")
    input_file_read = open(file_path, "r+")
    readed_data = input_file_read.read()
    replaced_data = readed_data.replace("@@", ",")
    replaced_data_end = replaced_data.replace("\"", "")
    input_file_read.close()
    # open file again, truncate (as flag "w" does) and put replaced data into file
    input_file_write = open(file_path, "w")
    input_file_write.write(replaced_data_end)
    input_file_write.close()
    log_file.write("Delimiter changed from '@@' into ','\n")
    print("Delimiter changed from '@@' into ','")


def platform_check(platform):
    if re.search(r'\b.*AS400.*\b', platform, re.IGNORECASE):
        platform_changed = 'AS400'
    elif re.search(r'\b.*RACF.*\b', platform, re.IGNORECASE):
        platform_changed = 'RACF'
    elif re.search(r'\b.*PowerBroker.*\b', platform, re.IGNORECASE):
        platform_changed = 'PowerBroker'
    elif re.search(r'\b.*Unix.*\b', platform, re.IGNORECASE):
        platform_changed = 'UNIX'
    elif re.search(r'\b.*Windows.*\b', platform, re.IGNORECASE):
        platform_changed = 'Windows'
    elif re.search(r'\b.*Fileshare.*\b', platform, re.IGNORECASE):
        platform_changed = 'Windows'
    elif re.search(r'\b.*Kerberos.*\b', platform, re.IGNORECASE):
        platform_changed = 'Kerberos'
    elif re.search(r'\b.*MSSQL.*\b', platform, re.IGNORECASE):
        platform_changed = 'MS-SQL'
    elif re.search(r'\b.*Oracle.*\b', platform, re.IGNORECASE):
        platform_changed = 'Oracle'
    elif re.search(r'\b.*Sybase.*\b', platform, re.IGNORECASE):
        platform_changed = 'Sybase'
    else:
        platform_changed = 'PLATFORM UNKNOWN'
    return platform_changed


def get_service_accounts(arcout_file):
    try:
        for i in tqdm(range(num_lines)):
            for line in arcout_file.readlines():
                splitted_string = line.split(',')
                #  set variables of splitted account
                ACCT_GPIN = splitted_string[0]
                ACCT_LOGIN_USED = splitted_string[1]
                ACCT_TYPE = splitted_string[2]
                ACCT_LOCALITY = splitted_string[3]
                PLATFORM_NAME = splitted_string[8]
                # start sorting accounts
                # check if account is personal
                if splitted_string[2] != 'U':
                    if re.search(r'\bSWISS-DD.*\b', ACCT_LOCALITY, re.IGNORECASE):
                        if re.search(r'\bFR.*\b', ACCT_LOGIN_USED, re.IGNORECASE):
                            # Non-Personal Account - SWISS-DD + login starts with FR (IN SCOPE)
                            # change platform name depending on domain (whole platform) or platform list
                            platform_changed = platform_check(PLATFORM_NAME)
                            # check if domain is 'Whole platform' - if yes then change it into platform name
                            if re.search(r'\bWhole Platform.*\b', ACCT_LOCALITY, re.IGNORECASE):
                                domain_changed = platform_changed
                            else:
                                domain_changed = ACCT_LOCALITY
                            # save account into file
                            line_to_write = ACCT_GPIN + ',' + ACCT_LOGIN_USED + \
                                            ',' + ACCT_TYPE + ',' + str(domain_changed) + ',' + str(platform_changed)
                            arctest_cleaned.write(str(line_to_write + '\n'))
                            log_file.write(
                                "Non-Personal Account (SWISS-DD + login FR) included into scope:, {}".format(line))
                        else:
                            # Non-Personal Account but SWISS-DD domain and NOT FR login (NOT IN SCOPE)
                            log_file.write("SWISS-DD (login not FR) account deleted:, {}".format(line))
                    else:
                        # Non-Personal Account not SWISS-DD (IN SCOPE)
                        # change platform name depending on domain (whole platform) or platform list
                        platform_changed = platform_check(PLATFORM_NAME)
                        # check if domain is 'Whole platform' - if yes then change it into platform name
                        if re.search(r'\bWhole Platform.*\b', ACCT_LOCALITY, re.IGNORECASE):
                            domain_changed = platform_changed
                        else:
                            domain_changed = ACCT_LOCALITY
                        # save into file
                        line_to_write = ACCT_GPIN + ',' + ACCT_LOGIN_USED + \
                                        ',' + ACCT_TYPE + ',' + str(domain_changed) + ',' + str(platform_changed)
                        arctest_cleaned.write(str(line_to_write + '\n'))
                        log_file.write("Non-Personal Account included into scope:, {}".format(line))
                else:
                    # Personal account - remove from scope (NOT IN SCOPE)
                    log_file.write("User account deleted,: {}".format(line))
    except AttributeError:
        print("Please provide string separated by comma as argument.")
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e), e)

#  ========================================================================================
# FILE PROCESSING STARTS HERE
#  ========================================================================================
arcout_filepath = path_to_file(current_arcout_filename)
log_file_path = path_to_file("log_file")
arctest_cleaned = path_to_file("arcout_cleaned")

log_file = open(log_file_path, "a")

arctest = open(arcout_filepath, "r+")
arctest_cleaned = open(arctest_cleaned, "w")

num_lines = sum(1 for line in open(arcout_filepath))
print("")
print("---------------------------------------------------")
print("Number of lines in original file: " + str(num_lines))

start_time = time.time()
# 1. Change delimiter from '@@' into ','
delimiter_change(arcout_filepath, "@@", ",")
print("Processing file...")

# 2. Process accounts
get_service_accounts(arctest)

# closing cleaned arcout file
arctest_cleaned.close()

# closing log file
log_file.close()

end_time = time.time()
process_time = int(end_time - start_time)
print("Process completed!")
print("Processing time: " + str(process_time) + " seconds.")
print("")
print("---------------------------------------------------")
