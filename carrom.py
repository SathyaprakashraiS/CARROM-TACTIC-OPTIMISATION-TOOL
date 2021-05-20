import numpy as car
import math
xaxis=car.zeros([12,12],dtype=int) 
yaxis=car.zeros([12,12],dtype=int)
#print("\nMatrix b : \n", b[0][1])

#b=[[100]*12]*12

'''
COMMENTED GRAPH
k=1
for i in range(12):
	for j in range (12):
		xaxis[i][j]=100+k
		k+=1
print(xaxis)
print(" ")
k=44
j=1
g=k
for i in range(12):
	for j in range (12):
		yaxis[i][j]=100+k
		k-=1
	k=g-1
	g-=1
print(yaxis)
'''

graph=[
["9,0","9,1","9,2","9,3","9,4","9,5","9,6","9,7","9,8","9,9"],
["8,0","8,1","8,2","8,3","8,4","8,5","8,6","8,7","8,8","8,9"],
["7,0","7,1","7,2","7,3","7,4","7,5","7,6","7,7","7,8","7,9"],
["6,0","6,1","6,2","6,3","6,4","6,5","6,6","6,7","6,8","6,9"],
["5,0","5,1","5,2","5,3","5,4","5,5","5,6","5,7","5,8","5,9"],
["4,0","4,1","4,2","4,3","4,4","4,5","4,6","4,7","4,8","4,9"],
["3,0","3,1","3,2","3,3","3,4","3,5","3,6","3,7","3,8","3,9"],
["2,0","2,1","2,2","2,3","2,4","2,5","2,6","2,7","2,8","2,9"],
["1,0","1,1","1,2","1,3","1,4","1,5","1,6","1,7","1,8","1,9"],
["0,0","0,1","0,2","0,3","0,4","0,5","0,6","0,7","0,8","0,9"]
]
coingraph=[
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
]
hieght=10
width=10
lwidth=0
for i in range(10):
	for j in range(10):
		print(graph[i][j],end=" ")
	print(" ")

def commafinder(q):
	s=""
	d=""
	flag=0
	for i in range(len(q)):
		if(q[i]!="," and flag==0):
			s+=q[i]
		if(q[i]==","):
			flag=1
			j=i+1
			while(j<len(q)):
				d+=q[j]
				j+=1
	return s,d
def pocketdistance(q,w,e,r):#c v x y original
	distance=0
	yequ=int(r)-int(w)
	xequ=int(e)-int(q)
	#print(xequ)
	#equation=(pow((xequ),2)-pow((yequ),2))
	equation=((xequ*xequ)+(yequ*yequ))
	#print(equation)
	distance=math.sqrt(equation)
	return distance
