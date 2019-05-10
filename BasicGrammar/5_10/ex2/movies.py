import requests
import re

format = "https://movie.douban.com/top250?start={}"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Referer': 'https://book.douban.com/',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
}

def get_movies(movie_url):
    session = requests.Session()
    session.headers = headers
    response = requests.get(movie_url)
    text = response.text.replace("\n", "")

    header = re.compile(r'<a href="https://movie.douban.com/subject(([\s\S])*?)</a>')
    title = re.compile(r'<span.*?</span>')
    content = re.compile(r'<p class(([\s\S])*?)</p>')
    year = re.compile(r'\d')
    detail = re.compile(r'<br(([\s\S]*?))</p>')

    contents = content.findall(text)
    header_list = header.findall(text)

    for i, header in enumerate(header_list):
        if i % 2 == 1:
            titles = title.findall(header[0])
            if titles:
                print("----------")
                strs = [t.lstrip('<span class="title">').rstrip("</span>").lstrip('<span class="other">').replace("&nbsp;", "") for t in titles]
                print(" ".join(strs), end="")
            continue
        print()
        try:
            print_detail(contents[i][0])
        except:
            pass
    print()
    print_detail(contents[len(header_list)][0])

def print_detail(s):
    slice = [str for str in s.split("&nbsp;") if len(str) > 1]
    print(slice[0].lstrip('="">').strip().replace("\n", ""))
    for i, ss in enumerate(slice):
        if i == 1:
            print(ss.split("<br>")[0])
            print(ss.split("<br>")[1].strip())
        elif i != 0:
            print(ss)


if __name__ == "__main__":
    for i in range(10):
        get_movies(format.format(i*25))
