import requests

url = "http://127.0.0.1:8000"

# 127.0.0.1:8000/docsにアクセスするとswagger確認できる
get = requests.get(url)
get_sample = requests.get(f"{url}/sample")
get_item = requests.get(f"{url}/items/100")
delete = requests.delete(url)

def check_api(request):
    print(request.status_code)
    print(request.text)

check_api(get)
check_api(get_sample)
check_api(get_item)
check_api(delete)