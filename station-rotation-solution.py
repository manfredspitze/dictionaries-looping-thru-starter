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



# Station 4
