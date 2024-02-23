inputText = "EMRMESEBREITCRUACYSINIHIANLTOSSEYSAEACRUEWSHTESEKANKTIL"
import string
alphabet = list(string.ascii_uppercase)
decryptKey = [3,4,0,2,1]
plainText = ""
for i in range(0,11):
    cipherBlock = inputText[5*i:5*i+5] #Blocks of 5 because that appears to be correct
    #[0|1|2|3|4]
    plainBlock=list("ABCDE")
    for j in range(0,5):
        character = cipherBlock[j]
        realPos = decryptKey[j]
        plainBlock[realPos] = character
    plainText+="".join(plainBlock)
        

print(plainText) 
