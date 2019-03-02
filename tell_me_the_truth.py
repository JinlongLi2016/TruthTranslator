while True:
	words = input("你想输入的待翻译的话:\n")
	print("真心话其实是： ", end='')
	if words=='讨厌':
		print("你一点都不讨厌")
	elif words=='我睡不着' or words=='睡不着':
		print("你快来陪我啊")
	elif words=="十分钟" or words=='几分钟':
		print("一个小时")
	elif words=="看什么看什么" or words=='看什么看':
		print("哈哈，再多看一会")
	elif words=="不理你了" or words=='不理你':
		print("快哄我啊！")
	elif words=='现在怎么办才好':
		print("超开心")
	elif words=="顺路":
		print("我精心准备的...")
	elif words=='不贵' or words=='不贵不贵':
		print("老娘一个月的生活费啊！！")
	elif words=='你想睡觉了' or words=='你想睡觉' or words == '你要睡觉了吗':
		print("别睡,多和我聊会天吧")
	elif words=='我要睡觉了':
		print("你是真的烦，我是真的想睡觉了")
	elif words=='我漂亮吗':
		print('老娘今天画了这么多的装,你没啥感觉吗？')
	else:
		print("我也有有点不懂,请移步isseues")