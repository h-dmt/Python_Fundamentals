import re

dates = input()
# ['13/Jul/1928', '10-Nov-1934', '25.Dec.1937', '01/Jan-1951', '23/sept/1973', '1/Feb/2016']
date_pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"

matches = re.findall(date_pattern, dates)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
