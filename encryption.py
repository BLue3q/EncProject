
def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    newText=""
    for i in text:
        if i =="":
            continue
        else:
            newText=newText+i
    return newText

def Diagraph(text):#function to group 2 elements of a string
    Diagraph=[]
    group=0
    for i in range(2,len(text),2):
        Diagraph.append(text[group:i])

        group=i
    Diagraph.append(text[group:])
    return Diagraph

def fillerLetter(text):#function to fill a letter in a string element if 2 letters in the same string matches
    k=len(text)
    if k%2 ==0:
        for i in range(0,k,2):
            if text[i]==text[i+1]:
                new_word=text[0:i+1]+str('x')+text[i+1:]
                break
            else:
                new_word=text
    else:
        for i in range(0,k-1,2):
            if text[i]==text[i+1]:
                new_word=text[0:i+1]+str('x')+text[i+1:]
                new_word=fillerLetter(new_word)
                break
            else:
                new_word=text
    return new_word

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateKeyTable(word,list1):# Function to generate the 5x5 key square matrix
    keyLetters=[]
    for i in word:
        if i not in keyLetters:
            keyLetters.append(i)

    compElements = []
    for i in keyLetters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
 
    return matrix

def search(mat, element):#find the row and column index of a given element in a 5x5 matrix
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j
            
    #if element isn't found return none
    return None,None
            
def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):#encrypt a pair of letters that are in the same row of the key matrix
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]
 
    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]
 
    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):#encrypt a pair of letters that are in the same column of the key matrix
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]
 
    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]
 
    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char2 = ''
    if e1r is None or e1c is None or e2r is None or e2c is None:
        return ' b ',' b '
    
    char1 = matr[e1r][e2c]
    char2 = matr[e2r][e1c]

    return char1, char2

def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0,len(plainList)):
        c1=0
        c2=0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x==ele2_x:
            c1,c2=encrypt_RowRule(Matrix,ele1_x,ele1_y,ele2_x,ele2_y)

        elif ele1_y==ele2_y:
            c1,c2=encrypt_ColumnRule(Matrix,ele1_x,ele1_y,ele2_x,ele2_y)
        else:
            c1,c2=encrypt_RectangleRule(Matrix,ele1_x,ele1_y,ele2_x,ele2_y)

        Cipher=c1+c2
        CipherText.append(Cipher)
    return CipherText

textplain=input("enter the text you want to encrypt it:")

textplain=toLowerCase(textplain)
textplain=removeSpaces(textplain)

plainTextList=Diagraph(fillerLetter(textplain))

if len(plainTextList[-1])!=2:
    plainTextList[-1]=plainTextList[-1]+'z'

key="Moouussaa"
print("key text",key)
key=toLowerCase(key)
Matrix=generateKeyTable(key,list1)

print("Plain Text:", textplain)
CipherList = encryptByPlayfairCipher(Matrix, plainTextList)

CipherText=""
for i in CipherList:
    CipherText += i

print("CipherText:", CipherText)

print (key)

for i in range(5):
    row = ""
    for j in range(5):
        row += Matrix[i][j] + " "
    print(row.strip())
    