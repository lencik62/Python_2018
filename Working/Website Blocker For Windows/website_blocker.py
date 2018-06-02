import time
from datetime import datetime as dt
from datetime import timedelta as td
import os

# message_redirct = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "message.html")
message_redirct = '127.0.0.1 '
# win_host_path = 'C:\Windows\System32\drivers\etc'.replace('\\','\\\\')
win_host_path = r'C:\Windows\System32\drivers\etc\hosts'
block_sites = []
block_sites_path =os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','blocked sities.txt')
# win_host_path = 'hosts/hosts_clean.1'
def add_new_sities():
    while True:
        with open(block_sites_path,'r+') as file:
            temp = input('Enter site name without the www. or http/https. ex:"fb.com". enter "q" to quit ')
            if temp == 'q':
                break
            file.write('{}\n'.format(temp))
    print("Done with adding new blocked sities")
    main()
def blocker(worktime):
    now = dt.now()
    while True:
        time.sleep(20)
        if  dt(now.year, now.month, now.day, now.hour) < dt.now() < dt(now.year, now.month, now.day, 16)+td(seconds = worktime):
            with open(win_host_path, 'r+') as file:
                content  =  file.read()
                for website in block_sites:
                    if website in content:
                        pass
                    else:
                        file.write("{} {}\n".format(message_redirct,website))
                        file.write("{} {}\n".format(message_redirct,'www.'+website))
        else:
            with open(win_host_path, 'r+') as file:
                content  = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in block_sites):
                        file.write(line)
                file.truncate()

def load_block_sites() :
    with open(block_sites_path,'r') as file:
        block_sites.extend(file.readlines())

def get_worktime():
    while True:
        try:
            temp =  float(input("Please Input how many hours you would like to work for? \n > "))
            if(temp >= 0):
                # converting the hours to secouds
                return temp * 360
        except:
            print('!'*10+"invalid input try again"+'!'*10)
def main():
    temp = 0
    while True:
        try:
            temp =  int(input("Hello, Please Select an option from below by entering its number.\
         \n1: run blocker \
         \n2: add new sities\
         \n3: quit"))
            if 0 < temp < 4:
                break
            else:
                raise ValueError("not the right value")
        except:
            print("invaild input try again")
    if temp == 1:
        working_time = get_worktime()
        load_block_sites()
        blocker(working_time)
    if temp == 2:
        add_new_sities()
    if temp == 3:
        exit()
if __name__ == '__main__':
    main()