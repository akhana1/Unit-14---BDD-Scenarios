
import datetime
import sys

def social_security_calculator():
    while(1):
        birthyear = input("Enter the year of birth or to exit ")
        if birthyear == "":
            sys.exit("Process finished with exit code 0")
        else:
            birthyear = int(birthyear)
            birthmonth = int(input("Enter the month of birth "))
            current_year = datetime.datetime.now().strftime("%Y")
            if (birthyear < 1937 or birthyear == 1937):
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirment age is 65 and 0 month")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 65))

            elif (birthyear == 1938):
                birthmonth = 2 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 65 and 2 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 65))

            elif (birthyear == 1939):
                birthmonth = 4 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 65 and 4 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 65))

            elif (birthyear == 1940):
                birthmonth = 6 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 65 and 6 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 65))

            elif (birthyear == 1941):
                birthmonth = 8 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 65 and 8 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 65))

            elif (birthyear == 1942):
                birthmonth = 10 + birthmonth
                if(birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 65 and 10 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 65))

            elif (birthyear == 1943 or birthyear > 1943 and birthyear == 1954 or birthyear < 1954):
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 66")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 66))

            elif (birthyear == 1955):
                birthmonth = 2 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 66 and 2 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 65))

            elif (birthyear == 1956):
                birthmonth = 4 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 66 and 4 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 66))

            elif (birthyear == 1957):
                birthmonth = 6 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 66 and 6 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 66))

            elif (birthyear == 1958):
                birthmonth = 8 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 66 and 8 months")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 66))

            elif (birthyear == 1959):
                birthmonth = 10 + birthmonth
                if (birthmonth > 12):
                    birthmonth = birthmonth - 12
                    birthyear = birthyear + 1
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 66 and 10 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 66))

            elif (birthyear == 1960 or  birthyear > 1960 and birthyear < int(current_year)):
                months = datetime.date(birthyear, birthmonth, 1).strftime('%B')
                print("your full retirement age is 67 and 0 months ")
                print("this will be in {} of".format(months) + " {}".format(birthyear + 67))


print("Social Security Full Retirement Age Calculator")
social_security_calculator()
