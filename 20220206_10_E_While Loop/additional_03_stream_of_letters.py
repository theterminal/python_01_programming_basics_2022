# 20220206 - Python - While Loop
# Additional 03 - Stream of Letters - judge: https://judge.softuni.org/Contests/Practice/Index/1684#2


# user's input
letter_entered = input()                            # ASCII from 65 to 90 & from 97 to 122


# additional elements
word, word_print = '', ''
count_c = count_o = count_n = 0


# result
while letter_entered != "End":

    if letter_entered == "c" and count_c == 0:
        count_c = 1
    elif letter_entered == "o" and count_o == 0:
        count_o = 1
    elif letter_entered == "n" and count_n == 0:
        count_n = 1
    else:
        if 65 <= ord(letter_entered) <= 90 or 97 <= ord(letter_entered) <= 122:
            word += letter_entered

    if (count_c + count_o + count_n) == 3:
        word = word + " "
        count_c = count_o = count_n = 0
        word_print = word

    letter_entered = input()

print(word_print)
