"""

This is the programming part of your midterm exam.  It consists of a programming assignment that you will complete using the Python IDLE IDE. 
This part of your midterm exam is worth 50 points, and will be graded - as all programming assignments are graded - based on our Introductory Standards for Acceptable Software Development.  You may use your course materials.
Please name the .py files for your program as LNameFnameM#_Midterm (using your name). For example: GarvinFredM08_Midterm.py (Python will automatically append the extensions).  You'll submit this file for grading.
Your assignment is to write a program that inputs a sentence from the keyboard, word by word, into a list.  

The program should output the following.

1. The complete sentence, with only the first letter of the first word capitalized (if it wasn't already), spaces between each word, and a period at the end.

2. The count of the number of words in the sentence.

Hint: end input on a blank line or on input of the word "done".

For instance, if the input is: 
the

cat

ran 

home

quickly

Your program should output:

The cat ran home quickly.
There are 5 words in the sentence.

"""

def main():
    words = []
    print("Please type in a sentence.")
    print("Type 'complete' or press Enter on a blank line to finish.")

    while True:
        word: str = input("Enter a word: ")

        if word == "" or word.lower() == "done":
            break

        words.append(word)

    # this will check to see if any words were entered during initial input request
    if len(words) == 0:
        print("No words were entered.")
        return

    full_sentence: str = " ".join(words)
    formatted_sentence: str = full_sentence.capitalize() + "."

    # final results
    print("Output:")
    print(formatted_sentence)
    print(f"There are {len(words)} words in the sentence.")

if __name__ == "__main__":
    main()
