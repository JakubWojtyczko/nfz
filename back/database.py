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
