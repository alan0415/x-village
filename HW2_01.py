import pandas as pd
import requests
url = 'http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=948aaefa-3d1e-4e0a-84f7-e5374730d592'
r = requests.get(url)
r.encoding = 'utf-8-sig'
print(r.text)