def straightline(q,w,e,r,t):
	q=float(q)
	w=int(w)
	e=int(e)
	r=int(r)
	t=int(t)
	z=t
	print("q",q)
	print("w",w)
	print("e",e)
	print("r",r)
	print("t",t)
	'''
	if(r<=boardxmedian):
		distanceb=r-w
		if(t<=boardymedian):
			for t in range(boardleft,t):
				print("here1special")
				print("i",t)
				if(t==((q*r)+distanceb)):
					print("returned")
					print(e)
					return t
				else:
					print("over1 and e value is :",(q*r)+distanceb)
					t-=1
		else:
			for t in range(t,boardright):
				if(t==((q*r)+distanceb)):
					print("returned")
					print(e)
					return t
				else:
					print("over1 and e value is :",(q*r)+distanceb)
					t+=1
	'''
	#new model testcase
	'''distanceb=r-w
	if(t<=boardymedian):
		for t in range(boardleft,z):
			print("here1special")
			print("i",t)
			if(z==((q*r)+distanceb)):
				print("returned")
				print(e)
				return t
			else:
				print("over1 and e value is :",(q*r)+distanceb)
				t-=1
	if(t>=boardymedian):
		for t in range(z,boardright):
			if(z==((q*r)+distanceb)):
				print("returned")
				print(e)
				return t
			else:
				print("over1 and e value is :",(q*r)+distanceb)
				t+=1'''
	'''
	if(r>=w):
		print("here1")
		distanceb=r-w
		i=t
		for i in range(width):
			print("i",i)
			if(e==((q*r)+distanceb)):
				return i
			else:
				i+=1
		
	if(r<=w):
		print("here2")
		distanceb=w-r
		i=t
		for i in range(width):
			print("i",i)
			if(e==((q*r)+distanceb)):
				return i
			else:
				i+=1
		return 0
	if(t>=e):
		print("here3")
		distanceb=e-t
		i=y
		for i in range(width):
			print("i",i)
			if(e==((q*r)+distanceb)):
				return i
			else:
				i-=1
		return 0
	if(t<=e):
		print("here4")
		distanceb=e-t
		i=t
		for i in range(width):
			print("i",i)
			if(e==((q*r)+distanceb)):
				return i
			else:
				i-=1
		return 0
	return 0
	'''


	#was working now made into comment for now 
	t=z
	if(r>w):
		print("here1")
		distanceb=r-w
		for t in range(t,width):
			print("i",t)
			if(r-w<=0):
				slope1=0
				slope2=0
			else:
				slope1=(t-e)/(r-w)
				slope2=(e-t)/(r-w)
			if(w-r<=0):
				slope3=0
				slope4=0
			else:
				slope3=(t-e)/(w-r)
				slope4=(e-t)/(w-r)
			#if(t==((q*r)+distanceb)):
			if(slope1==1 or slope2==1 or slope3==1 or slope4==1):
				print("returned")
				print((q*r)+distanceb,r,t)
				return r,t
			else:
				print("over1 and e value is :",(q*r)+distanceb)
				t+=1
		t=z
		for t in reversed(range(0,t)):
			print("i",t)
			if(r-w<=0):
				slope1=0
				slope2=0
			else:
				slope1=(t-e)/(r-w)
				slope2=(e-t)/(r-w)
			if(w-r<=0):
				slope3=0
				slope4=0
			else:
				slope3=(t-e)/(w-r)
				slope4=(e-t)/(w-r)
			#if(t==((q*r)+distanceb)):
			if(slope1==1 or slope2==1 or slope3==1 or slope4==1):
				print("returned")
				print((q*r)+distanceb,r,t)
				return r,t
			else:
				print("over1 and e value is :",(q*r)+distanceb)
				t-=1
	t=z
	if(r<w):
		print("here2")
		distanceb=w-r
		for t in range(t,width):
			if(r-w<=0):
				slope1=0
				slope2=0
			else:
				slope1=(t-e)/(r-w)
				slope2=(e-t)/(r-w)
			if(w-r<=0):
				slope3=0
				slope4=0
			else:
				slope3=(t-e)/(w-r)
				slope4=(e-t)/(w-r)
			#if(t==((q*r)+distanceb)):
			if(slope1==1 or slope2==1 or slope3==1 or slope4==1):
				print("found position :",r,t)
				return r,t
			else:
				print("pass")
				t+=1
		t=z
		for t in reversed(range(0,t)):
			if(r-w<=0):
				slope1=0
				slope2=0
			else:
				slope1=(t-e)/(r-w)
				slope2=(e-t)/(r-w)
			if(w-r<=0):
				slope3=0
				slope4=0
			else:
				slope3=(t-e)/(w-r)
				slope4=(e-t)/(w-r)
			#if(t==((q*r)+distanceb)):
			if(slope1==1 or slope2==1 or slope3==1 or slope4==1):
				print("found position :",r,t)
				return r,t
			else:
				print("pass")
				t-=1
		print("no pos found")
		#return 0
	t=z
	if(t>e):
		print("here3",t)
		distanceb=e-t
		for t in reversed(range(0,t)):
			if(r-w<=0):
				slope1=0
				slope2=0
			else:
				slope1=(t-e)/(r-w)
				slope2=(e-t)/(r-w)
			if(w-r<=0):
				slope3=0
				slope4=0
			else:
				slope3=(t-e)/(w-r)
				slope4=(e-t)/(w-r)
			#if(t==((q*r)+distanceb)):
			if(slope1==1 or slope2==1 or slope3==1 or slope4==1):
				print(" found position :",r,t)
				return r,t
			else:
				t-=1
		#return 0
	t=z
	if(t<e):
		print("here4")
		distanceb=e-t
		for r in range(t,width):
			if(r-w<=0):
				slope1=0
				slope2=0
			else:
				slope1=(t-e)/(r-w)
				slope2=(e-t)/(r-w)
			if(w-r<=0):
				slope3=0
				slope4=0
			else:
				slope3=(t-e)/(w-r)
				slope4=(e-t)/(w-r)
			#if(t==((q*r)+distanceb)):
			if(slope1==1 or slope2==1 or slope3==1 or slope4==1):
				print("the position is  :",r,t)
				return r,t
			else:
				t+=1
		#return 0
	t=z
	return 0,0
def triangle(q,w,e,r,t,y):#er pocketloc qw coinloc ty newcoinloc
	q=int(q)
	w=int(w)
	e=int(e)
	r=int(r)
	t=int(t)
	y=int(y)
	o=0
	a=0
	h=0
	temp=0
	degree=0
	#distance=[]
	o=math.sqrt(((y-r)*(y-r))+((t-q)*(t-q)))
	#distance.append(o)
	a=math.sqrt(((r-w)*(r-w)+(q-e)*(q-e)))
	#distance.append(a)
	h=math.sqrt(((r-y)*(r-y)+(t-e)*(t-e)))
	#distance.append(h)
	#print("triangle function",lwidth,width)
	if(o>a and o>h):
		print("in o")
		temp=h
		h=o
		o=temp
	if(a>h and a>o):
		print("in a")
		temp=h
		h=a
		a=temp
	degree=math.asin(o/h)
	degree*=57.296
	print("degree :",degree)
	return o,a,h,degree
def straightstricker():
	print("straight stricker function")
