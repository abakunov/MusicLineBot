def return_pass():
    with open('pass.txt', 'r') as f:
        return f.readline().strip()

