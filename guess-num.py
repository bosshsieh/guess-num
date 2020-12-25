#讓使用者自訂隨機產出數字範圍
#讓使用者重複猜數字
#猜對的話 印出 "終於猜對了"
#猜錯的話 要告訴他 比答案大/小
#計算猜的次數

import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍開始值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
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



