from datetime import datetime
from time import sleep
import re

LOG_FILE = 'c:\\program files (x86)\\grinding gear games\\path of exile\\logs\\client.txt'
LOAD_AREA_TEXT = 'You have entered '
LOAD_AREA_LEN = len(LOAD_AREA_TEXT)

area_name = ''
load_time = None
load_start_time = None

# fetch log to get current offset
client_log = open(LOG_FILE, 'r', encoding='utf8')
log_offset = len(client_log.read())
# main loop
while True:
    # check log file
    log_data = client_log.read(log_offset)
    if not log_data:
        # wait for log to be appended
        sleep(0.001)
        continue
    # change offset to the new end of the log
    log_offset += len(log_data)

    # check if area load started
    if 'Got Instance Details from login server' in log_data:
        load_start_time = datetime.now()
    # check if area load finished
    if 'You have entered ' in log_data and load_start_time:
        load_end_time = datetime.now()
        load_duration = load_end_time - load_start_time
        load_time = '{}.{}'.format(load_duration.seconds, round(load_duration.microseconds * 0.001))
        # reset load_start_time
        load_start_time = None
        # get the area name
        area_name_offset = log_data.find(LOAD_AREA_TEXT) + LOAD_AREA_LEN
        area_name = ''
        area_char = log_data[area_name_offset]
        while area_char != '.':
            area_name += area_char
            area_name_offset += 1
            area_char = log_data[area_name_offset]

    # check if area is loaded
    if load_time:
        # show load time
        print('{} loaded in {} seconds'.format(area_name, load_time))
        # reset load_time
        load_time = None

client_log.close()
