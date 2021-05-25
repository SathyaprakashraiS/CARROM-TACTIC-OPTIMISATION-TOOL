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
#pockets=["9,0","9,9","0,0","0,9"]
pockets=["1277,186","596,186","1277,864","596,864"]
pocketslope=["0","0","0","0"]
playerpos=["1,1","1,8"]
#boardleft=0 #of y
boardleft=596
#boardright=9#of y
boardright=1277
#boardtop=9 #of x
boardtop=186
#boardbottom=0#of x
boardbottom=864
whitemass=5
blackmass=5
redmass=5
strickermass=5
timel=0.3
timeh=0.7

#boardxmedian=abs((boardright-boardleft)/2)
#boardymedian=abs((boardtop-boardbottom)/2)
boardxmedian=955
boardymedian=517

print("BOARD X MEDIAN :",boardxmedian)
print("BOARD Y MEDIAN :",boardymedian)
lan=[]
print("which coin do you want to pocket ? enter the location of it")
x=int(input("xaxis :"))
y=int(input("yaxis :"))
ssx=int(input("striker lane starting x co-ordinate"))#stricker lan start x coord
lan.append(ssx)
ssy=int(input("stricker lane starting y co-ordinate"))#stricker lan start y coord
lan.append(ssy)
sex=int(input("stricker lane ending x co-ordinate"))#stricker lan end x coord
lan.append(sex)
sey=int(input("stricker lane ending y co-ordinate"))#stricker lan end y coord
lan.append(sey)
#coingraph[x][y]=1
print(x,y)
mindis=9999
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
#COMMENTED FOR TEST PURPOSE
'''
if(slope!=1 and online==0):
	posx,posy=straightline(slope,xpocket,ypocket,x,y)
	print("the position to be moved is :",posx,posy)
	opposite,adjacent,hypotenuse,degree=triangle(x,y,xpocket,ypocket,posx,posy)#qwerty
	print("opposite :",opposite,"adjacent :",adjacent,"hypotenuse :",hypotenuse,"degree :",degree)
	print("opposite :",opposite,"adjacent :",adjacent,"hypotenuse :",hypotenuse,"degree :",degree)
	if(y>boardymedian):
		if(x>boardxmedian):
			print("attack coin at a angle of ",degree,"degree bottomleft side of the coin")
		if(x<=((boardright-boardleft)/2)):
			print("attack coin at a angle of ",degree,"degree bottomright side of the coin")
	elif(y<boardymedian):
		if(x>boardxmedian):
			print("attack coin at a angle of ",degree,"degree topleft side of the coin")
			print("or maybe try a backshot the strategy on build")
		if(x<=boardxmedian):
			print("attack coin at a angle of ",degree,"degree topright side of the coin")
			print("or maybe try a backshot the strategy on build")
	else:
		print("no possible moves can be made to pocket the coin")
else:
	print("coin is straight to the pocket")
	if(x>boardxmedian):
		if(y>boardymedian and (x==int(xpocket))):
			print("attack the coin left side of it parallely")
		if(y<((boardtop-boardbottom)/2) and (x==int(xpocket))):
			print("backshot to be attempted as in build")
	if(x<boardxmedian):
		if(y>boardymedian and (x==int(xpocket))):
			print("attack the coin right side of it parallely ")
		if(y<boardymedian and (x==int(xpocket))):
			print("backshot to be attempted as in build")
'''

if(slope!=1 and online==0):
	posx,posy=straightline(slope,xpocket,ypocket,x,y)
	print("the position to be moved is :",posx,posy)
	opposite,adjacent,hypotenuse,degree=triangle(x,y,xpocket,ypocket,posx,posy)#qwerty
	print("opposite :",opposite,"adjacent :",adjacent,"hypotenuse :",hypotenuse,"degree :",degree)
	print("opposite :",opposite,"adjacent :",adjacent,"hypotenuse :",hypotenuse,"degree :",degree)
	if(y<boardymedian):
		if(x<=boardxmedian):
			print("attack coin at a angle of ",degree,"degree bottomright side of the coin")
		if(x>boardxmedian):
			print("attack coin at a angle of ",degree,"degree bottomleft side of the coin")
	elif(y>boardymedian):
		if(x<=boardxmedian):
			print("attack coin at a angle of ",degree,"degree topright side of the coin")
			print("or maybe try a backshot the strategy on build")
		if(x>boardxmedian):
			print("attack coin at a angle of ",degree,"degree topleft side of the coin")
			print("or maybe try a backshot the strategy on build")
	else:
		print("no possible moves can be made to pocket the coin")
