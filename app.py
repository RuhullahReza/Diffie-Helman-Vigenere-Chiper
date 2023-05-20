from utils.keyGenerator import *
from utils.largePrime import generateTwoPrimes, nBitRandom
from utils.vigenere import *
from utils.uiClass import * 

inputN = InputBox('N',300,50,100,500)
inputG = InputBox('G',300,100,100,500)
inputx = InputBox('a',850,50,100,500)
inputy = InputBox('b',850,100,100,500)

inputVigenereKey = InputBox('Vigenere Key',570,345,100,500)

inputText = InputBox('Text',570,435,100,500)
outputText = InputBox('Result',570,530,100,500)

inputLargeX = InputBox('X',300,200,100,500)
inputLargeY = InputBox('Y',300,250,100,500)

inputK1 = InputBox('K1',850,200,100,500)
inputK2 = InputBox('K2',850,250,100,500)


def generatePrime():
    prime = generateTwoPrimes(128)
    N = prime[0]
    G = prime[1]
    inputN.clearValue()
    inputG.clearValue()
    inputN.setValue(N)
    inputG.setValue(G)

def generateAB():
    x = nBitRandom(8)
    y = nBitRandom(8)  
    inputx.clearValue()
    inputy.clearValue()
    inputx.setValue(x)
    inputy.setValue(y)   

def outputLargeXY():    
    N = int(inputN.getEntry())
    G = int(inputG.getEntry())
    x = int(inputx.getEntry())
    y = int(inputy.getEntry())
    largeY = generateY(G,N,y)
    largeX = generateX(G,N,x)
    inputLargeX.clearValue()
    inputLargeY.clearValue()
    inputLargeX.setValue(largeX)
    inputLargeY.setValue(largeY)

def generateK():
    N = int(inputN.getEntry())
    G = int(inputG.getEntry())
    x = int(inputx.getEntry())
    y = int(inputy.getEntry())
    largeY = generateY(G,N,y)
    largeX = generateX(G,N,x)
    K1 = getKey(largeY,x,N)
    K2 = getKeyValidation(largeX,y,N)
    inputK1.clearValue()
    inputK2.clearValue()
    inputK1.setValue(K1)
    inputK2.setValue(K2)

def getVigenereKey():
    k1 = int(inputK1.getEntry())
    chunk = generateChunks(k1)
    vigenereKey = generateViginereKey(chunk)
    inputVigenereKey.clearValue()
    inputVigenereKey.setValue(vigenereKey)

def getEncrypted():
    vigenereKey = inputVigenereKey.getEntry()
    plain = inputText.getEntry().lower().replace(" ","")
    key = generateKey(plain,vigenereKey)
    chiper = encrypt(plain,key)
    outputText.clearValue()
    outputText.setValue(chiper)

def getDecrypted():
    vigenereKey = inputVigenereKey.getEntry()
    chiper = inputText.getEntry().lower().replace(" ","")
    key = generateKey(chiper,vigenereKey)
    plain = decrypt(chiper,key)
    outputText.clearValue()
    outputText.setValue(plain)

ProcessButton('Generate Random Prime',generatePrime,290,150)
ProcessButton('Generate a and b',generateAB,850,150)
ProcessButton('Get X and Y',outputLargeXY,293,300)
ProcessButton('Get K',generateK,850,300)
ProcessButton('Get Vigenere Key',getVigenereKey,570,400)
ProcessButton('Encrypt',getEncrypted,520,490)
ProcessButton('Decrypt',getDecrypted,620,490)

root.mainloop()
