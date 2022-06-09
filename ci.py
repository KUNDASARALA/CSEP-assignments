#compute compound interest using recursion function 
#assuming the interest to be 10%
def comp(p,n):
	if(n==1):
		return p*(1.1)
	else:
		return (comp(p,n-1))*1.1
print(comp(200,3))
