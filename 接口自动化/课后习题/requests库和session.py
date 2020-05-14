import requests
import json

# payload = {
#     "Overall": "良好",
#     "Progress": "30%",
#     "Problems": [
#         {
#             "No": 1,
#             "desc": "问题1...."
#         },
#         {
#             "No": 2,
#             "desc": "问题2...."
#         },
#     ]
# }

# r = requests.post("http://httpbin.org/post", data=json.dumps(payload).encode('utf8'))
# # r = requests.post("http://httpbin.org/post", json=payload)
# print(r.text)

# payload = '''
# <?xml version="1.0" encoding="UTF-8"?>
# <WorkReport>
#     <Overall>良好</Overall>
#     <Progress>30%</Progress>
#     <Problems>暂无</Problems>
# </WorkReport>
# '''

# r = requests.post("http://httpbin.org/post", data=payload.encode('utf8'))
# print(r.text)
response = requests.post("http://httpbin.org/post", data={1: 1, 2: 2})

obj = json.loads(response.content.decode('utf8'))
print(obj)
