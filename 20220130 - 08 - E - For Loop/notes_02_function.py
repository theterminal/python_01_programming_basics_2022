# 20220130 - Python Code
# Notes - 02 - Functions

def sayhello():
    for i in range(1, 10001):
        print(f"{i} - Hello!")
        if i == 5000:
            print("Yeah " * 1000)


sayhello()
