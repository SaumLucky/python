time_gone = int(input("enter the time gone "))
hour = (time_gone % (60 * 24) // 60 )
minuters = time_gone % 60
print( hour, minuters)