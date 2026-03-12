val = "Hello my name is Inigo Montoya"
print(val[0:5])
print(val[6:13])
print(val[::2])
print(val[3:18:2])

sentence = input("Enter sentence: ")
vowels = "aeiou"
translated_sentence = ""
for i in sentence.lower():
    translated_sentence += i
    if i in vowels:
        translated_sentence += "b" + i
        
print(translated_sentence)


