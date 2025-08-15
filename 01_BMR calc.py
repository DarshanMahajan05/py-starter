gender = input("Enter your gender(M/F): ")

weight = int(input("Enter your weight in kg"))

height = int(input("Enter your height in cm"))

age = int(input("Enter your age in years"))



if gender == 'M':
    BMRFM = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 *age)
    print("Your") 
    print(BMRFM)


elif gender == 'F':
    BMRFW = 655.1 + (9.563 *weight) +(1.850 * height) - (4.676 *age)
    print("Your") 
    print(BMRFW)

else :
    print("Please enter a valid information")