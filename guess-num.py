#產生一個隨機整數1~100(不要印出來)
#讓使用者重複猜數字
#猜對的話 印出 "終於猜對了"
#猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1,100)
count = 0
while True:
	# print(r)
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('你猜了', count, '次')
		break
	elif num > r:
		print('你的數字比答案大')
	elif num < r:
		print('你的數字比答案小')
	print('你猜了', count, '次')



