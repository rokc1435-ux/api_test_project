import requests
class ApiClient:
    def __init__(self,base_url):
        self.session = requests.Session()
        self.base_url = base_url
    def get(self,path):
        url = self.base_url + path
        response = self.session.get(url)
        print(f"GET {url},{response.status_code}")
        print(f" 响应body: {response.text}")
        return response
    def post(self,path,json=None):
        url = self.base_url + path
        response = self.session.post(url,json=json)
        print(f"POST {url},{response.status_code}")
        print(f" 请求body: {json}")
        print(f" 响应body: {response.text}")
        return response
    def put(self,path,json=None):
        url = self.base_url + path
        response = self.session.put(url,json=json)
        print(f"PUT {url},{response.status_code}")
        print(f" 请求body: {json}")
        print(f" 响应body: {response.text}")
        return response
    def delete(self,path):
        url = self.base_url + path
        response = self.session.delete(url)
        print(f"DELETE {url},{response.status_code}")
        print(f" 响应body: {response.text}")
        return response
    def login(self, username, password):
        path = f"/user/login?username={username}&password={password}"
        response = self.get(path)
        token = response.json().get("message")
        self.session.headers.update({"api_key": token})
        print(f"TOKEN → {token}")
        return response