import string
 
#read file
def read_file(filename):
    with open(filename,'r') as file:
        return file.read()

#clean text
def clean_text(text):
    text=text.lower()
    text=text.translate(str.maketrans('','',string.punctuation))
    return text

#split words
def get_words(text):
    return text.split()

#count sentences 
def count_sentences(text):
    sentences=text.replace('!','.').replace('?','.').split('.')
    sentences=[s for s in sentences if s.strip()!='']
    return len(sentences)

#ford frequency
def word_frequency(words):
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    
    return freq
    
# top 10 words
def top_10_words(freq):
    sorted_words=sorted(freq.items(),key=lambda x:x[1],reverse =True)
    return sorted_words[:10]

def analyze_text(filename):
    text = read_file(filename)
    
    cleaned = clean_text(text)
    words = get_words(cleaned)
    
    total_words = len(words)
    total_sentences = count_sentences(text)
    unique_words = len(set(words))
    
    freq = word_frequency(words)
    top_words = top_10_words(freq)
    
    print("\n--- Text Analysis ---")
    print("Total Words:", total_words)
    print("Total Sentences:", total_sentences)
    print("Unique Words:", unique_words)
    
    print("\nTop 10 Frequent Words:")
    for word, count in top_words:
        print(word, ":", count)


# Run program
if __name__ == "__main__":
    filename = input("Enter file name: ")
    
    try:
        analyze_text(filename)
    except FileNotFoundError:
        print("File not found. Please check the file name.")