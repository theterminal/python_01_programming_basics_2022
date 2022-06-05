# 20220219 - Python Code - Function test

# defining a function
def say_hello():
    print(13 * "hello ")
    for i in range(1, 10):
        print(i, end=" ")


say_hello()

# ------------- another example ------------------

import hashlib
import binascii

sha256hash = hashlib.sha256(b'hello').digest()
print("\n\nSHA-256('hello') = ", binascii.hexlify(sha256hash))
