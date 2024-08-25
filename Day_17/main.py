class User:
    pass


# user_1 = User()
# user_1.id = "0101"
# user_1.username = "murga"

# # print(user_1.username)

# user_2 = User()
# user_2.id = "0110"
# user_2.username = "amar"


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(505, "Murga")
print(user_1.id)
print(user_1.username)

user_2 = User(422, "Amar")
print(user_2.followers)

user_1.follow(user_2)

print(user_2.followers, user_1.following)
