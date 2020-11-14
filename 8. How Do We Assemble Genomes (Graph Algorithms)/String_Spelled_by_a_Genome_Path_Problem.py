text = input()
try:
    while True:
        text += input()[-1]
except EOFError:
    print(text)
