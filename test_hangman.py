

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

def test_mask_word_multiple_letters():
    secret_word = "aligator"
    guesses = ["a"]
    ret = hangman.hangman_mask(secret_word, guesses)
    assert ret == "a---a---"


def test_mask_word_mixed_letters():
    secret_word = "aligator"
    guesses = ["a", "g", "w"]
    ret = hangman.hangman_mask(secret_word, guesses)
    assert ret == "a--ga---"

def test_create_status_no_guesses():
    secret_word = "aligator"
    guesses = []
    remaining_turn = 8
    ret = hangman.hangman_create_status(secret_word, guesses, remaining_turn)
    assert ret == """Word:--------
    Guesses:
    Remaining_turns:8"""


def test_create_status_normal():
    secret_word = "aligator"
    guesses = ["a", "g", "h"]
    remaining_turns = 4
    ret = hangman.hangman_create_status(secret_word, guesses, remaining_turns)
    assert ret == """Word:a--ga---
    Guesses:a g h
    Remaining_turns:4"""        