pockets=["9,0","9,9","0,0","0,9"]
pocketslope=["0","0","0","0"]
playerpos=["1,1","1,8"]
boardleft=0 #of y
boardright=9#of y
boardtop=9 #of x
boardbottom=0#of x
whitemass=5
blackmass=5
redmass=5
strickermass=5
timel=0.3
timeh=0.7
boardymedian=(boardright-boardleft)/2
boardxmedian=(boardtop-boardbottom)/2
print("which coin do you want to pocket ? enter the location of it")
x=int(input("xaxis :"))
y=int(input("yaxis :"))
coingraph[x][y]=1
print(x,y)
mindis=999
flagpocket=0
for i in range(len(pockets)):
	spocket=pockets[i]
	c,v=commafinder(spocket)
	pocketslope[i]=pocketdistance(c,v,x,y)
print("pocketslope :",pocketslope)
for i in range(len(pockets)):
	numbertest=int(pocketslope[i])
	if(numbertest<mindis):
		mindis=numbertest
		flagpocket=i
		print("flagpocket :",flagpocket)
print("nearest pocket location: ",pockets[flagpocket],"distance between: ",mindis)
#finding is coin pocket on straight line
#y=mx+c
xpocket,ypocket=commafinder(pockets[flagpocket])
#slope = del(y)/del(x)

'''
testx=int(ypocket)-int(y)
testy=int(xpocket)-int(x)
print(testx,testy)
'''
xslope=(int(xpocket)-int(x))
if(xslope!=0):
	slope=(int(ypocket)-int(y))/(int(xpocket)-int(x))
else:
	slope=(int(ypocket)-int(y))
if(slope<0):
	slope*=-1
print("slope: ",slope)
print("xpocket :",xpocket,"ypocket :",ypocket,x,y)
online=0
if(int(xpocket)==int(x) or int(ypocket)==int(y)):
	print("qwe")
	online=1
	posx,posy=straightline(slope,xpocket,ypocket,x,y)
	#opposite=math.sqrt(((int(posy)-int(ypocket))*(int(posy)-int(ypocket)))+((int(posx)-int(x))*(int(posx)-int(x))))
	opposite=math.sqrt(((int(y)-int(ypocket))*(int(y)-int(ypocket)))+((int(xpocket)-int(x))*(int(xpocket)-int(x))))
	#a=math.sqrt(((r-w)*(r-w)+(q-e)*(q-e)))
	#h=math.sqrt(((r-y)*(r-y)+(t-e)*(t-e)))
else:
	print("rty")
	online=0
if(slope!=1 and online==0):
	posx,posy=straightline(slope,xpocket,ypocket,x,y)
	print("the position to be moved is :",posx,posy)
	#find triangle
	opposite,adjacent,hypotenuse,degree=triangle(x,y,xpocket,ypocket,posx,posy)#qwerty
	print("opposite :",opposite,"adjacent :",adjacent,"hypotenuse :",hypotenuse,"degree :",degree)
	if(y>((boardtop-boardbottom)/2)):
		if(x>((boardright-boardleft)/2)):
			print("attack coin at a angle of ",degree,"degree bottomleft side of the coin")
		if(x<=((boardright-boardleft)/2)):
			print("attack coin at a angle of ",degree,"degree bottomright side of the coin")
	elif(y<((boardtop-boardbottom)/2)):
		if(x>((boardright-boardleft)/2)):
			print("attack coin at a angle of ",degree,"degree topleft side of the coin")
			print("or maybe try a backshot the strategy on build")
		if(x<=((boardright-boardleft)/2)):
			print("attack coin at a angle of ",degree,"degree topright side of the coin")
			print("or maybe try a backshot the strategy on build")
		#print("attack coin at a angle of ",degree,"degree below the coin")
	else:
		print("no possible moves can be made to pocket the coin")
else:
	print("coin is straight to the pocket")
	if(x>((boardright-boardleft)/2)):
		if(y>((boardtop-boardbottom)/2) and (x==int(xpocket))):
			print("attack the coin left side of it parallely")
		if(y<((boardtop-boardbottom)/2) and (x==int(xpocket))):
			print("backshot to be attempted as in build")
	if(x<((boardright-boardleft)/2)):
		if(y>((boardtop-boardbottom)/2) and (x==int(xpocket))):
			print("attack the coin right side of it parallely ")
		if(y<((boardtop-boardbottom)/2) and (x==int(xpocket))):
			print("backshot to be attempted as in build")
print("calculating speed")
if(y>((boardtop-boardbottom)/2)):
	print("assuming time is 0.3")
	print("distance :",opposite,"time :",timel,"test distance :",mindis)
	speed=int(opposite)/timel 
	speed1=speed*3779
	speed2=speed/3779
	speed3=3779/speed
	print("speed :",speed)
	print("speed1 :",speed1)
	print("speed2 :",speed2)
	print("speed3 :",speed3)
if(y<((boardtop-boardbottom)/2)):
	print("assuming time is 0.7")
	print("distance :",opposite,"time :",timeh)
	speed=int(opposite)/timeh
	speed1=speed*3779
	speed2=speed/3779
	speed3=3779/speed
	print("speed :",speed)
	print("speed1 :",speed1)
	print("speed2 :",speed2)
	print("speed3 :",speed3)
'''
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''