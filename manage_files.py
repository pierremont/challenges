###! /bin/python
#@author: petrus.munteanu, 2020
#due to lack of time, the script is not at all optimized. Repetitions and small mistakes are bound to exist here, but feel free to improve the script as you find fit

import os, fnmatch
import datetime

search_dir = "c:\\workspace\\python\manage_files"
#search_dir = "c:\\users\\public\\workspace\\pycharm\\test_files"
#search_dir = "/home/ctm_user/devops/mongo/dumps/prd/test/test_files"
dest_dir = 'c:\\workspace\\python\\manage_files\\move_folder'

# how many months the script will process
# The script will ignore the last 2 months - excluding # the current one
# so if you put in 6 months, the script will process 4 months -> from 6 months ago until 2 months ago:
num_months = 6

''' extract the last month date '''
# date = (datetime.datetime.today() - datetime.timedelta(30)).strftime("%d-%b-%Y") #a month ago'
# date = first_day - datetime.timedelta(days=1)   #last date of the previous month
# print(date.strftime("%Y_%m"))

def find_months():
    month_list = []
    today = datetime.date.today()
    beautiful_day = today.replace(day=10)  # the tenth day of the current month
    for i in range(num_months, 2, -1):
        date = beautiful_day - datetime.timedelta(days=30 * i)
        month_list.append(str(date.strftime("%Y_%m")))
    return month_list
month_list = find_months()


'''  6 files of every month except the last 2 months '''
backup_candidates = []
def search_files (iter_mon):
    iter_backup_candidates = []
    print("looking for files for the " + iter_mon + " month")
    for y in range(1, 29):  #we search each day
        for file in os.listdir(search_dir):
            if len(iter_backup_candidates) != 6:
                if fnmatch.fnmatch(file, str(iter_mon) + "_" + str(y).zfill(2) + "*"):
                    iter_backup_candidates.append(file)
            elif not iter_backup_candidates:
                print("nothing")
            else:
                backup_candidates.append(iter_backup_candidates)
                return (backup_candidates)
        iter_backup_candidates = []

for iter_mon in month_list:
    search_files(iter_mon)

for k in backup_candidates:
    print('the following files are elligible for movin to the permanent backup')
    print ("\n".join(k))
''' move the candidate files in the permanent backup folder '''

''' delete the older files except the current month '''

