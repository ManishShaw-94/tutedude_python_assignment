print('Please enter your score to know your grade: ')
val = int(input())
if (val >= 90 and val <=100):
    print("Congratulation! Your Grade is 'A'")
elif (val >= 80 and val <=89):
    print("Excelent! Your Grade is 'B'")
elif (val >= 70 and val <=79):
    print("Very Good! Your Grade is 'C'")
elif (val >= 60 and val <=69):
    print("Good! Your Grade is 'D'")
elif (val >= 0 and val <=59):
    print("Hard Luck! Your Grade is 'F'")
else:
    print('Please enter a valid score')