from textblob import TextBlob

correct_me = input("Enter a sentence: ")
a = TextBlob(correct_me)

print(a.correct())

