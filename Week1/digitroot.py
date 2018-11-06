def digit_root(n):
	print("value of input:",n)
	digits=list(n)
	sum=0
	for i in digits:
		sum+=int(i)
	if sum >= 10:
		return digit_root(str(sum))
	else:
		print("Current sum:",sum)	
		return sum 


if __name__ =='__main__':
	n=input("Enter any number:")
	print("Root is :", digit_root(n))