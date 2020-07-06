#Python3
# scans documents from the scanner to a folder on the hard drive
# url in question is http://192.168.2.6/#hId-webscanPage Your scanner's IP address may differ


import webbrowser
from selenium import webdriver

# TODO: Launch Firefox with the newly created Selenium profile which downloads PDFs by default

browser = webdriver.Firefox()
browser.get('http://192.168.2.6/#hId-webscanPage')
scanning = input('would you like to scan a document? Y/N ')

while scanning == 'y':
    fileType = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/form/div[1]/div[1]/div/div[1]/div/select/option[1]')
    userElem = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/form/div[2]/div[1]/div[1]/input[1]')
# TODO: locate the download button on the pdf frame
    fileType.click() # clicks the button to scan the document as pdf
    userElem.click() # clicks the "start scan" button

# TODO: click the button and specify a folder in which to save the new pdf
    
    scanning = input('would you like to scan another? y/n ')
