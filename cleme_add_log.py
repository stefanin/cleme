
# importing the requests library
import requests
import socket

# defining the api-endpoint
API_ENDPOINT = "http://localhost:8080/add_hosts"

ip = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()
data = {'ip': ip, 'hostname': hostname}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
