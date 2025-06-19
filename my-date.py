import datetime

x = datetime.datetime.now()

d = x.strftime("%Y-%m-%d")
h = x.strftime("%H:%M:%S")

print(f"Today is {d} and it is {h}.")
