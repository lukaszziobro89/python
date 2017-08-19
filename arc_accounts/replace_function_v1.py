import datetime
import sys
from tqdm import *
import time
import re

log_name = str("log_name_") + str(datetime.datetime.now().strftime("%Y-%m-%d %H.%M"))
log_file = open("C:\\Users\luq\Desktop\\arcout\{}.txt".format(log_name), "a")


arctest = open("C:\\Users\luq\Desktop\\arcout\\arctest-ccdd.txt", "r+")
arctest_cleaned = open("C:\\Users\luq\Desktop\\arcout\\arctest_cleaned.txt", "w")

num_lines = sum(1 for line in open("C:\\Users\luq\Desktop\\arcout\\arctest-ccdd.txt"))
print("Number of lines in original file: " + str(num_lines))

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
              #set variables of splitted account
              ACCT_GPIN = splitted_string[0]
              ACCT_LOGIN_USED = splitted_string[1]
              ACCT_TYPE = splitted_string[2]
              ACCT_LOCALITY = splitted_string[3]
              PLATFORM_NAME = splitted_string[8]
              #start sorting accounts
              #check if account is personal
              if splitted_string[2] != 'U':
                  if (re.search(r'\bSWISS-DD.*\b', ACCT_LOCALITY, re.IGNORECASE)):
                      if (re.search(r'\bFR.*\b', ACCT_LOGIN_USED, re.IGNORECASE)):
                        # Non-Personal Account - SWISS-DD + login starts with FR (IN SCOPE)
                         #change platform name depending on domain (whole platform) or platform list
                         platform_changed = platform_check(PLATFORM_NAME)
                         #check if domain is 'Whole platform' - if yes then change it into platform name
                         if (re.search(r'\bWhole Platform.*\b', ACCT_LOCALITY, re.IGNORECASE)):
                             domain_changed = platform_changed
                         else:
                             domain_changed = ACCT_LOCALITY
                         #save account into file
                         line_to_write = ACCT_GPIN + ',' + ACCT_LOGIN_USED+\
                                ',' + ACCT_TYPE+ ',' + str(domain_changed) + ',' + str(platform_changed)
                         arctest_cleaned.write(str(line_to_write+'\n'))
                         log_file.write("Non-Personal Account (SWISS-DD + login FR) included into scope,: {}".format(line))
                      else:
                         # Non-Personal Account but SWISS-DD domain and NOT FR login (NOT IN SCOPE)
                         log_file.write("SWISS-DD (login not FR) account deleted,: {}".format(line))
                  else:
                  #Non-Personal Account not SWISS-DD (IN SCOPE)
                      # change platform name depending on domain (whole platform) or platform list
                      platform_changed = platform_check(PLATFORM_NAME)
                         #check if domain is 'Whole platform' - if yes then change it into platform name
                      if (re.search(r'\bWhole Platform.*\b', ACCT_LOCALITY, re.IGNORECASE)):
                          domain_changed = platform_changed
                      else:
                          domain_changed = ACCT_LOCALITY
                      #save into file
                      line_to_write = ACCT_GPIN + ',' + ACCT_LOGIN_USED + \
                              ',' + ACCT_TYPE + ',' + str(domain_changed) + ',' + str(platform_changed)
                      arctest_cleaned.write(str(line_to_write + '\n'))
                      log_file.write("Non-Personal Account included into scope,: {}".format(line))
              else:
                  #Personal account - remove from scope (NOT IN SCOPE)
                  log_file.write("User account deleted,: {}" .format(line))
    except AttributeError:
        print("Please provide string separated by comma as argument.")
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e), e)


def delimiter_change(file_path, current_delimiter, new_delimiter):
        #open file, read data from it, replace and close
    print("Changing delimiter from '@@' into ',' in progress ...")
    input_file_read = open(file_path, "r+")
    readed_data = input_file_read.read()
    replaced_data = readed_data.replace("@@", ",")
    input_file_read.close()
        #open file again, truncate (as flag "w" does) and put replaced data into file
    input_file_write = open(file_path, "w")
    input_file_write.write(replaced_data)
    input_file_write.close()
    log_file.write("Delimiter changed from '@@' into ','\n")
    print("Delimiter changed from '@@' into ','")


start_time = time.time()
#1. Change delimiter from '@@' into ','
delimiter_change("C:\\Users\luq\Desktop\\arcout\\arctest-ccdd.txt","@@",",")

#2. Process accounts
get_service_accounts(arctest)

#closing cleaned arcout file
arctest_cleaned.close()

#closing log file
log_file.close()

end_time = time.time()
process_time = int(end_time - start_time)
print("Process completed!")
print("Processing time: " + str(process_time) + " seconds.")