import requests

x = requests.get('https://webscraper.io/test-sites')

res = x.text

file = open("copy.txt", "w")
count = 0
for line in res:
    for character in line:
        if character == '<':
            count = 1
            continue
        elif character == '>':
            count = 0
            continue
        elif count == 1:
            continue
        else:
            file.write(character)

file.close()
print ('Hello')
file = open("copy.txt", "r")
lines = file.readlines()
file.close()
lines = filter(lambda x: not x.isspace(), lines)
file = open("copy.txt", "w")
file.writelines(lines)
file.close()