import string
def word_frequency(paragraph):
    paragraph = paragraph.lower()
    # Remove punctuation using str.translate and string.punctuation
    paragraph = paragraph.translate(str.maketrans('','',string.punctuation))
    words = paragraph.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count

paragraph_input = input("Enter a paragraph of text: ")
word_freq_dict = word_frequency(paragraph_input)
print("\nWord Frequency:")
for word, count in word_freq_dict.items():
    print(f"{word}: {count}")