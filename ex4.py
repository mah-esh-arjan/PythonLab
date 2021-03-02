#Given the integer N - the nuumber of minutes that is passed since midnight - how many hours and minutes are dispayed
# on the 24h digital clock?
#the program should print two numbers; the number of hours (between 0 and 23) and the number of minutes *between 0 and 59)
#For example, if N=150, 150 minutes have passed since midnight - i.e. now is 2:30 am. So, the program should print 2:30.
N=int(input("enter the number of minutes that have passed since midnight : "))
hours = (N//60)
minutes = (N%60)
print(f"the hour is {hours}")
print(f"the minute is {minutes}")
print(f"its {hours}:{minutes} now ")