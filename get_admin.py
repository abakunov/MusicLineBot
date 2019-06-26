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


def add_admin(id, username):
    if not(is_admin(id)):
        with open('admins.txt', 'r') as f:
            user_id = int(f.readline().strip().split()[-1])
        with open('admins.txt', 'a') as f:
            f.write(str(user_id) + ' ' + str(id) + ' ' + username + '\n')
            user_id += 1
        file = []
        with open('admins.txt', 'r') as f:
            file = f.readlines()
        with open('admins.txt', 'w') as f:
            f.write('now id ' + str(user_id) + '\n')
            for i in file[1:]:
                f.write(i)

