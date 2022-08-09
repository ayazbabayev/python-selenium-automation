# FIND THE FIRST UNIQUE LETTER IN GIVEN WORDS:
# AMAZON
# GOOGLE
# ANUNAKI

# REWRITE THE QUESTION. AND ALWAYS REFER IN YOUR CODE TO THOSE WORDS:
# IF ASKS CREATE A STRING, CREATE A STRING. IF RETURN. USE RETURN. IF PRINT. USE PRINT.


#   1:
# def unique(word: str):                  #define that the unique word is string
#     word = word.lower()
#     for letter in word:
#         if word.count(letter) == 1:     #eger word icinde count letter =1 ise
#             return letter
#
# print(unique('Amazon'))
# print(unique('Google'))
# print(unique('Anunaki'))

#   2:
def unique(word: str):
    word=word.lower()
    d={}
    print(d)

    for letter in word:
        print('Dict',d)
        if letter not in d:
            d[letter] = 1       # START ADDING IT TO DICTIONARY
        else:
            d[letter]+=1        # (after above) if the letter is in dictionary
                                # find it and add it into dictionary
    print('whole count', d)

    for k,v in d.items():       #k KEY & v VALUE in dictionary items
        if v ==1:
            return k

print(unique('akalaka'))
