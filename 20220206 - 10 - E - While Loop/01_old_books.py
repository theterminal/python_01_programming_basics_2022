# 20220205 - Python Code
# Old Books

# user input
book_searched_for = input()

# calculations & results
counter_books = 0

while True:
    book = input()

    if book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {counter_books} books.")
        break
    else:
        counter_books += 1

        if book == book_searched_for:
            print(f"You checked {counter_books - 1} books and found it.")
            break

# --------------------another way ----------------------------

# # user input
# book_searched = input()
# book_in_library = input()
#
# # calculations & results
# n = 0
#
# while book_in_library != "No More Books":
#     if book_searched == book_in_library:
#         print(f"You checked {n} books and found it.")
#         quit()
#     n += 1
#     book_in_library = input()
#
# print("The book you search is not here!")
# print(f"You checked {n} books.")
