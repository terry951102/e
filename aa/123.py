from bs4 import BeautifulSoup
import requests
import json
result =[]

n = int(input("你要爬幾頁？請輸入："))

def crawler(url):
    global result
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    elems = soup.findall(class="r-ent")


    for elem in elems:
        if elem.find("a") == None:
            continue
        result.append({
            "title":elem.find(class = "title").getText().strip(),
            "url":"https://www.ptt.cc/" +str(elem.find("a")["href"]).strip(),
            "author":elem.find(class ="author").getText().strip(),
        })
    prev_url = soup.findall(class ="btn wide")[1]['href']
    return "https://www.ptt.cc/" + str(prev_url)



crawler("https://www.ptt.cc/bbs/Baseball/index864.html%22)
i = 1
url = "https://www.ptt.cc/bbs/Baseball/index864.html"

while i <= n:

    url = crawler(url)
    result.append({
        "--------------" : "-----------------"
    })
    i += 1


with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, sort_keys=True, ensure_ascii=False)
