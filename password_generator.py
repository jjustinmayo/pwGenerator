# import a module that generates random characters whenever "random." is used 
import random

# Create variables for each random character 
# the "random.randint()" method returns an integer from the specified range. The range used for  each variable is based on unicode (ASCII) values
# "chr()" TO STUDY
# "str()" TO STUDY
lowercaseLetter1 = chr(random.randint(97,122))   
lowercaseLetter2 = chr(random.randint(97,122))  
uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))
digit1 = str(random.randint(0,9))                 
digit2 = str(random.randint(0,9))
punctuation1 = chr(random.randint(33,47))
punctuation2 = chr(random.randint(33,47))


def pwGenerator():
    # create a new list which lists the objects as strings in order
    pwList = [lowercaseLetter1, lowercaseLetter2, uppercaseLetter1, uppercaseLetter2, digit1, digit2, punctuation1, punctuation2]
    # using the random module, use .shuffle to randomize the order of each object in the list created
    random.shuffle(pwList)
    # to STUDY
    randomPw = "".join(map(str,pwList))
    print(randomPw)
    
pwGenerator()

