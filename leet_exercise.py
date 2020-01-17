#leet exercise

paragraph = "This is the paragraph I want printed in leetspeek"
paragraph_upper = paragraph.upper()
leet_letters = "AEGIOST"
for letter in paragraph_upper:
    if letter in leet_letters:
        paragraph_upper = paragraph_upper.replace('A', str(4))
        paragraph_upper = paragraph_upper.replace('E', str(3))
        paragraph_upper = paragraph_upper.replace('G', str(6))
        paragraph_upper = paragraph_upper.replace('I', str(1))
        paragraph_upper = paragraph_upper.replace('O', str(0))
        paragraph_upper = paragraph_upper.replace('S', str(5))
        paragraph_upper = paragraph_upper.replace('T', str(7))
print(paragraph_upper)