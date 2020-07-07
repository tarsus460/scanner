#Python3
# scans documents from the scanner to a folder on the hard drive
# url in question is http://192.168.2.6/#hId-webscanPage Your scanner's IP address may differ


import os,shutil,datetime,webbrowser
from selenium import webdriver
from pathlib import Path

def fileList():
        n = 1
        cdate = datetime.date.today()
        for filename in os.listdir(pathy):
                m = str(cdate) + '#' + str(n) + '.pdf'
                shutil.copy( pathy / filename, pathee /str(m))
                n = n + 1
# TODO: change the folder to which files downloaded in Firefox are saved
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print('!!!!!!!WAIT FOR FIREFOX TO LOAD THE PAGE BEFORE GIVING INPUT!!!!!!!')
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
pathy = Path(r'C:\Users\mille\Downloads\test') # YOUR PATH WILL BE DIFFERENT
pathee = Path(r'G:\Documents\scansMain')       # YOUR PATH WILL BE DIFFERENT
#TODO: Open the Selenium Firefox profile whenever Firefox is launched from this program
browser = webdriver.Firefox()
browser.get('http://192.168.2.6/#hId-webscanPage') # YOUR IP WILL BE DIFFERENT
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
    
    #scanning = input('would you like to scan another? y/n ')
