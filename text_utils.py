PUNCTUATIONS = ",/.<>?:;\"\\'|!@#$%^&*()[]{}_"                           


def clean_word(word):
    return word.strip().strip(PUNCTUATIONS).lower()

def get_stop_words():
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