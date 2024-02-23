inputText = "AGBAPZTGELGPTIPMGHQCGAECHZFVCEXXGLYIGHEULTQATQHPUFEUYGZZEVGUYHGUYIPUYIGQUGYIPYEAYIGFNKTYYCEGLYIGFSQKZLEUMGUYPSEXIGCYIPYUQQUGSQKZLDCGPO"
import string
alphabet = list(string.ascii_uppercase)
counter = 0
cipherFreq = []
for character in alphabet:
    counter = inputText.count(character)
    if counter != 0:
        #print(character + ": " + str(counter))
        cipherFreq.append([character, counter])


from operator import itemgetter
cipherFreq=sorted(cipherFreq, key=itemgetter(1), reverse=True)
#print(cipherFreq)
commonCipherChars = [row[0] for row in cipherFreq]
#print(commonCipherChars)
mostFrequent = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

plainText = len(inputText)*['']

def find_indices_of_substring(full_string, sub_string):
    return [index for index in range(len(full_string)) if full_string.startswith(sub_string, index)]

for i in range(0,len(commonCipherChars)):
    char = commonCipherChars[i]
    indices = find_indices_of_substring(inputText,char)
    realChar = mostFrequent[i]
    for x in indices:
        plainText[x] = realChar

print(''.join(plainText))
