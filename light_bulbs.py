###
# House lighting with three bulbs and two switches
# Switch one turns one light bulb on and switch two turns the other two on
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
turning = int(input('Which light switch do you want to switch on? (1 - first one, 2 - second one, 3 - both, 4 - neither)'))

if turning == 1:
    light_switch1 == True
    bulbs_on += 1
if turning == 2:
    light_switch2 == True
    bulbs_on += 1
if turning == 3:
    light_switch1 == True
    light_switch2 == True
    bulbs_on += 2
if turning == 4:
    light_switch1 == False
    light_switch2 == False
    bulbs_on = 0
print(f'There is/are currently {bulbs_on} light bulb(s) illuminating the house.')