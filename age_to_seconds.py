# first we take an input from a user

age = input('Please enter your age(in years): ')

age_in_seconds = int(age) * 365 * 24 * 60 * 60

# we need to convert age into integers so 

# now we print the age

print(f'Your age in seconds is {age_in_seconds} seconds.')

# test it out