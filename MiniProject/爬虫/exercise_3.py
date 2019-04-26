import requests
from bs4 import BeautifulSoup

format = "https://book.douban.com/subject/{}/"
headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Referer': 'https://book.douban.com/',
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
}

def get_comments(book_url):
    session = requests.Session()
    session.headers = headers
    page = 1
    l = []
    while True:
        print("Now on page:", page)
        response = requests.get(book_url+"comments/hot?p="+str(page))
        soup = BeautifulSoup(response.text, features="lxml")
        comments = soup.find_all(class_="comment-item")
        if len(comments) == 0:
            break
        for comment in comments:
            if "还没人写过短评呢" in comment.get_text():
                return []
            l.append(comment.get_text())
        page += 1
    return l

def welcome():
    print("Welcome to my web crawler~")
    print("** -- ** Start Now!")

def eastereggs():
    print("--: 1999.05.12 is author's birthday!")
    print("Thanks for your willingness to use my script.")

if __name__ == "__main__":
    welcome()
    num = input("Please input the book num you want: ")
    if num == "19990512":
        eastereggs()
    book_url = format.format(num)
    comments = get_comments(book_url)
    with open(num+"comments.txt", "w", encoding="utf-8") as f:
        for comment in comments:
            f.write(comment)
    print("Comments Count is:", len(comments))
