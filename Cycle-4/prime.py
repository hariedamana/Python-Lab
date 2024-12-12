def is_prime(num):
	if num<=1:
		return false
	for i in range(2,int(num**0.5)+1):
		if num%i==0:
			return False
		return True
def nth_prime(n):
	count,current=0,2
	while count<n:
		if is_prime(current):
			count+=1
		if count<n:
			current+=1
	return current

n=int(input("Enter n:"))
print(f"The {n}th prime number is {nth_prime(n)}.")
