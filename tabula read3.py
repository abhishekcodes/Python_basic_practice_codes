import tabula
import os
import pandas as pd
 
folder = r'Users\abhishek chandel\python programs'
paths = [folder + fn for fn in os.listdir(folder) if fn.endswith('.pdf')]
for path in paths:
    df = tabula.read_pdf(path, encoding = 'cp932', pages = 'all', spreadsheet = True)
    path = path.replace('pdf', 'csv')
    df.to_csv(path, index = False)
