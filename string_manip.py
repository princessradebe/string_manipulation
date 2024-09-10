# String manipulation

sentence = "money!is!the!root!of!evil"
# rewriting the string in reverse
reverse_sentence = sentence[:: -1]
# rewriting the string capital letters
upper_sentence = (sentence.upper()) 
# replacing ! with empty string in the sentence
new_sentence = sentence.replace("!", " ")

print(sentence)
print(new_sentence)
print(reverse_sentence)
print(upper_sentence)
