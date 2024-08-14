#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per hr:")
r = float(rate)
pay = h * r

if h >= 40:
    overtime_pay = (h - 40) * (r * 0.5)
    pay = pay + overtime_pay
    print(pay)
else:
    print(pay)