"""Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical 
order. Then working out the alphabetical value for each name, multiply this value
 by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3+15+12+9+14 = 53, is the 938th name in the list. So, COLIN would obtain a 
score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""
def get_alphabetical_score(name):
    """Returns the alphabetical score (abby would be 1+2+2+25)"""
    letters="-abcdefghijklmnopqrstuvwxyz"
    total_score = 0
    for letter in name:
        letter_score = letters.index(letter)
        total_score += letter_score
    return total_score

with open("vars022.txt", "r") as file:
    names_str = file.read()

names = names_str.lower().replace('"','').split(",")
names.sort()

total_score = 0
position = 1
for name in names:
    total_score+= get_alphabetical_score(name) * position
    position += 1

print(total_score)