

import hangman

def test_secret_word_no_proper_noun():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("apple\n")
        f.write("Grape\n")
        f.write("Watermelon\n")
    for _ in range(10):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "apple"

def test_secret_word_correct_length():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("ape\n")
        f.write("table\n")
        f.write("mattresses\n")
    for _ in range(20):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "table"

def test_secret_word_no_punctuation():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("spain's\n")
        f.write("america's\n")
        f.write("india\n")
    for _ in range(20):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "india"

def test_mask_word_a_letter():
    secret_word = "aligator"
    guesses = ["g"]
    ret = hangman.hangman_mask(secret_word, guesses)
    assert ret == "---g----"