import requests

# with open('ljh.jpg', 'wb') as f:
#     f.write(r.content)

# print(r.headers)

# print(r.status_code) # 200 is success, 300 is redirect, 400 is client error, 500 is server error

# print(r.ok) # True if status_code is less than 400

# print(r.headers)

# # httpbin.org is a great site to test HTTP requests
# payload = {'username': 'sadie', 'password': 'testing'}
# r = requests.post('https://httpbin.org/post', data=payload)

# r_dict = r.json()

# print(r_dict['form'])

# #put example

r = requests.get('https://httpbin.org/delay/2', timeout=4)
print(r)
                                                                      


