def fun_palindrome(str):

	str_rev = ''.join(list(reversed(str)))
	if str==str_rev:
		print("Its a palindrome")
	else:
		print("Not a PALINDROME")
	
if __name__ == "__main__":
	str = input("Enter a string:")
	fun_palindrome(str)