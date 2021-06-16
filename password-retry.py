password = 'a123456'
count = 3
while count > 0:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        count = count - 1
        print('密碼錯誤! 還有', count, '次機會')
