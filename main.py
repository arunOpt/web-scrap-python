from bs4 import BeautifulSoup
with open("home.html", "r") as html_file:
    content=html_file.read()
    soup=BeautifulSoup(content, "lxml")
    html_tags=soup.find_all("h5")
    for tag in html_tags:
        print(tag.text)
    html_card=soup.find_all("div", class_="card")
    for card in html_card:
        print(card.text)
