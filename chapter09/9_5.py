import time
import re

new_format = ''
cur_time = time.localtime()
res = time.strftime("%w,%d.%m %Y %H:%M%p", cur_time)
component_list = re.split('[,. ]', res)
if component_list[0] == '0':
    new_format += 'Sunday'
elif component_list[0] == '1':
    new_format += 'Monday'
elif component_list[0] == '2':
    new_format += 'Tuesday'
elif component_list[0] == '3':
    new_format += 'Wednesday'
elif component_list[0] == '4':
    new_format += 'Thursday'
elif component_list[0] == '5':
    new_format += 'Friday'
else:
    new_format += 'Saturday'

new_format += ','

new_format += component_list[1]
new_format += '.'

if component_list[2] == '01':
    new_format += 'January'
elif component_list[2] == '02':
    new_format += 'February'
elif component_list[2] == '03':
    new_format += 'March'
elif component_list[2] == '04':
    new_format += 'April'
elif component_list[2] == '05':
    new_format += 'May'
elif component_list[2] == '06':
    new_format += 'June'
elif component_list[2] == '07':
    new_format += 'July'
elif component_list[2] == '08':
    new_format += 'August'
elif component_list[2] == '09':
    new_format += 'September'
elif component_list[2] == '10':
    new_format += 'October'
elif component_list[2] == '11':
    new_format += 'November'
elif component_list[2] == '12':
    new_format += 'December'

new_format += ' '
new_format += component_list[3]
new_format += ' '
new_format += component_list[4]

print(new_format)
