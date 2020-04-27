import os

class DataBase:

    def __init__(self):
        pass
        
    
    def check_user(self, login, password):
        if not os.path.isfile('../user_db.txt'):
            return -1
        with open('../user_db.txt') as file:
            for line in file.readlines():
                numb, log, pas = line.split()
                if log == login and pas == password:
                    return numb
        return -1

    def add_user(self, login, password):
        # check login does not already exist
        max_num = 0
        if os.path.isfile('../user_db.txt'):
            with open('../user_db.txt') as file:
                for line in file.readlines():
                    numb, log, pas = line.split()
                    max_num = int(numb)
                    if log == login:
                        # login already exists
                        return -1
        with open('../user_db.txt', 'a') as file:
            new_num = max_num + 1
            file.writelines(["{} {}\t{}\n".format(new_num, login, password)])
        return new_num

    def add_to_fav(self, token, id):
        with open('../fav_db.txt', 'a') as file:
            file.writelines(["{}\t{}\n".format(token, id)])

    def remove_fav(self, token, id):
        if not os.path.isfile('../fav_db.txt'):
            return
        lines = []
        with open('../fav_db.txt') as file:
            for line in file.readlines():
                print(line.split())
                old_token, old_id = line.split()
                if old_token == token and old_id == id:
                    continue
                else:
                    lines.append(line)
        print(lines)
        with open('../fav_db.txt', 'w') as file:
            file.writelines(lines)

    def is_fav(self, token, id):
        if not os.path.isfile('../fav_db.txt'):
            return
        with open('../fav_db.txt') as file:
            for line in file.readlines():
                old_token, old_id = line.split()
                if old_token == token and old_id == id:
                    return True
        return False

    def get_fav_id(self, token):
        if not os.path.isfile('../fav_db.txt'):
            return []
        fav_list = []
        with open('../fav_db.txt') as file:
            for line in file.readlines():
                old_token, old_id = line.split()
                if old_token == token:
                    fav_list.append(old_id)  
        return fav_list