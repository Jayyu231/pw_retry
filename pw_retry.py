#密碼重試程式

password = 'a123456'

a = 0
while a < 3:
	a = a + 1
	user_keyin_pw = input('Please keyin your password :')
	if password == user_keyin_pw :
		print('pw input correctly')
		break
		#raise SystemExit
	
	elif a ==3 :
		print('You\'re running out of time of guessing')
		raise SystemExit
	elif password != user_keyin_pw :
		print('Your pw is wrong! you still have ' + str(3-a) +' times chance')
	

