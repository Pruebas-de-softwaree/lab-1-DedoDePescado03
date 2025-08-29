import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    userManager = UserManager()

    
    for i in range (1000):   
        userManager.add_user(i, f"User {i}")
    
    #usuario = userManager.find_user("1")
    #userManager.delete_user("1")
    #usuario = userManager.find_user(1)
    #allUsers = userManager.get_all_names()
    #avgUsersId = userManager.average_user_id() 
    usuario = userManager.find_user(1)
    print("end")