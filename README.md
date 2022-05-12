# Python-SHA-256
An implementation of the SHA-256 hashing function written in Python to understand the basic principles and function of it.
The `hash.py` file contains the actual code, `example.py` is just example usage. Run `hash.textToSha256(message)` to use.

**What is Sha-256?**
Sha-256 is a cryptographic hash function. It was created in 2001 by the US National Security Agency, also known as the NSA. This hashing function is one-way, meaning that once you create a hash from a string, you can't create the string from the hash. Each hash is 64 characters long, and includes numbers and letters. 'sha' stands for 'Secure Hash Algorithm'. 

More information can be found on [Wikipedia](https://wikipedia.org/wiki/SHA-2).

**Sha-256 in Python (with hashlib)**
In python, there is a built-in library for handling hashing like this, called hashlib. A very simple hashing program can look like this:
```python
import hashlib

print(hashlib.sha256("Message here".encode('ASCII')).hexdigest())
```
This is very easy and fast, which made me wonder... what if I made my own sha256 program in Python _without_ using libraries like hashlib?

So I created this project. In total, it uses two external libraries, but only for printing to the console. The libraries it uses are:
 - `os`: for clearing the console between inputs
 - `time`: for logging the amount of time each operation took

**Explanation**
The repl has 12 functions, which are explained below.
- `lowestMultiple(multiple, greaterThan)` (line 1): Returns the lowest number that is a multiple of `multiple` but greater than `greater than`
- `splitIntoList(original, stringSize)` (line 7): Returns the string `original` split into an array of strings, each the length of `stringSize` (length of `original` must be divisible by `stringSize`)
- `xorAddBinary(binary)` (line 17): Takes a list of binary strings, `binary`, and adds them together with an 'exclusive or'. Each bit is only true if the value of each corresponding bit differs, so if one is `true` and the other is `false`
- `andAddBinary(binary)` (line 30): Takes a list of binary strings, `binary`, and adds them together with an `and`. Each bit is only true if the value of both the corresponding input bits is true.
- `notBinary(binary)` (line 42): Takes one binary string, `binary`, and inverts it. The `1`s become `0`s, and the `0`s become `1`s.
- `padBinary(binary)` (line 51): Takes an array of binary strings, `binary`, and finds the length of the longest one. Then, it adds `0`s to the beginning of the other strings to make them all the same length
- `addBinary(binary)` (line 64): Takes an array of binary strings, `binary`, and adds them with module 2^32. Each binary string is 32 in length, and so is the output. 
- `rightRotate(string, amount)` (line 88): Right rotates the `string` by `amount`. Basically, each character is pushed `amount` characters to the right. When a character falls off, it is moved to the beginning of the string.
- `rightShift(string, amount)` (line 95): Right shifts the `string` by `amount`. Like the right rotate function, each character is pushed to the right by `amount`, however, if one falls off, it is replaced by `0` in the beginning.
- `getNextWord(words)` (line 98): Takes a list of words, `words`, and uses that the calculate the next word in the sequence using the sha-256 algorithm. In pseudocode, with `i` being the index you are trying to find:
```
s0 := (w[i-15] rightrotate  7) xor (w[i-15] rightrotate 18) xor (w[i-15] rightshift  3)
        s1 := (w[i- 2] rightrotate 17) xor (w[i- 2] rightrotate 19) xor (w[i- 2] rightshift 10)
        w[i] := w[i-16] + s0 + w[i-7] + s1
```
- `binaryToHex(binary)` (line 120): Converts the string of binary into hexadecimal.
- `textToSha256(text)` (line 146): Converts the string `text` into a hash. This uses the above functions to convert this.
