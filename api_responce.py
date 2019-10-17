import requests, json

response = requests.get(url = "")
print(response)

from requests import get
response1 = get('https://comcast.service-now.com/nav_to.do?uri=%2F$pa_dashboard.do', auth=('',''))
print(response1)
