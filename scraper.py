import urllib.request
import json
from datetime import datetime
from Structure_and_Variables import *


# open, clean and export all data to json file
def open_and_strip():
    ######################################################################
    # formatting of for loop variables and array
    lines_to_open = [[11, 12, 15], [17, 18, 21], [23, 24, 27], [29, 30, 33], [37, 38, 41], [43, 44, 47], [49, 50, 53],
                     [55, 56, 59], [72, 73, 76], [78, 79, 82], [84, 85, 88], [90, 91, 94]]

    #########################################################################
    web_file = open('files_to_read.txt', 'r')
    web_links = web_file.readlines()
    #  text file is parsed from right to left so flip prod type so values line up
    prod_type.reverse()

    # load online text file to local text so it can be parsed
    for url in web_links:

        urllib.request.urlretrieve(url, 'data.txt')
        input_file = open('data.txt', 'r')
        lines = input_file.readlines()
        d = lines[0].split()

        # get file date and change month name to number
        this_file_date = d[-2] + ' ' + d[-1]
        this_file_date = datetime.strptime(this_file_date, '%B %Y').strftime('%m-%Y')

        line_group_counter = 0
        for place in location:
            for comm in comm_type:
                time_counter = 0
                for date in time:
                    d = lines[lines_to_open[line_group_counter][time_counter]].split()
                    time_counter = time_counter + 1
                    d.reverse()
                    for i in range(len(prod_type)):
                        storage[place][comm][prod_type[i]][date].append((this_file_date, float(d[i])))
                # counters keep track of index in the lines_to_open array
                line_group_counter = line_group_counter + 1

    with open('info.json', 'w') as file:
        json.dump(storage, file)
