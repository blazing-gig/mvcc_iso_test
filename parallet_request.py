
import threading

import requests
import time

# Retrieve a single page and report the URL and contents
def load_url(url, method, timeout, json = None):
    # headers = {
    #     "Authorization": "Token 5e2bcb35bcac3c250aae9b7860a854073279a7f6"
    # }
    if method == "get":
        r = requests.get(url, timeout = timeout, params = None)
    elif method == "put":
        r = requests.put(url, timeout = timeout, json = json)
    elif method == "delete":
        r = requests.delete(url, timeout = timeout, json = json)
    else:
        r = requests.post(url, timeout = timeout, json = json)
    # print(r.json())
    return method, r.json()





# st_time = time.time()
#
threads = []

URLS = [
        'http://localhost:8000/book/' for i in range(2)
    ]

# sleep_times = [ 0, 2 ]
methods = ["put", "post"]

for index, url in enumerate(URLS):
    threads.append(
        threading.Thread(target = load_url, args = (url, methods[index], 10, {
            "author_1": "Dan",
            "author_2": "Brown"
        }))
    )

for index, t in enumerate(threads):
    if index == 1:
        time.sleep(0.010)
    t.start()

# for t in threads:
#     t.join()
#
# print("time taken ", time.time() - st_time)

# for url in URLS:
#     res = load_url(url, 2)
#     print("url and res is ", url, len(res))
#
# print("time taken ", time.time() - st_time)