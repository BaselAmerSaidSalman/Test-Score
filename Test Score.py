print("Welcome to my app")
degree = float(input("Please enter a student degree: \n"))
if degree >= 90:
  print("Excellent")
elif degree < 90 and degree >= 75:
  print("Good")
elif degree < 75 and degree >= 50:
  print("Acceptable")
else:
  print("Weak")