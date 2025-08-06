from collections import Counter


def calculationChar():
    file_name = input("Please enter the path to the .txt file: ")

    try:
        with open(file_name, "r", encoding="UTF-8") as file:
            content = file.read()

            if content:
                print("There is information in the txt file.")
            else:
                print("There is no information in the txt file.")
                return  # Exit early if file is empty

    except FileNotFoundError:
        print("❌ File not found. Please check the path and try again.")
        return

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return

    # Count characters
    numberChar = len(content)
    print(f"The number of characters in the txt file is: {numberChar}")

    # Count words
    numberWords = content.split()
    print(f"The number of words in the txt file is: {len(numberWords)}")

    # Count word frequencies
    word_count = Counter(numberWords)

    # Most common word
    most_common_word, frequency = word_count.most_common(1)[0]
    print(
        f"The most used word is '{most_common_word}' (used {frequency} times).")

    # Print words used more than once
    print("Words used more than once:")
    for word, count in word_count.items():
        if count > 1:
            print(f"{word}: {count}")

    # Count sentences based on punctuation
    numberPhrase = sum(content.count(punct) for punct in [".", ",", "?", "!"])
    print(f"The number of phrases in the txt file is: {numberPhrase}")


calculationChar()
