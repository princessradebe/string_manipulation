# String manipulation

sentence = "money!is!the!root!of!evil"
reverse_sentence = sentence[:: -1] #rewriting the string in reverse
upper_sentence = (sentence.upper()) #rewriting the string capital letters
new_sentence = sentence.replace("!", " ") #replacing ! with empty string in the sentence

print (sentence)
print (new_sentence)
print (reverse_sentence)
print (upper_sentence)
