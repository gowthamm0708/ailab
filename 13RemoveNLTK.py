import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    stop = set(stopwords.words('english'))
    
    for line in f1:
        words = line.split()
        for word in words:
            if word.lower() not in stop:
                f2.write(word + " ")
