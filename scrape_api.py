import requests
import pandas as pd
res=[]
url = "https://www.cpppc.org/en/content/page"
for x in range(1,5):
    querystring = {"channelIds":"3513","orderBy":"27","page":f"{x}","size":"20"}

    payload = ""
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "SESSION=MGIxYmU2MzgtMjAwMi00ZjMxLTkxNWEtZDdmOGYzNDdkNzU4; JIDENTITY=abe66769-a810-4bf0-98f4-d4470a81f84b; JIDENTITY=622dff77-3c3c-402d-84d4-1fa7fac6a3e3",
        "Referer": "https://www.cpppc.org/en/djyw.jhtml",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78",
        "X-Requested-With": "XMLHttpRequest",
        # "sec-ch-ua": ""Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"",
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": ""Windows""
    }

    r = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data=r.json()
    for p in data['data']['content']:
        res.append(p)

df = pd.json_normalize(res)
df.to_csv('fiestresults1.csv')
