hours = int(input('Hours: '))
minutes = int(input('Minutes: '))
if hours == 0:
    time = '12:' + minutes + ' AM'
elif hours < 12:
    time = int(hours) + ':' + minutes + ' AM'
elif hours == 12:
    time = int(hours) + ':' + minutes + ' PM'
else:
    time = int(hours-12) + ':' + minutes + ' PM'
    
print ('Time:',time)

