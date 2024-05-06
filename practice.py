from textblob import TextBlob



text1 = "I am very happy with my purchase"
text2 = "The quality is of this item is reasonable"

#TextBlob analyzes and outputs two parameters: polarity and subjectivity
#Using TextBlob to check both parameters of each sentence

p1 = TextBlob(text1).sentiment.polarity
p2 = TextBlob(text2).sentiment.polarity

s1 = TextBlob(text1).sentiment.subjectivity
s2 = TextBlob(text2).sentiment.subjectivity


print("Polarity of text 1: ", p1)
print("Polarity of text 2: ", p2)

print("Subjectivity of text 2: ", s1)
print("Subjectivity of text 2 is: ", s2)

