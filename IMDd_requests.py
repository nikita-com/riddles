import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.riddles.com/riddle-of-the-day')
web_page = response.text

riddles2 = []
Riddle = []
Answer = []

soup = BeautifulSoup(web_page, "html.parser")
riddles = soup.find_all(name='div', class_="panel-body lead")

for riddle in riddles:
    riddles2 = riddle.getText().replace("\n", "").replace("\t", "")
    if riddles2.find("Riddle:") == -1:
        continue
    Riddle.append(riddles2[riddles2.find("Riddle:")+7: riddles2.find("Answer:")])
    Answer.append(riddles2[riddles2.find("Answer:Answer:") + 14: riddles2.find("Please Share!")])

while len(Riddle) != 0:
    print(Riddle[0])
    answer = input(':')
    if answer == Answer[0]:
        print('True')
    else:
        print(Answer[0])
    print('-----------')
    Answer.pop(0)
    Riddle.pop(0)

print(len(Riddle))
print(len(Answer))

