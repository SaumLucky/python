time_gone = int(input("enter the time gone "))
hour = (time_gone % (60 * 60 * 24) // 3600 )
minutes = time_gone % (60 * 60) // 60
seconds = time_gone % 10
print(hour // 10,hour % 10, ":", minutes // 10,minutes % 10, ":", seconds // 10,seconds % 10)