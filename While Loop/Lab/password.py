TEXT = 'Welcome {}!'

username = input()
password = input()

while True:
      user_password = input()
      if(user_password == password):
          print(TEXT.format(username))
          break



