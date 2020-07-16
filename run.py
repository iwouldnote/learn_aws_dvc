import time

with open('file.txt', 'r') as f:
    time.sleep(3)
    name = f.read()
    print(f'I found your name, {name}')

with open('result.txt', 'w') as f:
    time.sleep(3)
    name = f.write(f'Your name is {name}')
    print('I wrote down your name')
