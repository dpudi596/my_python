import requests, json

response = requests.get(url = "https://comcast.service-now.com/nav_to.do?uri=%2F$pa_dashboard.do")
print(response)

from requests import get
response1 = get('https://comcast.service-now.com/nav_to.do?uri=%2F$pa_dashboard.do', auth=('dpudi200','Sridevi2121'))
print(response1)
