import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
print(r.text)

vowels= {"a", "e", "i", "o", "u"}
letters= [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
message= ""
counter=0
lines=r.text.split('\r')


for line in lines:
    counter=0
    for i in line:
        if i in vowels:
            counter+= 1
    message = message + letters[counter]

print(message)