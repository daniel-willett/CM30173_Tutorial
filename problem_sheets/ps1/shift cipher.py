inputText = "WKHPDJLFZRUGVDUHVTXHDPLVKRVVLIUDJH"
import string
alphabet = list(string.ascii_uppercase)
for shift in range(1,25):
    shiftedText = ""
    for letter in inputText:
        newVal = (ord(letter)+shift)%26
        shiftedText += chr(newVal+65)
    print(shiftedText)
