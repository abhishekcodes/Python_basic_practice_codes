from bs4 import BeautifulSoup as BS
import pandas as pd
import numpy as np
import urllib.request
import datetime
import urllib

#%y gives date in 2 digits and %Y gives data in 4 digits    
Date = datetime.datetime.now().strftime("%d-%m-%y")
Date = str(Date)
print(Date)

Download_page='https://posoco.in/reports/daily-reports/daily-reports-2017-18'
page= urllib.request.urlopen(Download_page).read()
prossd_page= BS(page, 'lxml')
dwnld_links = prossd_page.findAll("a", href= True)
dwnld_link_td = prossd_page.td.a
dwnld_str= str(dwnld_link_td)
element= dwnld_str.split()
dwn_lnk= str(element[1])
act_dwn_lnk= dwn_lnk[6:64]

urllib.request.urlretrieve(act_dwn_Link, filename= "NLDC.pdf") 
