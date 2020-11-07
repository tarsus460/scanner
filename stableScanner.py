#Python3
# scans documents from the scanner to a folder on the hard drive
# url in question is http://192.168.2.6/#hId-webscanPage Your scanner's IP address may differ
#TODO: Make a config file in which to store things such as IP address, paths to which files should be downloaded, etc.

import os,shutil,datetime,webbrowser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pathlib import Path

pathy = Path(r'C:\Users\phrogg\Documents\Pathy')         # YOUR PATH WILL BE DIFFERENT
pathee = Path(r'C:\Users\phrogg\Documents\Pathee')       # YOUR PATH WILL BE DIFFERENT

options = FirefoxOptions()
options.add_argument('--headless')
profile = webdriver.FirefoxProfile(r'C:\Users\phrogg\AppData\Roaming\Mozilla\Firefox\Profiles\82vk0ft4.StableScanner')
browser = webdriver.Firefox(profile,options=options)
browser.get('http://192.168.1.65/#hId-webscanPage') # YOUR IP WILL BE DIFFERENT

currentList = os.listdir(Path.cwd())
config = 'config.txt'
print('##############################')
print('##### StableScanner v1.2 #####')
print('##############################')
def nameLoop():
    nameQuery = input('Query: Would you like to name your batch of documents today? ')
    global cdate
    if nameQuery == 'y':
        cdate = input('and what would that name be? ')
        configCheck()
    elif nameQuery == 'n':
        cdate = datetime.date.today()
        configCheck()

def fileList():
        n = 1
        #cdate = datetime.date.today()
        for filename in os.listdir(pathy):
                m = str(cdate) + '#' + str(n) + '.pdf'
                shutil.copy( pathy / filename, pathee /str(m))
                n = n + 1

def scanLoop():
    scanning = input('would you like to scan a document? Y/N ')
    while scanning == 'y':
        fileType = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/form/div[1]/div[1]/div/div[1]/div/select/option[1]')
        startScan = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/form/div[2]/div[1]/div[1]/input[1]')    

        fileType.click() # clicks the button to scan the document as pdf
        startScan.click() # clicks the "start scan" button
        scanning = input('would you like to scan another? y/n ')
    if scanning == 'n':
        fileList()
    else:
        print('i\m sorry, that won\'t work')
        scanLoop()
def configCheck():
    print(currentList,'\n\n')
    if config in currentList:
        scanLoop()
    else:
        print('no config found, creating...\n\n')
        p = open('config.txt','a')
        p.write('This is the Program\'s configuration\n\n')
        IP = input('what is your printer\'s IP address?')
        p.write('IP Address: ' + str(IP) + '\n\n')
        global downloadFolder
        downloadFolder = input('What is the download folder for Firefox? ')
        p.write('DownloadPath = ' + downloadFolder)
        p.close()
        scanLoop()
nameLoop()
