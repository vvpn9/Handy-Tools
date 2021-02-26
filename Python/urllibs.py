import requests

r = requests.get('http://www.tmall.com')

print(r.encoding)  # utf-8

print(type(r.headers))  # <class 'requests.structures.CaseInsensitiveDict'>

print(r.headers['Content-type'])  # text/html; charset=utf-8

# print(r.content) too much contents here
