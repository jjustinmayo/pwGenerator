import random

lowercaseLetter1 = chr(random.randint(97,122))   
lowercaseLetter2 = chr(random.randint(97,122))  
uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
digit1 = str(random.randint(0,9))                 
digit2 = str(random.randint(0,9))
punctuation1 = chr(random.randint(33,47))
punctuation2 = chr(random.randint(33,47))


def nothanksGoogle():
    pwList = [lowercaseLetter1, lowercaseLetter2, uppercaseLetter1, uppercaseLetter2, digit1, digit2, punctuation1, punctuation2]
    random.shuffle(pwList)
    randomPw = "".join(map(str,pwList))
    print(randomPw)
    
nothanksGoogle()

