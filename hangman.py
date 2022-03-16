import random

def get_secret_word(wordfile="/usr/share/dict/words"):
    good_words = []
    with open(wordfile) as f:
        for w in f:
            w = w.strip()
            if w[0].isupper():
                continue
            if len(w) < 4 or len(w) >= 10:
                continue
            if not w.isalpha():
                continue
            good_words.append(w)
    return random.choice(good_words)

def hangman_mask(secret_words, guesses):
    result_string = []
    for i in secret_words:
        if i in guesses:
            result_string.append(i)
        else:
            result_string.append("-")
    return "".join(result_string)

def hangman_create_status(secret_words, guesses, remaining_turn):
    masked_word = hangman_mask(secret_words, guesses)
    guessed = " ".join(guesses)
    return f"""Word:{masked_word}
    Guesses:{guessed}
    Remaining_turns:{remaining_turn}"""       