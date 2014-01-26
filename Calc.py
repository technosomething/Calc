# Simple trinomial factoring with python by technosomething v1.1 created 4/17/2013 
import sys,os,time
cls = lambda: os.system('cls')
cls()
print "\nWelcome.\nPlease have your quadratic equation ready and in the form\nAx^2+Bx+C A>0\n"
C=[]
while True:
	ans1="oops"
	while True:
		try:
			a=int(raw_input("Enter A: "))
			if a>292681:
				print "Value out of range. Please use a smaller value for A"
				continue
			if a<0:
				print "A MUST be positive. Factor out -1 and try again"
				continue
			break
		except:
			print "Try again"
	while True:
		try:
			b=int(raw_input("Enter B: "))
			break
		except:
			print "Try again"
	while True:
		try:
			c=int(raw_input("Enter C: "))
			break
		except:
			print "Try again"
	if c<0:
		c=-1*c
		C.append(-1)
		c_neg=True
	else:
		C.append(1)
		c_neg=False
	y=a*c
	list1=[]
	list2=[]
	for x in range(1,y+1):
		if y%x==0:
			list1.append(x)
			list2.append(y/x)
	for i,x in enumerate(list1):
		if x+list2[i]==b and not c_neg:
			ans1=x
			ans2=list2[i]
			break
		if -x+list2[i]==b and c_neg:
			ans1=-x
			ans2=list2[i]
			break
		if -x-list2[i]==b and not c_neg:
			ans1=-x
			ans2=-list2[i]
			break		
	try:
		ans1+1
	except:
		print"\nUNFACTORABLE\n"
		cont=raw_input("Another? Y/N: ")
		try:
			if cont.lower()[0]=="y":
				print""
				continue
			else:
				break
		except:
			break
	a_list1=[]
	a_list2=[]
	if a>1:
		for x in range(1,a+1):
			if a%x==0:
				a_list1.append(x)
				a_list2.append(a/x)
		for i,x in enumerate(a_list1):
			if ans1%x==0 and ans2%a_list2[i]==0:
				ans1x=a_list2[i]
				ans2x=x
				ans1=ans1/ans2x
				ans2=ans2/ans1x
				break
	else:
		ans1x,ans2x=1,1
	print""
	if b<0:
		sign1=""
	else:
		sign1="+"
	if c_neg:
		sign2="-"
	else:
		sign2="+"
	if ans1<0:
		sign3=""
	else:
		sign3="+"
	if ans2<0:
		sign4=""
	else:
		sign4="+"
	if a==1:
		a=""
	if b==1:
		b=""
	if ans1x==1:
		ans1x=""
	if ans2x==1:
		ans2x=""
	print str(a)+"x^2"+sign1+str(b)+"x"+sign2+str(c)+" = ("+str(ans1x)+"x"+sign3+str(ans1)+")("+str(ans2x)+"x"+sign4+str(ans2)+")\n"
	cont=raw_input("Another? Y/N: ")
	try:
		if cont.lower()[0]=="y":
			print""
			continue
		else:
			break
	except:
		break
print "\n\nThank you for using Calc 1.1\n\n"
time.sleep(1)
print "Good Bye.\n"