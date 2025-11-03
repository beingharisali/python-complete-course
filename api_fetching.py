import requests
api_url = "https://www.course-api.com/react-tours-project"

response = requests.get(api_url)
data = response.json()
print(data)
# CRUD
# C - create - POST
# R - read - GET
# U - update - PATCH / PUT
# D - delete - DELETE