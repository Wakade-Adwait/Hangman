import random
import hangman_words
# from hangman_art import stages

#from hangman_words import word_lists

lives=6

choosen_word=random.choice(hangman_words.word_list)
# print(choosen_word)

placeholder=""
word_length=len(choosen_word)
for position in range(word_length):
    placeholder +="_"
    word_length=len(choosen_word)
print("word to guess:-"+ placeholder)

game_over=False
correct_letters=[]

while not game_over:
    print(f" {lives} left")


    guess=input("Guess a letter:-").lower()
    if guess in correct_letters:
        print(f"You've already guess {guess}")

    display=""

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display +=letter
        else:
            display+="_"

    print("Word to guess :- " + display)



    if guess not in choosen_word:
        lives -=1
        print(f"You've guessed {guess} a wrong value you lose a life.")
        if lives==0:
            game_over=True

            print("******* YOU LOSE  **********")
            print(f"It was {choosen_word}")

    if"_"not in display:
        game_over=True
        print("************* YOU WON ***************")
        # print(stages[lives])
