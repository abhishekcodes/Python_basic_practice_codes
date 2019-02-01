import tabula
import os
from tabula import read_pdf
import pandas


#expected_csv = 'C:\Users\abhishek chandel\python program\x.csv'
df =tabula.read_pdf('C:\asdf.pdf',pages="all", multiple_tables=True)
print(df)






    
   
