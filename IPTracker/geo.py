import requests 

print("IP geolocation tracker")
ip = input("enter target IP:")

url = f"http://ip-api.com/json/{ip}"

response = requests.get(url)
data = response.json()

print("---------------")
print(f"[+]country:{data['country']}")
print(f"[+] City:    {data['city']}")   
print(f"[+] ISP:     {data['isp']}")    
print(f"[+] Lat/Lon: {data['lat']}, {data['lon']}") 
print("------------------------------")