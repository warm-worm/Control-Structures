###
##
# Program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard
# Sample:
# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm
##
###
time = input('Enter the hour (hh:mm): ')
hour = int(time[:2])
minute = time [3:]
if hour >= 12:
    converted_hour = int(hour - 12)
else:
    converted_hour = hour

if hour > 12:
    noon = 'pm'
elif hour <= 12:
    noon = 'am'
print(f'Time in 12-hour format is: {converted_hour}:{minute}{noon}')