else:
	print("coin is straight to the pocket")
	if(x<boardxmedian):
		if(y<=boardymedian and (x==int(xpocket))):
			print("attack the coin left side of it parallely")
		if(y>((boardtop-boardbottom)/2) and (x==int(xpocket))):
			print("backshot to be attempted as in build")
	if(x>boardxmedian):
		if(y<=boardymedian and (x==int(xpocket))):
			print("attack the coin right side of it parallely ")
		if(y>boardymedian and (x==int(xpocket))):
			print("backshot to be attempted as in build")


print("calculating speed")
if(y>((boardtop-boardbottom)/2)):
	print("assuming time is 0.3")
	print("distance :",opposite,"time :",timel,"test distance :",mindis)
	speed=int(opposite)/timel 
	speed1=speed*3779
	speed2=speed/3779
	speed3=3779/speed
	speed4=(int(opposite)*0.0002645833)/timel
	speed5=((int(opposite)*0.0002645833)*100)/timel
	print("speed :",speed)
	print("speed1 :",speed1)
	print("speed2 :",speed2)
	print("speed3 :",speed3)
	print("speed4 :",speed4)
	print("speed5 :",speed5 ,"cm/s")
if(y<((boardtop-boardbottom)/2)):
	print("assuming time is 0.7")
	print("distance :",opposite,"time :",timeh)
	speed=int(opposite)/timeh
	speed1=speed*3779
	speed2=speed/3779
	speed3=3779/speed
	speed4=(int(opposite)*0.0002645833)/timeh
	speed5=((int(opposite)*0.0002645833)*100)/timeh
	print("speed :",speed)
	print("speed1 :",speed1)
	print("speed2 :",speed2)
	print("speed3 :",speed3)
	print("speed4 :",speed4)
	print("speed5 :",speed5,"cm/s")

sslope=[]
medianlane=(sex-ssx)/2
if(x>medianlane):
	sstartx=medianlane
	temp=sstartx
	send=lan[2]
	for temp in range(send+1):
		sslope.append((abs((x-temp))/abs((y-ssy))))
		#print("")
if(x<=medianlane):
	sstartx=lan[0]
	send=medianlane
	temp=sstartx
	for temp in range(send+1):
		sslope.append((abs((x-temp))/abs((y-ssy))))
		#print("")
maxslope=0
sdist=0
tempsdist=0
temp=ssx
sposx=0
sposy=0
for i in range(len(sslope)):
	if(maxslope<sslope[i]):
		maxslope=sslope[i]
		sdist=math.sqrt(((x-(temp+i))*(x-(temp+i)))+((y-ssy)*(y-ssy)))
		sposx=temp+i
		sposy=ssy
	if(maxslope==sslope[i]):
		tempsdist=math.sqrt(((x-(temp+i))*(x-(temp+i)))+((y-ssy)*(y-ssy)))
		if(tempsdist<sdist):
			maxslope=sslope[i]
			sdist=tempsdist
			sposx=temp+i
			sposy=ssy
		else:
			sdist=math.sqrt(((x-(temp+i))*(x-(temp+i)))+((y-ssy)*(y-ssy)))
print("MAX SLOPE :",maxslope,"DISTANCE BETWEEN STRICKER COIN :",sdist)
print("STRICKER X CO-ORDINATES :",sposx,"STRICKER Y CO-ORDINATES :",sposy)
# 1PIXEL IS 0.0002645833 METER
# 1METER IS 3779 PIXEL 

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