# We often include emoticons in our text messages to indicate 
# how we are feeling. The three consecutive characters :-) 
# indicate a happy face and the three consecutive characters 
# :-( indicate a sad face. Write a program to determine the 
# overall mood of a message

# DMOJ ccc15j2

# DMOJ submission (accepted):

mess = input()

htally = mess.count(':-)')
stally = mess.count(':-(')

if htally == 0 and stally == 0:
    print('none')
elif htally > stally:
    print('happy')
elif stally > htally:
    print('sad')
else:
    print('unsure')
