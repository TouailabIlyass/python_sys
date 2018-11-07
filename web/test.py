import requests

url="http://192.168.1.18/nagiosxi/includes/components/xicore/status.php?show=hosts"
r=requests.get(url)
print(r.text)