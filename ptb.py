import markovify

# Get raw text as string.
with open("corpus.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

# Print five randomly-generated sentences
for i in range(20):
    sentence = text_model.make_sentence()
    if sentence != None:
        print(sentence)

