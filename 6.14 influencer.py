###
## Program that checks whether a given person is a good influencer, 
# that is, whether the person has at least two of the following accounts: 
# Facebook, Twitter or Instagram
# Use logical type variables: facebook, twitter, instagram, the value of
# which indicates whether the person has an account on the social 
# networking site
# Sample:
# facebook = True
# twitter = False
# instagram = True
## You are a good influencer!
### 
facebook = input('Do you have a Facebook account? (Y/N) ')
twitter = input('Do you have a Twitter account? (Y/N) ')
instagram = input('Do you have an Instagram account? (Y/N) ')
facebook = (facebook == 'Y')
twitter = (twitter == 'Y')
instagram = (instagram == 'Y')

if (facebook + twitter + instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You are a bad influencer.")
