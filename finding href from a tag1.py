# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:01:13 2018

@author: abhishek chandel
"""

from bs4 import BeautifulSoup as BS
import pandas as pd
import numpy as np
import urllib.request
import datetime
import urllib
import tabula

#%y gives date in 2 digits and %Y gives data in 4 digits    
Date = datetime.datetime.now().strftime("%d-%m-%y")
Date = str(Date)
print(Date)
   
Download_page='https://posoco.in/reports/daily-reports/daily-reports-2017-18'


#try:
    #page = urllib.request.urlopen(Download_page).read()
#except (urllib.IncompleteRead) as e:
    #page = e.partial
    
    
page= urllib.request.urlopen(Download_page).read()
prossd_page= BS(page, 'lxml')
#print(prossd_page.body.span)
#grabbing link of download
#convertingslinks into string
#dwnld_links_ra= str(dwnld_links)

#link1= str.find("https://posoco.in/download/"

dwnld_links = prossd_page.findAll("a", href= True)
x = "https://posoco.in/download/"+Date+"_nldc_psp/?wpdmd1=    "
if x in dwnld_links:
    print(x)

#to get the table content
dwnld_link_td =prossd_page.td.a
dwnld_str= str(dwnld_link_td)
element= dwnld_str.split()
dwn_lnk= str(element[1])
act_dwn_lnk= dwn_lnk[6:64]
urllib.request.urlretrieve(act_dwn_link, filename= "NLDC.pdf")


df = tabula.read_pdf(r'C:\Users\abhishek chandel\python program\NLDC.pdf', encoding="cp932",pages="all", multiple_tables=True)
Regional_data = df[0]
FREQ = pd.DataFrame(df[1])
PSPS = pd.DataFrame(df[2])
ICTE = pd.DataFrame(df[3])
IER =  pd.DataFrame(df[4])
GEN_OUT = pd.DataFrame(df[5])
SOURCE_GEN = pd.DataFrame(df[6])
IR_EX = pd.DataFrame(df[7])

IR_EX.to_csv("Inter_regional_exchange.csv")
PSPS.to_csv("PSPS.csv")

#for a in dwnld_links.find_all("a", text=re.complie('wpdmd1')):
    #for tr in prossd_page.find_all('tr'):
    #td = tr.find('td')
    #if td:
        #print(td)print(a['href'])
#rqr_tag= "<html><body><tr><td><a href=''/></td></tr></body></html>"
#print(BS(rqr_tag,'lxml'))
#a_tags=prossd_page.findAll(('a'))




#this function will download the file form the text generated from the scraping     
#urllib.request.urlretrieve("https://posoco.in/download/05-03-18_nldc_psp-pdf/?wpdmdl=16569","x.pdf")
   
#to import it into excel csv using
#import csv
#from datetime import datetime
    # open a csv file with append, so old data will not be erased
#with open(‘index.csv’, ‘a’) as csv_file:
 #writer = csv.writer(csv_file)
# writer.writerow([name, price, datetime.now()]) 
 
 
 #table_data= prossd_page.find("table",attrs={"class":"table table-striped wpdm-all-packages-table dataTable no-footer"})
