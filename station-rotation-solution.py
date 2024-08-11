# Looping Through Python Dictionaries

# Station 1
# Create a dictionary with countries as keys and capitals as values
countries_capitals = {
    "United States": "Washington D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasilia",
    "Australia": "Canberra"
}

# Iterate through the dictionary and print country and capital using f-strings
for country, capital in countries_capitals.items():
    print(f"The capital of {country} is {capital}.")


# Station 2
# Create a dictionary with author and book title pairs
books = {
    "J.K. Rowling": "Harry Potter and the Sorcerer's Stone",
    "Stephen King": "The Shining",
    "Jane Austen": "Pride and Prejudice",
    "Agatha Christie": "Murder on the Orient Express"
}

# Get the author to search for from the user
author_to_find = input("Enter the author's name: ")

# Check if the author is in the dictionary
if author_to_find in books:
    print(f"{author_to_find} is in the dictionary. Their book is: {books[author_to_find]}")
else:
    print(f"{author_to_find} is not in the dictionary.")



# Station 3
# Create a dictionary with student names and exam scores
student_scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "David": 95,
    "Emily": 88
}

# Print each student's name and score
for student, score in student_scores.items():
    print(f"{student} got a score of {score}.")

# Calculate the class average
total_scores = sum(student_scores.values())
num_students = len(student_scores)
average_score = total_scores / num_students

# Print the class average
print(f"The class average is {average_score:.2f}.")



# Station 4
