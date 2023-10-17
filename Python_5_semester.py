import sys
import string
from collections import Counter
""" 
Упражнение 3. Напишите программу, которая вычисляет статистику содержимого файла: 
наиболее часто встречающееся слово, количество слов, и количество символов. 
Имя файла задается из командной строки.
"""

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().lower()
    except OSError:#FileNotFoundError:
        raise Exception("File error.")
    
    if not data:
        data = ""
    
    return data



def compute_statistics(data):
    
    character_count = len(data)  
    
    #                           !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~`
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    data = data.translate(translator)
    
    word_count = 0
    most_frequent_word = ""
    words = data.split()
    words = [word for word in words if len(word) > 1 and any(char.isalpha() for char in word)]
    if words:  
        word_count = len(words)

        word_frequency = Counter(words)
        most_frequent_word = word_frequency.most_common(1)[0][0]

    return {"most_frequent_word": most_frequent_word, "word_count": word_count, "character_count": character_count}



def main():
    if len(sys.argv) < 2:
        print("Usage: python lab3.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    
    try:
        data = read_file(filename)
    
        result = compute_statistics(data)
        
        print("Most frequent word:", result["most_frequent_word"])
        print("Number of words:", result["word_count"])
        print("Number of characters:", result["character_count"])

        with open("statistics.txt", "w") as output_file:
            output_file.write(f"Most frequent word: {result['most_frequent_word']}\n")
            output_file.write(f"Number of words: {result['word_count']}\n")
            output_file.write(f"Number of characters: {result['character_count']}\n")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()