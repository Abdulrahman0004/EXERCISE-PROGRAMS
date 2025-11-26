import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Terminal is now available to all users, free of charge! (X, Colab Notebook). The new Colab AI experience is now available to all users."

print("Word Tokenization :")
word = word_tokenize(text)
for num, words in enumerate(word):
  print(num, words)

print("\nSentence Tokenization :")
sentence = sent_tokenize(text)
for num, sentences in enumerate(sentence):
  print(num, sentences)