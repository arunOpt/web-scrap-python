from bs4 import BeautifulSoup
import requests
import time

print("search something?")
searchVal=input(">")
print(f"Search: {searchVal}")
def searchSomething():
    content=requests.get("https://stackoverflow.com/questions/71418546/beautiful-soup-not-working-on-this-website").text
    soup=BeautifulSoup(content, "lxml")
    # print(soup.prettify())
    search=soup.find_all("div", class_="s-prose js-post-body")
    more_info=soup.a['href']
    print(more_info)
    for index,tag in enumerate(search):
        question=tag.find("p").text
        with open(f"results/{index}.txt", "w") as f:
             f.write(f'''{question.strip()}\n''')
        print("File Saved")
        print(f'''
        {question}
        ''')
        if "JavaScript." in question:
            print(f"{question.strip()}")
        print("************************************ ")
    # print(search)
if __name__== "__main__":
    while True:
        searchSomething()
        time_wait = 1
        print(f"waiting {1} minutes...")
        time.sleep(time_wait*60)