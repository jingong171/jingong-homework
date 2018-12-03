print("Give me two numbers, and I'll sum them.")
print("Enter 'q' to quit.")
while True:
	x = input("\nFirst number: ")
	if x == 'q':
		break
	y = input("Second number: ")
	if y == 'q':
		break
	try:
		x=int(x)
		y=int(y)
	except ValueError:
		print("请不要输入文本")
	else:
		print(x+y)
