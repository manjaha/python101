from collections import Counter


def game_process(list_to_guess, used_letters, secret_word, cnt, attempts, guessed_word):
    while True:
        letter_to_guess = Counter(''.join(list_to_guess))
        for letter in used_letters:
            del letter_to_guess[letter]
        letter_to_guess = letter_to_guess.most_common(cnt)[-1][0]
        print(F"Is '{letter_to_guess}' in this word?")
        if letter_to_guess in secret_word:
            cnt += 1
            attempts += 1
            indices = [i for i, x in enumerate(secret_word)
                       if x == letter_to_guess]
            for i in indices:
                guessed_word[i] = letter_to_guess
                for word in list_to_guess:
                    list_to_guess = [x for x in list_to_guess if x[i] == letter_to_guess]
            if len(list_to_guess) == 1 or ''.join(guessed_word) == secret_word:
                print(f'Word to guess ({len(secret_word)} letters):',
                      list_to_guess[0])
                print(f'Word is guessed in {attempts} attempts')
                break
            else:
                print(f'Word to guess ({len(secret_word)} letters):',
                      ''.join(guessed_word),
                      f'[{len(list_to_guess)} potential word(s) left]')
            used_letters.append(letter_to_guess)
            continue
        elif letter_to_guess not in secret_word:
            cnt = 1
            attempts += 1
            used_letters.append(letter_to_guess)
            for word in list_to_guess:
                if letter_to_guess in word:
                    list_to_guess.remove(word)
            if len(list_to_guess) == 1:
                print(f'False!\nWord to guess ({len(secret_word)} letters):',
                      list_to_guess[0])
                print(f'Word is guessed in {attempts} attempts')
                break
            else:
                print('False! Please try again',
                      f'[{len(list_to_guess)} potential word(s) left]')
                continue


def main():
    words = {}
    list_to_guess = []
    used_letters = []
    cnt = 1
    attempts = 0
    #  1. generate list of words
    text = open('words.txt', 'r', encoding="utf-8").read().lower().split()
    for word in text:
        if word.isalpha():
            words[word] = len(word)
    #  2. get and validate secret_word
    while True:
        print(words.keys())
        secret_word = input('\nPlease enter some word from the list above: ')
        if secret_word not in words.keys():
            print(f"\n{secret_word} is out of range.\n")
            continue
        else:
            break
    #  3. generate list of potential words based on secret_word length
    for key, value in words.items():
        if value == len(secret_word):
            list_to_guess.append(key)
    #  4. print word to guess
    guessed_word = [" _ "]*len(secret_word)
    print(f'Word to guess ({len(secret_word)} letters):',
          ''.join(guessed_word),
          f'[{len(list_to_guess)} potential word(s) left]')
    #  5. start secret_word guessing
    game_process(list_to_guess, used_letters, secret_word, cnt, attempts, guessed_word)


if __name__ == '__main__':
    main()
