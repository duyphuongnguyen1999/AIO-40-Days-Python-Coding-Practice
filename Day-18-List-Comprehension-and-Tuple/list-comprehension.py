# List Comprehension
def main():
    stop_words=["I", "love", "and", "to"]
    input="I love AI and listen to music"
    # Remove stop words
    input_split=input.split(" ")
    result=[word for word in input_split
            if word not in stop_words]
    print(result)
if __name__=="__main__":
    main()