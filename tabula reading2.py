import os
import pandas as pd

from tabula import read_pdf

df = read_pdf(r"C:\Users\abhishek chandel\python program\x.pdf", pages="all")
print(df)
