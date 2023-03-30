import spacy
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
 similarity = nlp(sentence).similarity(model_sentence)
 print(sentence + " - ", similarity)

 # Comparing the results from en_core_web_md and en_core_web_sm":
 # the similarities calculated by the larger model (en_core_web_md) is higher, 
 # as it has been trained on a larger corpus of text and therefore has 
 # more information about the relationships between words. 
 # The smaller model (en_core_web_sm) should be faster and may be more suitable for applications 
 # that require real-time processing.
