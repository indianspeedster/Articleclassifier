import fasttext
model = fasttext.train_supervised(input="data.txt")
model.save_model("article classifier.bin")
print((model.predict('The first step of this tutorial is')))