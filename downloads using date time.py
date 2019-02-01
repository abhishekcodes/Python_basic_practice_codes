# defining new download function
import os
import datetime
import urllib.requests

def Download_pdf():
    #this gives the date to the variable date as a string which can be used later
    Date = datetime.datetime.now().strftime("%d-%m%y")
    Date = str(Date)
try :
    urllib.requests.urlretrievers('https://posco.in/download/'+Date+'_nldc_psp/')

except:
    print ('time out.. retrying..')
    time.sleep(1000)

download_pdf()

driver.maximize_window()
webDriverWait(driver,20)
time.sleep(10)
try:
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/main/article/div/div/div/div[2]/table/tbody/tr[5]/td/a').click()
    time.sleep(10)
    shutil.move("\Users\abhishek chandel\python program",'\Users\abhishek chandel\Desktop''\nldc files')

except:
    print('file not found... retrying..')
    time.sleep(1800)

Download.pdf()
            
    
