password = '123'
i = 3
while i > 0:
	swd = input('請輸入密碼')
	if swd == password:
		print('登入成功')
		break
	else:
	 	i=i-1
	 	print('密碼錯誤剩餘',i,'次機會')
