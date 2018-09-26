
import  requests
import json

URL= 'https://api.github.com'

def build_url(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response=requests.get(build_url("users/weibo532421"))
    print(better_output(response.text))
    print(response.url)



if __name__=='__main__':
    request_method()