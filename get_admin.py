def is_admin(id):
    id = str(id)
    with open('admins.txt', 'r') as file:
        f = False
        for i in file.readlines():
            if id in i.strip():
                f = True
                break
        if f:
            return True
        return False


def add_admin(id):
    if not(is_admin(id)):
        with open('admins.txt', 'a') as f:
            f.write(str(id) + '\n')


