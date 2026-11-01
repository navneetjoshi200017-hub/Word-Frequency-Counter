PUNCTUATIONS = ",/.<>?:;\"\\'|!@#$%^&*()[]{}_"                           


def clean_word(word):
    """Cleans the word of any extra whitespaces 
       and unwanted punctuations and turns everything into lower case.
    """
    return word.strip().strip(PUNCTUATIONS).lower()

def get_stop_words():
    """Creates a set of words that are to be ignored if user agrees
       and asks the user for custom words to ignore
       then returns the set
    """
    stop_words = {
    "the", "a", "an", "and", "or", "but",
    "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are",
    "was", "were", "be", "been", "being",
    "it", "this", "that", "these", "those",
    "i", "you", "he", "she", "we", "they"
    }
    while True:   
        custom_word = input("Enter word to ignore\n(Press Enter to skip): ")
        custom_word = clean_word(custom_word)
        if custom_word:
            stop_words.add(custom_word)
        else:
            break

    return stop_words