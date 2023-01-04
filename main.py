from bs4 import BeautifulSoup

with open('itgen.html') as file:
    contents = file.read()
# print(soup.title.text)
# print(soup.h1.string)
# print(soup.prettify())

soup = BeautifulSoup(contents, "html.parser")

heading = soup.find(name='h1', id='name')
# print(heading)

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

name = soup.select_one(selector='#name')
# print(name)

headings = soup.select(selector='.heading')
# print(headings)

text = soup.find_all(name='p')

for el in text:
    text2 = el.getText().replace("\n", "").replace("\t", "")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))

print(text2)

