import pandas  # Import the pandas library for data manipulation

# Read the CSV file containing NATO phonetic alphabet data into a DataFrame
nato_alphabets = pandas.read_csv("E:/Courses/Python/PyCharm Projects/NATO Alphabet Converter/nato_phonetic_alphabet.csv")

# Convert the DataFrame to ensure it is stored correctly (though reading CSV already creates a DataFrame)
nato_alphabets = pandas.DataFrame(nato_alphabets)

# Create a dictionary comprehension that maps each letter to its corresponding NATO phonetic code
nato_alphabets_dictionary = {row.letter: row.code for (index, row) in nato_alphabets.iterrows()}


def generate_phonetics():
    # Get user input, convert the input word to uppercase letters, and store it as a list of characters
    user_word = list(input("\nEnter a Word: ").upper())

    # Method 2 (optional): You could also create the list using this method for clarity
    # user_word = [word for word in user_word]

    converted_word = []

    try:
        # Convert each letter in the user's word to its corresponding NATO phonetic code using list comprehension
        converted_word = [
            code
            for word in user_word
            for (letter, code) in nato_alphabets_dictionary.items()
            if nato_alphabets_dictionary[word] and letter == word # nato_alphabets_dictionary[word]: This checks whether
            # word (from user_word) exists in the dictionary and returns True if it does.
        ]

        #converted_word = [nato_alphabets_dictionary[letter] for letter in user_word]

    except KeyError:
        print("\nOnly Alphabets are allowed")
        generate_phonetics()

    else:
        # Print the converted word in NATO phonetic code format
        print(converted_word)


generate_phonetics()