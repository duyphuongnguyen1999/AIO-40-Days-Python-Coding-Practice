# String manipulation using list
def main():
    corpus = ["Tôi thích Toán", "Tôi thích AI", "Tôi thích âm nhạc"]
    # Create a vocabulary
    vocabulary = []
    for doc in corpus:
        for word in doc.split(" "):
            if word not in vocabulary:
                vocabulary.append(word)
    print(vocabulary)
    # Bag-of-Words
    given_str = "Tôi thích AI thích Toán"
    given_str_tokenized = given_str.split(" ")
    vector = [0 for _ in range(len(vocabulary))]
    for word in given_str_tokenized:
        if word in vocabulary:
            idx = vocabulary.index(word)
            vector[idx] += 1
    print(vector)


if __name__ == "__main__":
    main()
