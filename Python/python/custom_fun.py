def is_strong_password(password):
  has_length = len(password) >= 8
  has_upper = not password.islower()
  has_not_only_letters = not password.isalpha()
  return has_length and has_upper and has_not_only_letters


# User se password input lena
user_pass = input("Apna password likhein: ")

if is_strong_password(user_pass):
  print("Password strong hai!")
else:
  print(
      "Password must be at least 8 characters long, include a capital letter, and not contain only letters."
  )