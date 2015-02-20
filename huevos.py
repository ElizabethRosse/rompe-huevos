import random
r=random.randrange(100)
print(r)
a = 14
b =1
for x in [14,27,39,50,59,67,74,80,85,89,92,94,95,99]:
	if (r<=x):	
		for y in range(b,x+1):
			if(y==r):
				print(y)
	b=x									
if(r==100):
	print(r)
