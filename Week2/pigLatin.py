import re

def pig_latin(word):
    vowels = ['a','e','i','o','u']
    # consonents = []
    index=0
    if word[0].lower() in vowels:
        newWord=word+'way'
    else:
        index=re.search('[aeiou]',word).span()[0]
        if word[0].isupper():
            newWordTemp=word.lower()
            newWord2 = newWordTemp[index:] + newWordTemp[:index] +'ay'
            newWord =newWord2.capitalize()
        else:
            newWord = word[index:] + word[:index] +'ay'
    return newWord


def translate(sentence):
    return ' '.join([pig_latin(i) for i in sentence.split(' ')])




if __name__ == '__main__':
    #word = ['apple','paper','school','Apple','Barney']
    sentence = "Barney ate the apple"
    print(translate(sentence))


#print(' '.join([pig_latin(i) for i in sentence.split(' ')]))
