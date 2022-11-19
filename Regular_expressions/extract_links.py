import re

pattern = r"(w{3}\.[a-zA-Z0-9]+([\-a-zA-Z0-9]+)*(\.[a-z]+)+)"
inp_text = input()
#print(inp_text)
while inp_text:
    valid_url = re.search(pattern, inp_text)
    #print(valid_url)
    if valid_url:
        url = valid_url.group()
        print(url)
    inp_text = input()
