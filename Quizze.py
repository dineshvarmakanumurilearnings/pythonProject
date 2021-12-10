from random import choice
capsData={'Andhra Pradesh':'Amaravati','Arunachal Pradesh': 'Itanagar','Assam':'Dispur',
          'Bihar':'Patna','Andhra Pradesh':'Amaravati','Andhra Pradesh':'Amaravati',
          'Chhattisgarh':'Naya Raipur','Goa':'Panaji','Gujarat':'Gandhinagar',
          'Haryana':'Chandigarh','Himachal Pradesh':'Shimla','Jharkhand':'Ranchi',
          'Karnataka':'Bangalore','Kerala':'Thiruvananthapuram','Madhya Pradesh':'Amaravati',
          'Andhra Pradesh':'Amaravati','Andhra Pradesh':'Amaravati', 'Andhra Pradesh':'Bhopal',
          'Maharashtra':'Mumbai','Telangana':'Hyderabad','Tamil Nadu':'Chennai',
          'West Bengal':'Kolkata'}
states=list(capsData.keys())
print('Welcome to Quiz Game........')
score=0
for x in range(0,10):
    state= choice(states)
    state_capital=capsData.get(state)
    answer=input('What is the Capital City of '+state+' : ')
    if answer.capitalize() == state_capital:
        print('Correct!')
        score +=1
    else:
        print('Wrong Answer!')
print('your Total Score is :',score)
