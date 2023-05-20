def generateX(G,N,x):
    largeX = (G ** x) % N
    return largeX

def generateY(G,N,y):
    largeY = (G ** y) % N
    return largeY

def getKey(Y,x,N):
    K = (Y ** x) % N
    return K

def getKeyValidation(X,y,N):
    K = (X ** y) % N
    return K

def generateChunks(K):
    strNumber = str(K) 
    chunks = [strNumber[i:i+2] for i in range(0, len(strNumber))]
    intChunks = [int(i) for i in chunks]
    return intChunks

def generateViginereKey(chunk):
    charList = [chr(97+(i%26)) for i in chunk]
    return ''.join(charList)

