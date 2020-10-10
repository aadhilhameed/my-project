#calculate time using if conditon

hours = int(input('Hours: '))
minutes = int(input('Minutes: '))

if hours == 0:
    time = '12:' + minutes + ' AM'
    
elif hours < 12:
    time = str(hours) + ':' + minutes + ' AM'
    
elif hours == 12:
    time = str(hours) + ':' + minutes + ' PM'
    
else:
    time = str(hours-12) + ':' + minutes + ' PM'
    
print ('Time:',time)

