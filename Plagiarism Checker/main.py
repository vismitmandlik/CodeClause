import string

def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def check_plagiarism(text1, text2):
    cleaned_text1 = remove_punctuation(text1.lower())
    cleaned_text2 = remove_punctuation(text2.lower())
    
    words1 = set(cleaned_text1.split())
    words2 = set(cleaned_text2.split())
    
    common_words = words1.intersection(words2)
    
    plagiarism_score = len(common_words) / len(words1) * 100
    
    return plagiarism_score

# Example usage with user input
user_input1 = input("Enter text 1: ")
user_input2 = input("Enter text 2: ")

score = check_plagiarism(user_input1, user_input2)
print(f"Plagiarism score: {score}%")

# Example usage with file inputs
file1_path = input("Enter path to file 1: ")
file2_path = input("Enter path to file 2: ")

with open(file1_path, "r") as file1:
    text1 = file1.read()

with open(file2_path, "r") as file2:
    text2 = file2.read()

score = check_plagiarism(text1, text2)
print(f"Plagiarism score: {score}%")
