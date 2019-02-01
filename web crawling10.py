from urllib.parse import quote
from requests import urlretrieve

qstr = quote( "cerc india")
do = urlretrieve("https://www.google.com/?q="+qstr)


