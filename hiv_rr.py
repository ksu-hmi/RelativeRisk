#Relative Risk: Human Immunodeficiency Virus Acquisition
#Section 1: Demographics

#gender = "male"
#while (gender == "female") or (gender == "male"):
#gender = input("What is your Gender? Male or Female").lower()

while True:
    gender = input("\n\nWhat is your Gender? Male or Female? ").lower()
    if gender.lower() == "male":
        print("Males pose a higher risk than females.")
        break
    elif gender.lower() == "female":
        print("Females do not pose as much of a risk as males.")
        break
    else:
        print("Invalid Choice. Please Try Again.")
    
while True:
    age = int(input("\n\nWhat is your Age? "))
    if age < 18:
        print("your age is ",age,"... Unfortunately, you are a minor.")
        break
    elif age > 17 and age < 25:
        print("your age is ",age,"... Your age group does not pose as a major risk.")
        break
    elif age > 24 and age < 30:
        print("your age is ",age,"... You fall within the range 25-29, the range that poses the highest risk of acquisition.")
        break
    elif age > 29 and age < 54:
        print("your age is ",age,"... Your age group does not pose as a major risk.")
        break
    elif age < 125 and age > 53:
        print("your age is ",age,"... Your age group pose a risk.")
        break
    else:
        print("Invalid Entry. Please Try Again.")

#race = "white"
#while (race == "black") or (race == "white") or (race == "hispanic") or (race == "asian") or (race == "other"):

while True:
    print("\n\nPlease enter your race as black, white, hispanic, asian, or other.")
    race = input("What is your Race/Ethnicity? ").lower()
    if race == "black".lower():
        print("your race poses the greatest risk of acquisition.")
        break
    elif race == "white".lower() or race == "asian".lower() or race == "other".lower():
        print("your race doesn't pose a significant risk.")
        break
    elif race == "hispanic".lower():
        print("your race poses the second greatest risk of acquisition.")
        break
    else:
        print("Invalid Entry! Please try again.")

while True:
    print("\n\nPlease enter Drop-Out, GED, High-School, Certificate, Associates, \nBachelors, Masters, or Doctoral")
    educ = input("What is your Highest Level of Education? ").lower()
    if educ == "Drop-Out".lower():
        print("Based on your education status, you pose the greatest risk of acquisition.")
        break
    elif educ == "GED".lower() or educ == "High-School".lower():
        print("Based on your education status, you pose as a risk of acquisition.")
        break
    elif educ == "Certificate".lower() or educ == "Associates".lower() or educ == "Bachelors".lower() or educ == "Masters".lower() or educ == "Doctoral".lower():
        print("Based on your education status, you do not pose as a risk of acquisition.")
        break
    else:
        print("Invalid Selection! Please try again!")
    

#Section 2
#print("\n\nPlease answer these questions with either a 0 or 1.")
#print("0 is No. 1 is Yes... \nAny other input would not be accepted.")
print("\n\n1. Have you or your sexual partners had other sexual partners within the past year?")
print("2. Have you ever had an STD/STI?")
print("3. Have you or your sexual partner(s) injected drugs or other substances and/or shared needles with another person?")
print("4. Have you ever had sex with a male partner who has had sex with another male?")
print("5. Have you ever had sex with a person who is HIV infected?")
print("6. Have you ever been paid for sex or had sex from a prostitute?")
print("7. Have you experienced or been exposed to blood-to-blood contact?")
print("8. Have you or your sexual partners received blood transfusions on or before 1985?")
print("9. Have you been the victim of nonconsentual sex rape/sexual abuse?")
print("10. Have you ever been tested for an STD?")
print("11. Do you or your sexual partner(s) use protection during intercourse?")
print("12. Do you or your sexual partner(s) get screened/tested?")

#count the number of 0s and 1s and total them.
total = 0
response = ""

def count_response(report = "all"):
    print("\n\nPlease answer these questions with either a 0 or 1. \n0 is No. 1 is Yes... \nAny other input would not be accepted.")
    print("\nThere should only be 12 responses recorded.\nType 'q' to quit.")
    total = 0
    response = ""
    while True:
        num = input("Now then, enter your response using a 0 or 1 or 'q' to quit.")
        if (num.isdigit()):
            total = total + int(num)
            if (report.upper() == "ALL"):
                response = response + num + "\n"
        elif (num == "Q" or num.startswith("Q") or num.startswith("q")):
            print("\n")
            if(report.upper() == "ALL"):
                print("Now Displaying all responses and total.")
                print("Responses:")
                print(response,"\n")
                print("Total:")
                print(total)
                break
        else:
            print("your input is invalid, please try again.")

count_response("ALL")

#input("Have you or your sexual partners had other sexual partners within the past year?")
#input("Have you ever had an STD/STI?")
#input("Have you or your sexual partner(s) injected drugs or other substances and/or shared needles with another person?")
#input("Have you ever had sex with a male partner who has had sex with another male?")
#input("Have you ever had sex with a person who is HIV infected?")
#input("Have you ever been paid for sex or had sex from a prostitute?")
#input("Have you experienced or been exposed to blood-to-blood contact?")
#input("Have you or your sexual partners received blood transfusions on or before 1985?")
#input("Have you been the victim of nonconsentual sex rape/sexual abuse?")
#input("Have you ever been tested for an STD?")
#input("Do you or your sexual partner(s) use protection during intercourse?")
#input("Do you or your sexual partner(s) get screened/tested?")
#if input == 1:
    #input("How often do you get tested throughout the year?")
#input("Do you and your sexual partner(s) plan to become pregnant or already pregnant?")
