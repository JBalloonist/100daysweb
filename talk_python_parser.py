# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from bs4 import BeautifulSoup

# +
with open('Python for decision makers and business leaders.html', 'r') as out:
    html = out.read()

soup = BeautifulSoup(html)

# + jupyter={"outputs_hidden": true}
tasks = {}
for i in soup.find_all('div', class_='outline'):
    for hdr in i.find_all('a', class_="start-player chapter-link"):
        print(hdr.get_text())
    for sub in i.find_all('div', class_="lecture-title-column"):
        print(sub.get_text())

# + jupyter={"outputs_hidden": true}
product = soup.find_all('div', class_='outline')
all_text = [hdr for product.find_all('div', class_='chapter-title')]

# -

stuff = [{hdr.get_text().strip("\n").strip(): 
         []
         for hdr in all_text.find_all('div', class_="chapter-title")} for all_text in product]

stuff

for n,i in enumerate(soup.find_all('tbody')):
    print(n)
    print(type(i))
    print(i.attrs)
    print(i)
#     print(i.get_text())


