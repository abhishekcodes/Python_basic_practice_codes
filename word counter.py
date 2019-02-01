import requests

from BeautifulSoup4 import beautifulsoup as soup
import operator
 
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soups = soup(source_code)
    for post_text in soups.findAll('a',{'class': "mar_b" }):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)
        clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = r"!@#$%^&*()_+<>{}:\"[];'.,/\|"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"")
            
        


start('http://www.cercind.gov.in/')
        
