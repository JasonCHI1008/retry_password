password = "spike1008"
x = 3#機會
while x <= 3 and x > 0:
    input_pass = input("請輸入密碼:")
    if password == input_pass:
        print("登入成功")
        break#leave loop
    else:
        x = x - 1
        print("密碼錯誤!還有", x,"次機會")
if x == 0:
    print("此帳號被凍結")