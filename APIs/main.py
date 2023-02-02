import requests
import json
def data_ids(threshold):
    req_results = requests.get("https://jsonmock.hackerrank.com/api/article_users?page=1")
    whole_json = req_results.json()
    tot_pages = whole_json['total_pages']
    page = 1
    res = []
    while page <= tot_pages:
        req_results = requests.get('https://jsonmock.hackerrank.com/api/article_users?page'+str(page))
        print("ENTERING PAGE ", page)
        whole_json = req_results.json()
        # print(whole_json)
        for i in whole_json['data']:
            if i['submission_count'] > threshold:
                print(i['username'])
                res.append(i['username'])
        page += 1
    return res
res = data_ids(10)
print(res)