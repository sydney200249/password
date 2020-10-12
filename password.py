password = 'a123'
i = 3
while i > 0:
	i = i - 1
	pwd = input('最多輸入三次密碼：')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤！')
		if i > 0:
			print('還有',i,'次機會')
		else:
			print('基於帳號安全已鎖定')

