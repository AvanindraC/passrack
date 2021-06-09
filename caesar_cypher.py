SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
MAX_KEY_SIZE = len(SYMBOLS)
def getKey():
    key = 0
    while True:
        key = 13
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
def getTranslatedMessage(mode,message , key):
    if mode [0] == 'd':
        key = -key
    translated = ''
            
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
                    
            translated += SYMBOLS[symbolIndex]
    return translated
text = ''
cce = getTranslatedMessage('e', text, 13)    

ccd = getTranslatedMessage('d', cce, 13)  
