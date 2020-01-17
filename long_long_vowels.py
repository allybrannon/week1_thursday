
# this isn't working!?!?
#sentence = input("Enter your sentence: ")

sentence = ("hello").lower()
new_string = ""

for index in range(len(sentence)):
    add = ""
    if sentence[index] == "a":
        add = "aaaaa"
    elif sentence[index] == "e":
        add = "eeeee"   
    elif sentence[index] == "i":
        add = "iiiii"
    elif sentence[index] == "o":
        add = "ooooo"
    elif sentence[index] == "u":
        add = "uuuuu"
    else:
        add = sentence[index]

    new_string += add

print(new_string)
    