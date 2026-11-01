import text_utils as t
from word_counter import count_words
from report import display_report


def main():
    # file_path = "Test.txt"
    file_path = input("Enter file path: ")        
    print("===Text Frequency Counter===")

    stop_flag = input("Want to ignore some common occuring words(y/n): ")

    if t.clean_word(stop_flag) == "y":
        stop_words = t.get_stop_words()
    else:
        stop_words = {}

    

    try:

        unique_words,total_words = count_words(file_path,stop_words)

    except FileNotFoundError:
        print("\nFile Does Not Exist!!")

    else:
        print("\nFile read successfully!")

        if not unique_words:
            display_report(unique_words,total_words,0)
            return

        while True:
            try:
                limit = int(input("\nEnter the number of top words to display: "))

                if limit <= 0:
                    print("Enter a number greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid Input. Enter a whole number.")
        display_report(unique_words,total_words,limit)


if __name__ == "__main__":
    main()
