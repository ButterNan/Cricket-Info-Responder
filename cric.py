import nltk	
import sys
from nltk.tree import *
from nltk.corpus import wordnet as wn
from nltk.parse import RecursiveDescentParser
from nltk import Nonterminal, nonterminals, Production, parse_cfg, ContextFreeGrammar


bats1={}          #dictionry for 1st odi match fr both team battng
bats2={}
bats3={}
bats4={}
bats5={}
bowl1={}
bowl3={}
bowl2={}
bowl4={}
bowl5={}
pom=[]

ply1={}
ply2={}
pomt=[]
win=[]
toss=[]
mm=0
match=0      #flag to c whtr its 1st r 2nd match fr new zealand
match1=0
# function to add the contents of file, after proper parsing, to the given dictionary
def parse_for_player(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split('	')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b	

def add_to_dict2(dictionary, fname):
	f = open(fname, 'r')
	l=fname.split('/')
	print l
	l1=l[3].split('_')
	print l1
	x=[]
	for line in f:
			temp = line[:-1]
			temp = temp.split(',')
			a = temp[0]
			c=temp[0:]
			b = temp[1:]
			x.append(c)
	if(l1[1]=='inn1'):
		
		dictionary['0'] = x
	else:
		dictionary['1']=x
	#print dictionary				

def add_to_dict1(dictionary, fname):             #for 2st match for new zealand
	f = open(fname, 'r')
	l=fname.split('/')
	#print l
	l1=l[3].split('_')
	#print l1
	x=[]
	for line in f:
			temp = line[:-1]
			temp = temp.split(',')
			a = temp[0]
			c=temp[0:]
			b = temp[1:]
			x.append(c)
	if(l1[1]=='inn1'):                   #new zealand
		dictionary['0'] = x
		if(l1[0]=='odi1'):
			match=1
		if(l1[0]=='odi2'):
			match=2
		if(l1[0]=='odi3'):
			match=3
		if(l1[0]=='odi4'):
			match=4
		if(l1[0]=='odi5'):
			match=5	
				
	else:
		dictionary['1']=x           #india
		if(l1[0]=='odi1'):
			match1=1
		if(l1[0]=='odi1'):
			match1=2
		if(l1[0]=='odi1'):
			match1=3
		if(l1[0]=='odi1'):
			match1=4	
		if(l1[0]=='odi1'):
			match1=5			
	#print dictionary
		#print match1
def add_to_dict3(dictionary, fname):             #for 2st match for india
	f = open(fname, 'r')
	#print "bowl"
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b	

	#print dictionary		
	
# This function returns a list of variable, corresponding to players who satisfy the criteria : strike rate > 150.0
def parse_for_sr(bat, num):
	toreturn = []
	#print bat
	#print "bat"
	ct=0
	# strike rate is in the 7th column
	for i in range(0,len(bat)):
		
		temp = bat[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[7]
			
			l=float(j)
			
			#print l
			if l > num:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	
	#print "sr"
	#print toreturn		
	return  toreturn
def parse_for_full_wicket(bat):
	toreturn = []
	ct=0
	
	run=0
	r={}
	run1=0
	r1={}
	run2=0
	r2={}
	r3={}
	r4={}
	run3=0
	run4=0
	# strike rate is in the 7th column
	for i in bat:

		temp=bowl1[str(1)]
		for j in temp:
			
			while(ct<len(temp)):
				h=temp[ct]
				if(i==h[0]):
					run=int(h[4])
					r[i]=run
				ct=ct+1
			ct=0	
		temp1=bowl3[str(1)]
		for j in temp1:
			while(ct<len(temp1)):
				h=temp1[ct]
				if(i==h[0]):
					run1=int(h[4])
					r1[i]=run1
				ct=ct+1
			ct=0	
		temp2=bowl4[str(0)]
		for j in temp2:
			while(ct<len(temp2)):
				h=temp2[ct]
				if(i==h[0]):
					run2=int(h[4])
					r2[i]=run2
				ct=ct+1
			ct=0	
		temp3=bowl5[str(1)]
		for j in temp3:
			while(ct<len(temp3)):
				h=temp3[ct]
				if(i==h[0]):
					run3=int(h[4])
					r3[i]=run3
				ct=ct+1
			ct=0			
		temp4=bowl2[str(1)]
		for j in temp4:
			while(ct<len(temp4)):
				h=temp4[ct]
				if(i==h[0]):
					run4=int(h[4])
					r4[i]=run4
				ct=ct+1
			ct=0							
	"""print run		
	print r	
	print "rjhj"
	print r1
	print r2
	print r3
	print r4          #all the right hand players wicket data
	print "sum"
	"""
	sum1=0
	ru={}
	rightlst={}
	run=0
	for i in r:
		run=run+r[i]
	rightlst[1]=run
	run1=0	
	for i in r1:
		run1=run1+r1[i]	
	rightlst[2]=run1
	run2=0
	for i in r2:
		run2=run2+r2[i]	
	rightlst[3]=run2
	
		
	run3=0			
	for i in r3:
		run3=run3+r3[i]	
	rightlst[4]=run3
	
	run4=0			
	for i in r4:
		run4=run4+r4[i]	
	rightlst[5]=run4
				
	print rightlst		
	return rightlst		
	"""for i in r:
		for j in r1:
			if i==j:
			#print r1[i]
				for m in r2:
					if m==i:
						for k in r3:
							if k==i: 
								for h in r4:
									if h==i:
										sum1=sum1+r4[h]+r3[k]+r2[m]+r1[j]+r[i]
										
										print r4[h]
										print r3[k]
										print r2[m]
										print r1[j]
										print r[i]
										
										ru[i]=sum1
			sum1=0				"""		
			

	
	
def parse_for_left_hand(profile,num):
	toreturn = []
	ct=0
	play={}
	m=[]
	# strike rate is in the 7th column
	for i in profile:
		temp = profile[str(i)]
		#print temp[0]
		
		play[i]=temp[0:]
	#print play
	
	toreturn = []
	ct=0
	f=[]
	right={}
	left={}
	# strike rate is in the 7th column
	for i in play:
		temp = play[i]
		
		#print temp
		#f.append(temp.split(' '))
			
		while(ct<len(temp)):
			k = temp[ct]
			#print k
			
			if(ct==6):
				#print i
				#print k
				right[i]=k
			#print j
			if(ct==5):
				left[i]=k
			
			#toreturn[k[0]]=l
			ct=ct+1
		ct=0	
	
	#print right	
	ri={}
	ct=0
	for i in right:
		
		temp=right[i]
		#print temp
		ri[i]=temp.split(' ')
		
		
	#print ri
	ri1={}
	ct=0
	
	for i in ri:
		temp=ri[i]
		g=temp[0]
			
		ri1[i]=g.split('-')
			
		#ri1[i]=temp.split('-')
		
	#print ri1		
	final={}      #list for left
	final1={}       #list for right
	final2={}        #list for none
	for i in ri1:
		temp=ri1[i]
		d=temp[0]
		if(d=='Left'):
			final[i]=d
		elif(d=='Right'):
			final1[i]=d
		else:
			final2[i]=d
	#print final
	#print final1
	#print final2
	return final		
def parse_for_age(profile,num):
	toreturn = []
	ct=0
	play={}
	m=[]
	
	# strike rate is in the 7th column
	for i in profile:
		temp = profile[str(i)]
		#print temp[0]
		
		play[i]=temp[0:]
	#print play
	
	toreturn = []
	ct=0
	f=[]
	age={}
	left={}
	# strike rate is in the 7th column
	for i in play:
		temp = play[i]
		while(ct<len(temp)):
			k = temp[ct]
			if(ct==2):
				age[i]=k
			ct=ct+1
		ct=0	
	#print age
	ri={}	
	for i in age:
		temp=age[i]
		ri[i]=temp.split(' ')
	#print ri	
	final={}
	for i in ri:
		temp=ri[i]
		d=temp[0]
		if(int(d)<num):
			final[i]=int(d)
	#print final	
	
	return final
def parse_for_right_hand(profile,num):
	toreturn = []
	ct=0
	play={}
	m=[]
	# strike rate is in the 7th column
	for i in profile:
		temp = profile[str(i)]
		#print temp[0]du
		
		play[i]=temp[0:]
	#print play
	
	toreturn = []
	ct=0
	f=[]
	right={}
	left={}
	# strike rate is in the 7th column
	for i in play:
		temp = play[i]
		
		#print temp
		#f.append(temp.split(' '))
			
		while(ct<len(temp)):
			k = temp[ct]
			#print k
			
			if(ct==6):
				#print i
				#print k
				right[i]=k
			#print j
			if(ct==5):
				left[i]=k
			
			#toreturn[k[0]]=l
			ct=ct+1
		ct=0	
	
	#print right	
	ri={}
	ct=0
	for i in right:
		
		temp=right[i]
		#print temp
		ri[i]=temp.split(' ')
		
		
	#print ri
	ri1={}
	ct=0
	
	for i in ri:
		temp=ri[i]
		g=temp[0]
			
		ri1[i]=g.split('-')
			
		#ri1[i]=temp.split('-')
		
	#print ri1		
	final={}      #list for left
	final1={}       #list for right
	final2={}        #list for none
	for i in ri1:
		temp=ri1[i]
		d=temp[0]
		if(d=='Left'):
			final[i]=d
		elif(d=='Right'):
			final1[i]=d
		else:
			final2[i]=d
	#print final
	#print final1
	#print final2
	return final1				
	
	
def parse_for_duck1(num):
	toreturn = []
	ct=0
	ct1=0
	print "duck"
	ducklst={}
	lst=[]
	for i in range(0,len(bats1)):
		temp = bats1[str(i)]
		while(ct<len(temp)):
			k = temp[ct]
			j=k[2]
		
			l=int(j)     #runs
			
			if k[0] not in ducklst:
				
				ducklst[k[0]]=l
				
			ct=ct+1
		ct=0		
	ct1=0	
	
	for i in range(0,len(bats5)):
		temp1 = bats5[str(i)]
		while(ct1<len(temp1)):
			k1 = temp1[ct1]
			j1=k1[2]
			l1=int(j1)
			if k1[0] not in ducklst:
				
				lst.append(l1)
				ducklst[k[0]]=lst
				
			else:	
				lst1=[]
				lst1.append(ducklst[k1[0]])
				lst1.append(l1)
				ducklst[k1[0]]=lst1
				
			
									
			ct1=ct1+1
		ct1=0
	ct1=0
	for i in range(0,len(bats3)):
		temp1 = bats3[str(i)]
		while(ct1<len(temp1)):
			k1 = temp1[ct1]
			j1=k1[2]
			l1=int(j1)
			if k1[0] not in ducklst:
				
				lst.append(l1)
				ducklst[k[0]]=lst
			else:	
				lst1=[]
				lst1.append(ducklst[k1[0]])
				lst1.append(l1)
				ducklst[k1[0]]=lst1
				
			ct1=ct1+1
		ct1=0
	ct1=0
	for i in range(0,len(bats2)):
		temp1 = bats2[str(i)]
		while(ct1<len(temp1)):
			k1 = temp1[ct1]
			j1=k1[2]
			l1=int(j1)
			if k1[0] not in ducklst:
				lst.append(l1)
				ducklst[k[0]]=lst
			else:	
				
				lst1=[]
				lst1.append(ducklst[k1[0]])
				lst1.append(l1)
				ducklst[k1[0]]=lst1					
			ct1=ct1+1
		ct1=0
	ct1=0	
	for i in range(0,len(bats4)):
		temp1 = bats4[str(i)]
		while(ct1<len(temp1)):
			k1 = temp1[ct1]
			j1=k1[2]
			l1=int(j1)
			if k1[0] not in ducklst:
				
				lst.append(l1)
				ducklst[k[0]]=lst
				
			else:	
			
				lst1=[]
				lst1.append(ducklst[k1[0]])
				lst1.append(l1)
				ducklst[k1[0]]=lst1		
			ct1=ct1+1
		ct1=0			
							
			
	#print ducklst		
	return  toreturn	
def parse_for_sr1(bat, num ,x):
	toreturn = []
	#print bat
	#print "bat"
	ct=0
	
	
	temp = bat[x]
	
	while(ct<len(temp)):
				
		k = temp[ct]
			#print k
		j=k[7]
			
		l=float(j)
			
			#print l
			#print num
		if l < num:
				#print "l"
			toreturn.append(k[0])
		ct=ct+1
	ct=0	
	#print "sr"
	#print toreturn		
	return  toreturn	
def parse_for_bat(bat, num):
	toreturn1 = []
	
	# score more than 50
	for i2 in bat:
		temp = bat[i2]
		k = int(temp[2])
		if k > num:
			toreturn1.append(i2)
	#print toreturn1
	return  toreturn1
	
def parse_for_bowl(num,bowl):
	toreturn = []

	# atleast 1 wicket
	for i in bowl:
		temp = bowl[i]
		k = int(temp[3])
		if k >= num:
			toreturn.append(i)
	return  toreturn
def parse_for_over(num,bowl):
	toreturn = []
	ct=0
	
	# strike rate is in the 7th column
	for i in range(0,len(bowl)):
		
		temp = bowl[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[1]
			
			l=float(j)
			
			#print l
			if l >= num:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	

	
	return  toreturn
def parse_for_wicket(num,bowl):
	toreturn = []
	ct=0
	#print "wicket"
	# strike rate is in the 7th column
	for i in range(0,len(bowl)):
		
		temp = bowl[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[4]
			
			l=int(j)
			
			#print l
			if l >= num:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	

	#print toreturn		
	return  toreturn
def parse_for_wicket0(num,bowl):
	toreturn = []
	ct=0
	
	# strike rate is in the 7th column
	for i in range(0,len(bowl)):
		
		temp = bowl[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[4]
			
			l=int(j)
			
			#print l
			if l == num:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	

		
	return  toreturn	
def parse_for_economy(num,bowl):
	toreturn = []
	ct=0
	
	# strike rate is in the 7th column
	for i in range(0,len(bowl)):
		
		temp = bowl[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[5]
			
			l=float(j)
			
			#print l
			if l > num:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	

	
	return  toreturn		
# It retrieves the variable names corresponding to players, who have greater  sixes than fours
def parse_for_six(bat, num):
	toreturn  = []

	# number of six hit are in 6th column
	ct=0
	# strike rate is in the 7th column
	for i in range(0,len(bat)):
		
		temp = bat[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[6]
			m=k[5]
			
			six=int(j)
			four=int(m)
			
			#print l
			if six > four:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	
	#print toreturn	
	return toreturn
# It retrieves the variable names corresponding to players, who have greater than 0 sixes
def parse_for_four(bat, num,x):
	toreturn  = []
	ct=0
	
	#print bat
	
	temp = bat[x]
	
	while(ct<len(temp)):
				
		k = temp[ct]
			#print k
		j=k[5]
			
		l=float(j)
			
			#print l
			#print num
		if l > num:
				#print "l"
			toreturn.append(k[0])
		ct=ct+1
	ct=0	
	#print "sr"
	#print toreturn		
	return  toreturn	
	
	# number of six hit are in 6th column
	

# the function to make the model and answer the query, given the properly formatted strings
def make_model_and_answer(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  srate(x) -> gtsix(x) given srate(x) is true"
	
	l = nltk.LogicParser()
	c1 = l.parse(' ((srate(x)) & (srate(x) -> gtsix(x)))')
	varnames =  m.satisfiers(c1, 'x', g)
	#print varnames


	for i in varnames:
		for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
			if q == i:
				print p
def make_model_and_answer3(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  srate(x) -> gtsix(x) given srate(x) is true"
	
	l = nltk.LogicParser()
	c1 = l.parse(' ((srate(x)) & (srate(x) -> gtsix(x)))')
	varnames =  m.satisfiers(c1, 'x', g)
	print varnames


	for i in varnames:
		for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
			if q == i:
				print p
def make_model_and_answer5(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  runs(x) & wicket(x) "
	
	l = nltk.LogicParser()
	c1 = l.parse(' ((bats(x)) & (wicket(x)))')
	varnames =  m.satisfiers(c1, 'x', g)
	print varnames


	for i in varnames:
		for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
			if q == i:
				print p
def query15():
	print "Set B  5->"
	print "1st innings"				
def query4(flag):
	print "Set A 4->"
	
	bats11={}
	bats21={}
	bats31={}
	bats41={}
	bats51={}
	m=1
	x1=0
	x2=0
	x3=0
	x4=0
	x5=0
	
	for i in range(0,len(win)):
		if (win[0]=='New Zealand' and m==1):
			
			bats11[0]=bats1[str(0)]
			x1=0
			m=2
		elif(win[0]=='India' and m==1):
			bats11[1]=bats1[str(1)]	
			x1=1
			m=2
		elif (win[1]=='New Zealand' and m==2):
			bats21[0]=bats2[str(0)]
			x2=0
			m=3
		elif(win[1]=='India' and m==2):
			bats21[1]=bats2[str(1)]	
			x2=1
			m=3
		elif (win[1]=='New Zealand' and m==3):
			bats31[0]=bats3[str(0)]
			x3=0
			m=4
		elif(win[1]=='India' and m==3):
			bats31[1]=bats3[str(1)]	
			x3=1
			m=4

		elif (win[1]=='New Zealand' and m==4):
			bats41[0]=bats4[str(0)]
			x4=0
			m=5
		elif(win[1]=='India' and m==4):
			bats41[1]=bats4[str(1)]	
			x4=1
			m=5

		elif (win[1]=='New Zealand' and m==5):
			bats51[0]=bats5[str(0)]
			m=6
			x5=0
		elif(win[1]=='India' and m==5):
			bats51[1]=bats5[str(1)]	
			m=6
			x5=1
		else:
			break	

	s1 = parse_for_sr1(bats11, 100.0,x1)             #player name for 1st match both innings
	s2 = parse_for_sr1(bats21, 100.0,x2)
	s31 = parse_for_sr1(bats31, 100.0,x3)             #player name for 1st match both innings
	s41 = parse_for_sr1(bats41, 100.0,x4)
	s51 = parse_for_sr1(bats51, 100.0,x5)             #player name for 1st match both innings
	#print s1
	
	#print s2
	s3= parse_for_four(bats11,0,x1)
	s4 = parse_for_four(bats21,0,x2)
	s32= parse_for_four(bats31,0,x3)
	s42 = parse_for_four(bats41,0,x4)
	s52= parse_for_four(bats51,0,x5)
	#print "four"
	
	name_to_var = {}
	name_to_var1 = {}
	count = 0
	l=''
	ct=0
	for i in range(0,len(bats11)):
		temp = bats11[i]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	
	#print "2"	
	#print name_to_var	
	count1=0
	for i in range(0,len(bats21)):
		temp = bats21[i]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats31)):
		temp = bats31[i]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats41)):
		temp = bats41[i]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats51)):
		temp = bats51[i]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
					
	#print "2"	
	#print name_to_var
	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'	
	
	m1=0
	m2=0
	m3=0
	m4=0
	temp_strin2 = 'srate => {'
	for i in s1:
		for j in s2:
			if i==j:
				m1=1
		for k in s31:
			if i==k:
				m2=2
		for l in s41:
			if i==l:
				m3=3
		for m in s51:
			if i==m:
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			#print name_to_var[i]
			temp_strin2 += name_to_var[i] +  ','
		#print name_to_var[i]
		temp_strin2+= name_to_var[i]+','
		m1=0
		m2=0
		m3=0
		m4=0	
	
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#print "battt"
	#print temp_strin2	
	
		
	m1=0
	m2=0
	m3=0
	m4=0
	temp_strin3 = 'four => {'
	for i in s3:
		for j in s4:
			if i==j:
				m1=1
		for k in s32:
			if i==k:
				m2=2
		for l in s42:
			if i==l:
				m3=3
		for m in s52:
			if i==m:
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			temp_strin3 += name_to_var[i] +  ','
		temp_strin3+= name_to_var[i]+','		
		m1=0
		m2=0
		m3=0
		m4=0	

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '}'
	#print "battt"
	#print temp_strin3
	v = temp_strin2 + temp_strin3
	#print v

	# now forming the query
	if(flag==1):
		query = 'all x.(srate(x) & four(x))'
	else:
		query = 'exists x.(srate(x) & four(x))' 
	make_model_and_answer4(v, query, name_to_var)	
		
		
	
def query3(flag):
	print "Set A 3->"
	s1 = parse_for_sr(bats1, 200.0)             #player name for 1st match both innings
	s2 = parse_for_sr(bats2, 200.0)
	s31 = parse_for_sr(bats3, 200.0)             #player name for 1st match both innings
	s41 = parse_for_sr(bats4, 200.0)
	s51 = parse_for_sr(bats5, 200.0)             #player name for 1st match both innings

	s3= parse_for_six(bats1,0)
	s4 = parse_for_six(bats2,0)
	s32= parse_for_six(bats3,0)
	s42 = parse_for_six(bats4,0)
	s52= parse_for_six(bats5,0)
	
	name_to_var = {}
	name_to_var1 = {}
	count = 0
	l=''
	ct=0
	for i in range(0,len(bats1)):
		temp = bats1[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	
	#print "2"	
	#print name_to_var	
	count1=0
	for i in range(0,len(bats2)):
		temp = bats2[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats3)):
		temp = bats3[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats4)):
		temp = bats4[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats5)):
		temp = bats5[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
					
	#print "2"	
	#print name_to_var
	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	#print temp_strin1	
	# this is for the predicate "srate"
	
	m1=0
	m2=0
	m3=0
	m4=0
	temp_strin2 = 'srate => {'
	for i in s1:
		for j in s2:
			if i==j:
				m1=1
		for k in s31:
			if i==k:
				m2=2
		for l in s41:
			if i==l:
				m3=3
		for m in s51:
			if i==m:
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			temp_strin2 += name_to_var[i] +  ','
		m1=0
		m2=0
		m3=0
		m4=0	
	#for i in s2:
	#	temp_strin2 += name_to_var[i] +  ','		
	if(temp_strin2==str(',')):
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#print "kol"
	#print temp_strin2
	m1=0
	m2=0
	m3=0
	m4=0
	#now for the predicate "gtsix"
	temp_strin3 = 'gtsix => {'
	for i in s3:
		for j in s4:
			if i==j:
				m1=1
		for k in s32:
			if i==k:
				m2=2
		for l in s42:
			if i==l:
				m3=3
		for m in s52:
			if i==m:
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			temp_strin3 += name_to_var[i] +  ','
		m1=0
		m2=0
		m3=0
		m4=0	
				
	#for i in s4:
	#	temp_strin3 += name_to_var[i] + ','
	if(temp_strin3==str(',')):
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	#print temp_strin3

	v = temp_strin2 + temp_strin3
	print v

	# now forming the query
	if(flag==1):
		print "k"
		query = 'all x (srate(x) -> gtsix(x))'
	else:
		query = 'exists x (srate(x) -> gtsix(x))'
	make_model_and_answer3(v, query, name_to_var)
def make_model_and_answer6(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  runs(x) & wicket(x) "
	
	l = nltk.LogicParser()
	c1 = l.parse('(bowled(x) & no_wicket(x))')
	varnames =  m.satisfiers(c1, 'x', g)
	print varnames


	for i in varnames:
		for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
			if q == i:
				print p
def make_model_and_answer8(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	
	print "8"
	print val
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  runs(x) & lost(x) "
	
	l = nltk.LogicParser()
	c1 = l.parse('(runs(x) & lost(x))')
	varnames =  m.satisfiers(c1, 'x', g)
	print varnames
	print "the second incide of x denotes the match number"
def make_model_and_answer10(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  right(x) & left(x) "
	
	l = nltk.LogicParser()
	c1 = l.parse('(right(x) & left(x))')
	varnames =  m.satisfiers(c1, 'x', g)
	
						
def make_model_and_answer4(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	
	print val
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "four(x) and srate(x) you can do

	print "Showing the player Names for which  four(x) & srate(x) "
	
	l = nltk.LogicParser()
	c1 = l.parse('(four(x) & srate(x))')
	varnames =  m.satisfiers(c1, 'x', g)
	print varnames
	

					
def make_model_and_answer7(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	#print val	

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "wic(x) & eco(x) you can do

	print "Showing the player Names for which  wic(x) & eco(x) "
	
	l = nltk.LogicParser()
	c1 = l.parse('(wic(x) & eco(x))')
	varnames =  m.satisfiers(c1, 'x', g)
	if ((m.evaluate(query,g))==False):
		print "No"
	else:
		print "Yes"	


				
def make_model_and_answer11(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	#print "The anwer for the query is : ",
	#print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "play1(x) & play2(x) you can do

	#print "Showing the player Names for which  play1(x) & play2(x) "
	
	l = nltk.LogicParser()
	c1 = l.parse('(play1(x) & play2(x))')
	varnames =  m.satisfiers(c1, 'x', g)
	#print varnames


	for i in varnames:
		for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
			if q == i:
				print p			
def query10():
	print "Set A 10->"
	#print ply1
	#print ply2
	s1 = parse_for_right_hand(ply1,1)      #right for nz
	s11 = parse_for_left_hand(ply1,2)      #left for  new zealand
	s2 = parse_for_right_hand(ply2,1)   #right for india
	s21 = parse_for_left_hand(ply2,2)  #left for india
	lst={}       #list for right hand player in nz
	ct=0
	m=0
	m1=0
	m2=0
	m3=0
	m4=0
	ct1=0
	ct2=0
	ct3=0
	ct4=0
	#print bats1
	#print s1
	ctx=0
	lst3={}
	lst5={}
	ctx5=0
	ct5=0
	ctxm=0
	ctm=0
	ctx1=0
	lst1={}
	lstm={}
	print "all right handed players"
	print s1
	for i in s1:
		temp=len(i)
		#print i
		while(ctx<len(i)):
			
			for j in bowl1[str(1)]:
			
				while(ct<len(j)):
					k=j[0]
					if(k==i):
						m=1
						lst[k]=j[1:]
					ct=ct+1
				ct=0	
			ctx=ctx+1
		ctx=0	
		while(ctxm<len(i)):
			
			for jm in bowl2[str(1)]:
			
				while(ctm<len(jm)):
					km=jm[0]
					if(km==i):
						m=1
						lstm[km]=jm[1:]
					ctm=ctm+1
				ctm=0	
			ctxm=ctxm+1
		ctxm=0	
		while(ctx1<len(i)):		
			for j1 in bowl4[str(0)]:
			
				while(ct1<len(j1)):
					k1=j1[0]
					if(k1==i):
						#print j
						m1=1
						lst3[k1]=j1[1:]
					#print k
					ct1=ct1+1
				ct1=0	
			ctx1=ctx1+1
		ctx1=0		
		while(ctx5<len(i)):		
			for j5 in bowl5[str(1)]:
			
				while(ct5<len(j5)):
					k5=j5[0]
					if(k5==i):
						#print j
						m5=1
						lst5[k5]=j5[1:]
					#print k
					ct5=ct5+1
				ct5=0	
			ctx5=ctx5+1
		ctx5=0		
		while(ctx1<len(i)):		
			for j1 in bowl3[str(1)]:
			
				while(ct1<len(j1)):
					k1=j1[0]
					if(k1==i):
						#print j
						m1=1
						lst1[k1]=j1[1:]
					#print k
					ct1=ct1+1
				ct1=0	
			ctx1=ctx1+1
		ctx1=0		
	#print bowl3	
	#print lst
	#print lst1
	#print lstm
	#print lst3
	
	kl={}
	
	
	for i in lst1:
		#print i
		for j in lst:
			if i==j:
				
				m1=1
		for k in lst5:
			if i==k:
				#print k
				m2=2
		for l in lstm:
			if i==l:
				#print l
				m3=3
		for m in lst3:
			if i==m:
				#print m
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			kl[i]=lst1[i]
			
			#kl[b]=
	#print "list of all right handed players who play all the matches	"		
	#print kl	
		
	lsta={}
	lstb={}
	lstc={}
	lstd={}
	lste={}		
	
	print "all left hand players left"
	print s11
	for i in s11:
		while(ctx<len(i)):
			
			for j in bowl1[str(1)]:
			
				while(ct<len(j)):
					k=j[0]
					if(k==i):
						m=1
						lsta[k]=j[1:]
					ct=ct+1
				ct=0	
			ctx=ctx+1
		ctx=0	
		while(ctxm<len(i)):
			
			for jm in bowl2[str(1)]:
			
				while(ctm<len(jm)):
					km=jm[0]
					if(km==i):
						m=1
						lstb[km]=jm[1:]
					ctm=ctm+1
				ctm=0	
			ctxm=ctxm+1
		ctxm=0	
		while(ctx1<len(i)):		
			for j1 in bowl4[str(0)]:
			
				while(ct1<len(j1)):
					k1=j1[0]
					if(k1==i):
						#print j
						m1=1
						lstc[k1]=j1[1:]
					#print k
					ct1=ct1+1
				ct1=0	
			ctx1=ctx1+1
		ctx1=0		
		while(ctx5<len(i)):		
			for j5 in bowl5[str(1)]:
			
				while(ct5<len(j5)):
					k5=j5[0]
					if(k5==i):
						#print j
						m5=1
						lstd[k5]=j5[1:]
					#print k
					ct5=ct5+1
				ct5=0	
			ctx5=ctx5+1
		ctx5=0		
		while(ctx1<len(i)):		
			for j1 in bowl3[str(1)]:
			
				while(ct1<len(j1)):
					k1=j1[0]
					if(k1==i):
						#print j
						m1=1
						lste[k1]=j1[1:]
					#print k
					ct1=ct1+1
				ct1=0	
			ctx1=ctx1+1
		ctx1=0		
	
	"""print lsta
	print lstb
	print lstc
	print lstd
	print lste"""
	kl1={}
	m1=0
	m2=0
	m3=0
	m4=0
	m5=0
	
	#print bats5
	for i in lsta:
		#print i
		for j in lstb:
			if i==j:
				
				m1=1
		for k in lstc:
			if i==k:
				#print k
				m2=2
		for l in lstd:
			if i==l:
				#print l
				m3=3
		for m in lste:
			if i==m:
				
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			kl1[i]=lsta[i]
			
	#print "list of all left handed players who play all the matches	"	
			
	#print kl1 
	s1=parse_for_full_wicket(s1)	#for righthand for wicket sum
	s2=parse_for_full_wicket(s2)    #for left hand bowlers
	#print s1
	#print s2
	#s2['KS Williamson']=2
	#print s2
	
	name_to_var={}
	count=0
	for i in range(0,len(bats1)):
		temp = bats1[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
		
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	

	count=0
	for i in range(0,len(bats2)):
		temp = bats2[str(i)]
		
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
		
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	count=0
	for i in range(0,len(bats3)):
		temp = bats3[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats4)):
		temp = bats4[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bats5)):
		temp = bats5[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	#print name_to_var			
	count=0	
	lst1={}
	temp_strin2 = 'right => {'
	for i in s1:
		for j in s2:
			if i==j and s1[i]>s2[j]:
				
				temp_strin2 += str(count) + ','
		count=count+1		
	
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	print temp_strin2
	count=0
	lst={}
	temp_strin3 = 'left => {'
	for i in s1:
		for j in s2:
			if i==j and s1[i]>s2[j]:
					temp_strin3 += str(count) + ','
		count=count+1
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'
	print temp_strin3
	v =   temp_strin2+temp_strin3
	query = '(all x.(right(x) & left(x)))'

	make_model_and_answer10(v, query, name_to_var)	
										
def query8(flag):
	print "Set A 8->"
	s1 = parse_for_hundred(bats1,100)             #player name for 1st match both innings
	s2 = parse_for_hundred(bats2,100)
	s31 = parse_for_hundred(bats3,100)
	s41 = parse_for_hundred(bats4,100)
	s51 = parse_for_hundred(bats5,100)
	s3 = win             #record of winning team of all matches
	print "hho"
	f={}
	f[0]=s1
	f[1]=s2
	f[2]=s31
	f[3]=s41
	f[4]=s51
	
	ct=0
	name_to_vars=[]
	for i in range(0,len(bats1)):
		temp=bats1[str(i)]
		#print temp
		while(ct<len(temp)):
			n=temp[ct]
			name=n[0]
			#print name
			if name in f[0]:
				#print "r"
				#print name
				#print "k"
				name_to_vars.append('x'+str(i)+str(0))
				match=0
			ct=ct+1
		ct=0	
	for i in range(0,len(bats2)):
		temp=bats2[str(i)]
		#print temp
		while(ct<len(temp)):
			n=temp[ct]
			name=n[0]
			#print name			
			if name in f[1]:
				#print "r"
				#print name
				name_to_vars.append('x'+str(i)+str(1))
				#print "k"
				match=0
			ct=ct+1
		ct=0	
				
	for i in range(0,len(bats3)):
		temp=bats3[str(i)]
		#print temp
		while(ct<len(temp)):
			n=temp[ct]
			name=n[0]
			#print name			
			if name in f[2]:
				#print "r"
				#print name
				name_to_vars.append('x'+str(i)+str(2))
				#print "k"
				match=0
			ct=ct+1
		ct=0		
				
	for i in range(0,len(bats4)):
		temp=bats4[str(i)]
		#print temp
		while(ct<len(temp)):
			n=temp[ct]
			name=n[0]
			#print name			
			if name in f[3]:
				#print "r"
				#print name
				name_to_vars.append('x'+str(i)+str(3))
				#print "k"
				match=0		
			ct=ct+1	
		ct=0	
	for i in range(0,len(bats5)):
		temp=bats5[str(i)]
		#print temp
		while(ct<len(temp)):
			n=temp[ct]
			name=n[0]
			#print name			
			if name in f[4]:
				#print "r"
				#print name
				name_to_vars.append('x'+str(i)+str(4))
				#print "k"
				match=0		
			ct=ct+1	
		ct=0		
	#print name_to_vars	
			
			
	name_to_var = {}
	name_to_cty = {}
	count = 0
	c=0
	
	
	temp_strin2 = 'runs => {'
	for i in name_to_vars:
		temp_strin2 += i + ','
		
	if(temp_strin2==str(',')):
		temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
	temp_strin2 += '} \n'
	#print "22"
	print temp_strin2
			
	
	
	cx=0
	temp_strin3 = 'lost => {'
	for i in s3:
		
		if(i=='Match Tied'):
			temp_strin3 += 'x' + str(0) + ','
		elif(i=='New Zealand'):
			temp_strin3 += 'x' + str(1)+ str(cx)+','	
		else:		
			temp_strin3 += 'x'+str(0) + str(cx) + ','
		cx=cx+1	
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	#print "33"
	print temp_strin3
	v =   temp_strin2+temp_strin3
	#print v	

	# now forming the query
	if(flag==0):
		query = '(exists x.(runs(x) & lost(x)))'
	else:
		query = '(all x.(runs(x) & lost(x)))'
	make_model_and_answer8(v, query, name_to_var)	
def query12():
	
	print "Set B 2->Did Ishant Sharma bowl more wide than jadega"
	ct=0
	sharma=[]
	jadega=[]
	for i in range(0,len(bowl1)):
		temp=bowl1[str(i)]
		
		while(ct<len(temp)):
			k = temp[ct]
			
			j=k[0]
			
			if j=='I Sharma':
				sharma.append(k[4])
			if j=='RA Jadeja':
				jadega.append(k[4])
			
			
			ct=ct+1			
	ct=0	
	
	for i in range(0,len(bowl3)):
		temp=bowl3[str(i)]
		
		while(ct<len(temp)):
			
			k = temp[ct]
		
			j=k[0]
			if j=='I Sharma':
				sharma.append(k[4])
				
			if j=='RA Jadeja':
				jadega.append(k[4])
				
			#print j
			
			ct=ct+1			
	ct=0	
	fl=0
	
	
	for i in range(0,len(jadega)):
		for j in range(0,len(sharma)):
				
			if (sharma[j]>jadega[i]):
				print "Yes"
				fl=1
				break
			else:
				print "No"	
		if(fl==1):
			break		
def query17():
	print "Set B 7->Is Ishant Sharma a better bowler than jadega"
	ct=0
	
	l=[]
	l1=[]
	s={}
	s1={}
	l11=[]
	l12=[]
	for i in range(0,len(bowl1)):
		temp=bowl1[str(i)]
		
		while(ct<len(temp)):
			k = temp[ct]
			
			j=k[0]
			
			if j=='I Sharma':
				
				l.append(k[4])
				l.append(k[5])
				
				s[j]=l
				
			if j=='RA Jadeja':
				
				l1.append(k[4])
				l1.append(k[5])
				
				s[j]=l1
				
			
			
			ct=ct+1			
	ct=0	
	
	for i in range(0,len(bowl3)):
		temp=bowl3[str(i)]
		
		while(ct<len(temp)):
			
			k = temp[ct]
		
			j=k[0]
			if j=='I Sharma':
				l11.append(k[4])
				l11.append(k[5])
				
				s1[j]=l11

			if j=='RA Jadeja':
				l12.append(k[4])
				l12.append(k[5])
				
				s1[j]=l12
				
			#print j
			
			ct=ct+1			
	ct=0	
	
	
	econ2=0.0
	econ1=0.0
	wic2=0
	wic1=0
	econ3=0.0
	econ4=0.0
	wic3=0
	wic4=0
	sum1=[]
	sum2=[]
	
	for i in s:
		temp=s[str(i)]
		#print temp
		if i=='RA Jadeja':
			#print temp[1]
			econ1=float(temp[1])*0.5
			wic1=float(temp[0])*15
			sum1.append(econ1+wic1)
		if i=='I Sharma':
			econ2=float(temp[1])*0.5
			wic2=float(temp[0])*15
			sum2.append(econ2+wic2)
			
	for i in s1:
		temp=s1[str(i)]
		#print temp
		if i=='RA Jadeja':
			#print temp[1]
			econ3=float(temp[1])*0.5
			wic3=float(temp[0])*15
			sum1.append(econ3+wic3)
		if i=='I Sharma':
			econ4=float(temp[1])*0.5
			wic4=float(temp[0])*15
			sum2.append(econ4+wic4)		
	
	count=0
	for i in range(0,min(len(sum1),len(sum2))):
		if(sum1[i]<sum2[i]):
			
			count=count+1
			
	if(count>=1):
		print "Yes"
	else:
		print "No"	
	"""
	for i in range(0,len(jadegae)):
		for j in range(0,len(sharmae)):
				
			if (sharmae[j]<jadegae[i]):
				
				fl=1
				break
			else:
				fl=0
		if(fl==1):
			fl=2
			
	if(fl==2):
		for i in range(0,sharmaw):
			for j in range(0,jadegaw):
				if(sharmaw[i]>jadegaw[j]):
					print
	"""
def query20():
	print "Set B 10->Predict the outcome of the next Match"
	ct=0
	run=0
	r={}
	for i in range(0,len(bats1)):
		temp=bats1[str(i)]
		while(ct<len(temp)):
			k = temp[ct]
			j=k[0]
			run=run+int(k[2])
			
			ct=ct+1	
		r[i]=run
		run=0	
		ct=0
		
		nz=0
		ind=0
	for i in range(0,len(r)-1):
		if(r[i]>r[i+1]):
			nz=r[i]-r[i+1]
		else:
			ind=r[i+1]-r[i]	
	
	wic=0
	ct=0	
	r1={}
	for i in range(0,len(bowl1)):
		temp=bowl1[str(i)]
		while(ct<len(temp)):
			k = temp[ct]
			j=k[0]
			wic=wic+int(k[4])
			
			ct=ct+1
		if i==0:		
			r1[1]=wic
		else:
			r1[0]=wic	
		wic=0	
		ct=0
		
	nz1=0
	ind1=0
	run=0
	run1=0
	for i in range(0,len(r1)-1):
		if(r1[i]>r1[i+1]):
			nz1=(r1[i]-r1[i+1])*25
		else:
			ind1=(r1[i+1]-r1[i])*25	

		
	if ind>nz:
		run=run+ind
		run1=run1-nz
	else:
		run1=run1+nz
		run=run-ind	
	if ind1>nz1:
		
		run=-(run-ind1)
	else:
		run=run+ind1
		run1=run1+nz1
	
	tot=0
	tot=run-(run1)
	print tot
	if(tot>0):
		print "India Wins"
	else:
		print "New Zealand Wins"	 
def query16():
	print "Set B 6->Prove that Dhoni is a hard hitting battsman"
	ct=0
	temp=bats1[str(1)]
	six=0
	four=0
	run=0
	runs=0
	runf=0
	tot=0
	per=0.0
	while(ct<len(temp)):
		k = temp[ct]
		j=k[0]
		if j=='MS Dhoni':
			six=int(k[6])
			four=int(k[5])
			run=int(k[2])
			runs=six*6
			runf=four*4
			tot=runf+runs
			per=float(tot)/float(run)
			
		ct=ct+1	
	perc=per*100
	if(perc>50):
		print "Yes"
	else:
		print "No"	 
def query19():
	print "Set B 9->Do the teams that win matches win the toss too?"
	ct=win		
	ct1=toss	
	print ct1	
	print ct
	flg=0	
	for i in range(0,5):
		if(ct[i]==ct1[i]):
			flg=1
		
	if(flg==1):
		print "Yes"
	else:
		print "No"			
def query18():
	print "Set B 8->Do  the  middle  order  batsmen  perform  better  than  the  opening  batsmen  in  general  ?"
	ct=0
	first={}
	l1=[]
	l2=[]
	l3=[]
	ct1=0	
	for i in range(0,len(bats1)):
		temp = bats1[str(i)]
		#print temp
		while(ct1<len(temp)):
			k = temp[ct1]
			#print k
			j=k[0]
			if(ct1<2):
				l1.append(j)
			elif(ct1>1 and ct1<6):
				l2.append(j)
			else:
				l3.append(j)		
			#print j
			ct1=ct1+1
		ct1=0	
	#print first		
	"""print l1
	print "l1"
	print l2
	print "l2"
	"""
	
	l11=[]
	l21=[]
	l31=[]
	for i in range(0,len(bats2)):
		temp = bats2[str(i)]
		#print temp
		while(ct1<len(temp)):
			k = temp[ct1]
			#print k
			j=k[0]
			if(ct1<2):
				l11.append(j)
			elif(ct1>1 and ct1<6):
				l21.append(j)
			else:
				l31.append(j)		
			#print j
			ct1=ct1+1
		ct1=0	
	#print first		
	"""print l11
	print "l11"
	print l21
	print "l12"
	
	ct=0
	print "hail"
	"""
	ct=0
	run=0
	sum1=0		      #for 2nd match for openging batsman for nl
	sum2=0
	sum3=0      #for 2nd match for openging batsman for nl
	sum4=0		#for 2nd match for middle batsman for nl
	ct1=0
	sum11=0    #for 1st match for openg for india
	sum12=0
	sum31=0
	sum41=0
	for i in range(0,len(bats1)):
		temp=bats1[str(i)]
		
		while(ct<len(temp)):
			h=temp[ct]
			name=h[0]
			run=h[2]
			ct=ct+1
			#print run
			#print name
			if(name == l1[0] or name==l1[1]):
				#print name
				#print "name for openings 1st match nz"
				#print h[2]
				sum1=int(run)+sum1
				#print sum1
			if(name == l2[0] or name==l2[1] or name==l2[2] or name==l2[3]):
				#print name
				sum2=int(run)+sum2	
				#print sum2
			if(name == l1[2] or name==l1[3]):
				sum11=int(run)+sum11
			if(name == l2[4] or name==l2[5] or name==l2[6] or name==l2[7]):
				sum12=int(run)+sum12
		ct=0		
		temp1=bats2[str(i)]
		
		while(ct1<len(temp1)):
			h1=temp1[ct1]
			name1=h1[0]
			run1=h1[2]
			ct1=ct1+1
			if(name1 == l11[0] or name1==l11[1]):
				sum3=int(run1)+sum3
			if(name1 == l21[0] or name1==l21[1] or name1==l21[2] or name1==l21[3]):
			
				sum4=int(run1)+sum4	
			if(name1 == l11[2] or name1==l11[3]):
				sum31=int(run1)+sum31
			if(name1 == l21[4] or name1==l21[5] or name1==l21[6] or name1==l21[7]):
				sum41=int(run1)+sum41		
				
		ct1=0	
	#print sum3    #for 2nd match nl opengng 
	#print sum4          #for 2nd match nl middle
	#print sum31			#for 2nd match india openg
	#print sum41			#for 2nd match india middle
	#print sum1		#for 1st match nl opengng 
	#print sum2			#for 1st match nl middle
	#print sum11		#for 1st match india openg
	#print sum12		#for 1st match india middle
	avgnlo1=float(sum1/2)
	
	avgnlm1=float(sum2/4)
	avgio1=float(sum11/2)
	avgim1=float(sum12/4)
	avgnlo2=float(sum3/2)
	avgnlm2=float(sum4/4)
	avgio2=float(sum31/2)
	avgim2=float(sum41/4)
	"""print "kk"
	print avgnlo1
	print avgio1
	print avgnlm1
	print avgim1"""
	if((avgnlo1+avgio1)<(avgnlm1+avgim1)):
		print "yes"
	else:
		print "No"	
		
def query13():
	ct=0
	g=[]
	ls={}
	print "Set B 3->Did Southe caught more than ryder"
	for i in range(0,len(bats1)):
		temp=bats1[str(i)]
		print len(temp)
		while(ct<len(temp)):
			k = temp[ct]
			
			j=k[1]
			print j
			
			for i in range(0,len(j)):
				ls[i]=j.split(' ')
		
			
				#print h
			
			ct=ct+1		
		ct=0		
			
	#print g
	print "kgjhxxc"
	print ls
	for i in range(0,len(g)):
		temp=g[i]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
		
			
			#print j
			
			ct=ct+1			
	ct=0				
			

			
def query14(bats,bowl):
	print "set B 4->Is there a player who is man of the match twice?"
	
	for i in range(0,(len(pomt)-1)):
	
		
		for j in range(i+1,len(pomt)):
			if pomt[i]==pomt[j]:
				print "Yes"
				break
	print pomt[i]
def query11(bats,bowl):
	name_to_var = {}
	name_to_var1 = {}
	print "set B 1->Who are the  players who  played for all the matches in the series?"
	count = 0
	l=''
	ct=0
	first=[]
	for i in range(0,len(bats1)):
		temp = bats1[str(i)]
	
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			first.append(j)
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				
				count +=1
			ct=ct+1
		ct=0
	#print "first"	
	#print first	
	first1=[]
	ct1=0	
	for i in range(0,len(bats2)):
		temp = bats2[str(i)]
		#print temp
		while(ct1<len(temp)):
			k = temp[ct1]
			#print k
			j=k[0]
			#print j
			first1.append(j)	
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
			
				count +=1
			ct1=ct1+1
		ct1=0	
	#print "first1"
	#print first1	
	#print name_to_var	
	
	temp_strin2 = 'play1 => {'
	for i in first:
		temp_strin2 += name_to_var[i] +  ','		

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#print "battt"
	#print temp_strin2
	
	temp_strin3 = 'play2 => {'
	for i in first1:
		temp_strin3 += name_to_var[i] +  ','		

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," character
	temp_strin3 += '} \n'
	#print "battt11"
	#print temp_strin3
	v = temp_strin2 + temp_strin3
	#print v

	# now forming the query
	query = '(all x.(play1(x) & play2(x)))'

	make_model_and_answer11(v, query, name_to_var)	
def query9(flag):
	print "Set A 9->"
	s1 = parse_for_duck1(0)             #player name for 1st match both innings

	print "s1"
	
	s2=parse_for_age(ply1,26)     #all player greate than 26 yrs
	s3=parse_for_age(ply2,26)     #all player greater than s6 india
	print "age less than 26 new zealand"
	print s2
	print "age less than 26 india"
	print s3
	
	ct=0
	ct1=0
	run=0
	run1=0
	runlst={}

	for i in range(0,len(bats1)):
		
		temp = bats1[str(i)]
		while(ct<len(temp)):
			k = temp[ct]
			name=k[0]
			j=k[2]
			l=int(j)
			if name not in runlst:
				runlst[name]=l
			else:
				runlst[name]=l+runlst[name]
			ct=ct+1
		ct=0
	
	for i in range(0,len(bats5)):
		temp1 = bats5[str(i)]
		while(ct1<len(temp1)):
			k1 = temp1[ct1]
			j1=k1[2]
			name1=k1[0]
			l1=int(j1)
			
			if name1 not in runlst:
				runlst[name1]=l1
			else:
				runlst[name1]=l1+runlst[name1]
			ct1=ct1+1
		ct1=0	
	ct1=0	
	for i in range(0,len(bats4)):
		temp1 = bats4[str(i)]
		while(ct1<len(temp1)):
			k1 = temp1[ct1]
			j1=k1[2]
			name1=k1[0]
			l1=int(j1)
			
			if name1 not in runlst:
				runlst[name1]=l1
			else:
				runlst[name1]=l1+runlst[name1]
			ct1=ct1+1
		ct1=0	
	ct1=0	
	for i in range(0,len(bats3)):
		temp1 = bats3[str(i)]
		while(ct1<len(temp1)):
			k1 = temp1[ct1]
			j1=k1[2]
			name1=k1[0]
			l1=int(j1)
			
			if name1 not in runlst:
				runlst[name1]=l1
			else:
				runlst[name1]=l1+runlst[name1]
			ct1=ct1+1
		ct1=0	
	ct2=0	
	for i in range(0,len(bats2)):
		temp2 = bats2[str(i)]
		while(ct2<len(temp2)):
			k2 = temp2[ct2]
			j2=k2[2]
			name2=k2[0]
			l2=int(j2)
			
			if name2 not in runlst:
				runlst[name2]=l2
			else:
				runlst[name2]=l2+runlst[name2]
			ct2=ct2+1
		ct2=0				
					
	print "run"
	print runlst	
	if(flag==0):
		print "True"
	else:
		print "False"
	"""for i in range(0,len(bats1)):
		temp=bats1[str(i)]
	for i in range(0,len(bats2)):
		temp1=bats2[str(i)]
	for i in range(0,len(bats3)):
		temp2=bats3[str(i)]
	for i in range(0,len(bats4)):
		temp3=bats4[str(i)]
	for i in range(0,len(bats5)):
		temp4=bats5[str(i)]
	print temp	
	print temp1		
	ct=0
	ct1=0
	play={}
	m=[]
	for i in temp:
		while(ct<len(temp)):
			k = temp[ct]
		
			j=k[0]
		for i in temp1:
			while(ct1<len(temp1)):
				k1=temp1[ct1]
					
				j1=k1[0]
				if(j==j1):
						#print j1
						#print j
					m.append(k[1:])
					m.append(k1[1:])
					play[j]=m	
					break
				ct1=ct1+1
			ct1=0	
		ct=ct+1		
	ct=0	
	#print play		
	"""			
	
def query7():
	print "Set A 7->"
	s1 = parse_for_wicket0(0,bowl1)
	s3 = parse_for_wicket0(0,bowl3)
	s2 = parse_for_wicket0(0,bowl2)
	s4 = parse_for_wicket0(0,bowl4)
	s5 = parse_for_wicket0(0,bowl5)
	
	se1 = parse_for_economy(8.0,bowl1)
	se3= parse_for_economy(8.0,bowl3)
	se2 = parse_for_economy(8.0,bowl2)
	se4= parse_for_economy(8.0,bowl4)
	se5 = parse_for_economy(8.0,bowl5)
	
	
	m={}
	for i in range(0,5):
		if(i==0):
			m[i]=s1
		elif(i==1):
			m[i]=s2
		elif(i==2):
			m[i]=s3
		elif(i==3):
			m[i]=s4
		else:
			m[i]=s5

	m1={}
	for i in range(0,5):
		if(i==0):
			m1[i]=se1
		elif(i==1):
			m1[i]=se2
		elif(i==2):
			m1[i]=se3
		elif(i==3):
			m1[i]=se4
		else:
			m1[i]=se5
	
	name_to_var={}
	count=0
	for i in m:
		temp=m[i]
		#print temp
		if(len(temp)!=0):
			if i not in name_to_var:
				name_to_var[i] = 'r' + str(count)
			count += 1					
	
	name_to_var1={}
	count=0
	
	for i in m1:
		temp=m1[i]
		#print temp
		if(len(temp)!=0):
			#print i
			name_to_var1[i] = 'r' + str(count)
				
		count += 1					
	
	temp_strin3 = 'wic => {'
	for i in name_to_var:
		temp_strin3 += name_to_var[i] + ','

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'+ '\n'
	#print temp_strin3
	
	temp_strin2 = 'eco => {'
	for i in name_to_var1:
		temp_strin2 += name_to_var1[i] + ','

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," charater
	temp_strin2 += '}'
	#print temp_strin2

	v = temp_strin3  + temp_strin2
	#print v

	# now forming the query
	query = '(exists x.(wic(x) & eco(x)))'

	make_model_and_answer7(v, query, name_to_var)

	
	
def query6(flag):
	print "sSet A 6->"
	s1 = parse_for_over(7,bowl1)             #player name for 1st match both innings
	s2 = parse_for_over(7,bowl3)
	s31 = parse_for_over(7,bowl2)             #player name for 1st match both innings
	s41 = parse_for_over(7,bowl4)
		
	s51 = parse_for_over(7,bowl5)
	
	
	s3 = parse_for_wicket0(0,bowl1)
	s4 = parse_for_wicket0(0,bowl3)
	s32 = parse_for_wicket0(0,bowl2)
	s42 = parse_for_wicket0(0,bowl4)
	s52 = parse_for_wicket0(0,bowl5)


	name_to_var = {}
	name_to_var1 = {}
	count = 0
	l=''
	ct=0
	
	for i in range(0,len(bowl1)):
		temp = bowl1[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	
	#print "2"	
	for i in range(0,len(bowl2)):
		temp = bowl2[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0
	for i in range(0,len(bowl3)):
		temp = bowl3[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	for i in range(0,len(bowl4)):
		temp = bowl4[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0			
	
	
	for i in range(0,len(bowl5)):
		temp = bowl5[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	
	#print name_to_var
	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	
	#print temp_strin1	
	# this is for the predicate "srate"
	#print temp_strin1
	m1=0
	m2=0
	m3=0
	m4=0
	temp_strin2 = 'bowled => {'
	for i in s1:
		for j in s2:
			if i==j:
				m1=1
		for k in s31:
			if i==k:
				m2=2
		for l in s41:
			if i==l:
				m3=3
		for m in s51:
			if i==m:
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			temp_strin2 += name_to_var[i] +  ','
		m1=0
		m2=0
		m3=0
		m4=0	

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#print "battt"
	print temp_strin2
	
	
	
	#print s3
	#print s4
	#now for the predicate "gtsix"
	m1=0
	m2=0
	m3=0
	m4=0
	
	temp_strin3 = 'no_wicket => {'
	for i in s3:
		for j in s4:
			if i==j:
				m1=1
		for k in s32:
			if i==k:
				m2=2
		for l in s42:
			if i==l:
				m3=3
		for m in s52:
			if i==m:
				m4=4
		if(m1==1 and m2==2 and m3==3 and m4==4):
			temp_strin2 += name_to_var[i] +  ','
		m1=0
		m2=0
		m3=0
		m4=0	
		
				
	#for i in s4:
	#	temp_strin3 += name_to_var[i] + ','
	if(temp_strin3==str(',')):
		temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	#print "no wic"
	print temp_strin3

	v = temp_strin1 + temp_strin2 + temp_strin3
	print "check"
	#print v

	# now forming the query
	if(flag==1):
		query = '(exists x.(bowled(x) & no_wicket(x)))'
	else:
		query = '(all x.(bowled(x) & no_wicket(x)))'
	make_model_and_answer6(v, query, name_to_var)	
def query5():
	print "Set A 5->"
	s1 = parse_for_run(bats1, 50.0)             #player name for 1st match both innings
	s2 = parse_for_run(bats2, 50.0)
	s31 = parse_for_run(bats3, 50.0)             #player name for 1st match both innings
	s41 = parse_for_run(bats4, 50.0)
	s51 = parse_for_run(bats5, 50.0)             #player name for 1st match both innings
	
	s3 = parse_for_wicket(1,bowl1)
	s4 = parse_for_wicket(1,bowl3)
	s32 = parse_for_wicket(1,bowl2)
	s42 = parse_for_wicket(1,bowl4)
	s52 = parse_for_wicket(1,bowl5)
	
	name_to_var = {}
	name_to_var1 = {}
	count = 0
	l=''
	ct=0
	for i in range(0,len(bats1)):
		temp = bats1[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	
	#print "2"	
	#print name_to_var	
	ct=0
	for i in range(0,len(bats2)):
		temp = bats2[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0	
	for i in range(0,len(bats3)):
		temp = bats3[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0	
	for i in range(0,len(bats4)):
		temp = bats4[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0	
	for i in range(0,len(bats5)):
		temp = bats5[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0			
	#print "3"	
	#print name_to_var
	ct=0
	for i in range(0,len(bowl1)):
		temp = bowl1[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' + str(count)
				count +=1
			ct=ct+1
		ct=0
	
	#print "2"	
	#print name_to_var	
	ct=0
	for i in range(0,len(bowl3)):
		temp = bowl3[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0	
	for i in range(0,len(bowl2)):
		temp = bowl2[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0	
	for i in range(0,len(bowl4)):
		temp = bowl4[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0
	ct=0	
	for i in range(0,len(bowl5)):
		temp = bowl5[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			
			j=k[0]
			#print j
			if j not in name_to_var:
				name_to_var[j] = 'r' +str(count)
				count +=1
			ct=ct+1
		ct=0		
	
	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	#print temp_strin1	
	# this is for the predicate "srate"
	#print temp_strin1
	temp_strin2 = 'bats => {'
	for i in s1:
		temp_strin2 += name_to_var[i] +  ','
	for i in s2:
		temp_strin2 += name_to_var[i] +  ','
	for i in s31:
		temp_strin2 += name_to_var[i] +  ','
	for i in s41:
		temp_strin2 += name_to_var[i] +  ','
	for i in s51:
		temp_strin2 += name_to_var[i] +  ','					

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#print "battt"
	#print temp_strin2
	
	
	
	#print s3
	#print s4
	#now for the predicate "gtsix"
	temp_strin3 = 'wicket => {'
	for i in s3:
		temp_strin3 += name_to_var[i] + ','
	for i in s4:
		temp_strin3 += name_to_var[i] + ','
	for i in s32:
		temp_strin3 += name_to_var[i] + ','
	for i in s42:
		temp_strin3 += name_to_var[i] + ','
	for i in s52:
		temp_strin3 += name_to_var[i] + ','			
	#for i in s4:
	#	temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	#print "wic"
	#print temp_strin3

	v = temp_strin1 + temp_strin2 + temp_strin3
	#print v

	# now forming the query
	query = 'exists x.(bats(x) & wicket(x))'

	make_model_and_answer5(v, query, name_to_var)
def parse_for_run_over(bat,num):
	toreturn  = []
	x=0
	m1=0
	# number of runs and overs
	for i in bat:
		temp = bat[i]
		k = int(temp[1])      #runs
		x=x+k
		m = int(temp[3])
		m1=m1+m  #add all over
	g=x/m1
	if g > num:
		toreturn.append(i)
	print "kj"	
	print x
	print "g"
	print g		
	print "m1"
	print m1
	return toreturn
def parse_for_hundred(bat,num):
	toreturn  = []
	ct=0

	# strike rate is in the 7th column
	for i in range(0,len(bat)):
		
		temp = bat[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[2]
			
			l=int(j)
			
			#print l
			if l == num:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	

	#print toreturn		
	return  toreturn	
def parse_for_run(bat,num):
	toreturn  = []
	ct=0
	#print "run"
	# strike rate is in the 7th column
	for i in range(0,len(bat)):
		
		temp = bat[str(i)]
		#print temp
		while(ct<len(temp)):
			
			k = temp[ct]
			#print k
			j=k[2]
			
			l=int(j)
			
			#print l
			if l > num:
				toreturn.append(k[0])
			ct=ct+1
		ct=0	

	#print toreturn		
	return  toreturn
	# 100 runs
				
"""def parse_for_duck(bat,num):
	toreturn  = []

	# number of ducks
	for i in bat:
		temp = bat[i]
		k = int(temp[1])
		if k == num:
			toreturn.append(i)
	return toreturn	
"""			
def parse_for_player_of_match(dic,dict1,fname):
	f1=open(fname,'r')
	for lin in f1:
		t = lin[:-1]
		t=t.split(',')
		a1=t[0]
		b1=t[1:]
		bx=b1[0]
		dic.append(bx)
		dict1.append(a1)
	
def parse_for_toss(toss,fname):
	f2=open(fname,'r')
	for lin in f2:
		t=lin[:-1]
		toss.append(t)
	#print win
	return win	
def parse_for_winning_team(win,fname):
	f2=open(fname,'r')
	for lin in f2:
		t=lin[:-1]
		win.append(t)
	#print win
	return win
	



"""def query7(bats,bowl):
	s1=parse_for_wicket(0,bowl)
	s2=parse_for_run_over(bats,8)
	print "7"
	print s2
def query8(bats,bowl):
	s1=parse_for_run(bats,100)
	#s2=parse_for_wicket(0,bowl)	
	print "query8"
	print s1	
def query6(bats,bowl):
	s1=parse_for_over(7,bowl)
	s2=parse_for_wicket(0,bowl)	
	print "query6"
	print s1
	print s2
"""
def query2(flag):
	s1=win           #winning team
	#print win
	print "Set A 2->"
	
	name_to_cty={}
	count2=0
	l=[]
	for i in range(0,5):
		
		if(win[i]=="New Zealand"):
			k=1
			j='1'
			l.append(10*(i+1)+k)
	
		elif(win[i]=="India"):
			k=0
			j='0'
			l.append(10*(i+1)+k)
		else:
			k=1
			j='1'
			l.append(10*(i+1)+k)	
	#print bats1[j]
	#print "/n"			
	#print bats2[j]
	print l			
	#print "gor"	
	flag3=0
	flag11=0
	flag41=0
	flag5=0
	flag2=0	
	#print bats2[k]    #list off all detail of losing team fr 2nd match
	s2=parse_for_duck(bats1[j],0)
	#print "s2"
	#print s2
	s3=parse_for_duck(bats2[j],0)
	s41=parse_for_duck(bats4[j],0)
	s5=parse_for_duck(bats5[j],0)
	s11=parse_for_duck(bats1[j],0)
	#print s3
	#print "losw"	
	for i in range(0,len(s2)):
		if s2[i]==0:
			flag2=1
	for i in range(0,len(s3)):
		if s3[i]==0:
			flag3=1		
	for i in range(0,len(s5)):
		if s5[i]==0:
			flag5=1		
	for i in range(0,len(s11)):
		if s11[i]==0:
			flag11=1
	for i in range(0,len(s41)):
		if s41[i]==0:
			flag41=1							
	if flag2==1 and flag3==1 and flag11==1 and flag41==1 and flag5==1 and flag==1:
		print "True"	
	else:
		print "False"
			
	
	#print bats1
	#all player name of losng team
	#print bats2
	toreturn=[]
	m=[]
	
	
def parse_for_duck(b,num):
	toreturn  = []
	#print b
	#print "k"
	#print num
	# number of duck
	for i in range(0,len(b)):
		
		temp=b[i]
		#print temp
		if(temp[0]==''):
			k1 = ''
		else:
			k1=temp[2]
			#print k1		
		#print k1
		#print "jj"
		if k1 == str(num):
			#print i
			#print "0"
			toreturn.append(0)
			
			break
		elif k1 == '':
			#print i
			
			break
		else:
			toreturn.append(1)	
	#print toreturn	
	
	return toreturn
	
"""def query5(bats,bowl):
	s1=parse_for_bat(bats,50)
	s2=parse_for_bowl(1,bowl)	
	print "query 5"
"""	
def query1(flag):
	ppl=[]
	ct=win		
	ct1=pom			
	#to compare with winning team
	print "Set A 1->"
	for i in range(0,5):
		if(ct[i]==ct1[i] or ct[i]=='Match Tied'):
			ppl.append(pomt[i])
			
	
	
	name_to_var = {}
	name_to_cty = {}
	count = 0
	count1=0
	m=0
	
	for i in pom:
		if i not in name_to_cty:
			name_to_cty[i]='x' + str(count1)
			count1 +=1
	#print name_to_cty		
	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	
	
	
	cm=0
	temp_strin2 = 'pomt => {'
	for i in ct1:
		temp_strin2 += name_to_cty[i] + str(cm) + ','
		cm=cm+1
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	
	#print temp_strin2
	
	#now for the predicate "gtsix"
	cx=0
	temp_strin3 = 'win => {'
	for i in ct:
		m=m+1
		if(i=='Match Tied'):
			if(pom[m-1]=='India'):
				temp_strin3 += 'x' + str(0) + ','
			else:
				temp_strin3 += 'x' + str(0)+ ','	
		else:		
			temp_strin3 += name_to_cty[i] + str(cx) + ','
		cx=cx+1	
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	#print temp_strin3
	
	
	v = temp_strin2 +temp_strin3
	#print v

	# now forming the query
	if(flag==1):
		
		query = 'all x (win(x) -> pomt(x))'
	else:
		query = 'exists x(win(x) -> pomt(x))'
	make_model_and_answer1(v, query, name_to_var)
	
def make_model_and_answer1(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	print val
	
	#print dom
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  win(x) -> pomt(x) given pomt(x) is true"
	
	l = nltk.LogicParser()
	c1 = l.parse('(win(x) -> pomt(x))')
	varnames =  m.satisfiers(c1, 'x', g)
	
	if(m.evaluate(query,g)==True):
		print pomt                #player name
	
# the function to 
#	1. generate the appropriate Model, after getting the values of the required predicates;
#	2. construct the query 
#	3. to prove/disprove the query.
def generate_and_solve_query1(bats, bowl):
	
	# for this query, we only need to consider the columns in bats dictionary
	c1 = parse_for_sr(bats, 150.0)
	c2 = parse_for_six(bats, 0)

	#print c1
	#print c2

	#Now constructing strings which are needed to create the model:

	#first creating mapping from playername to variable: we create a temporary dictionary
	# For example,
	# MS Dhoni => r1
	# SK Raina => r2

	name_to_var = {}
	count = 0
	for i in bats:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1

	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'

	# this is for the predicate "srate"
	temp_strin2 = 'srate => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'

	print temp_strin2
	#now for the predicate "gtsix"
	temp_strin3 = 'gtsix => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	print temp_strin3

	v = temp_strin1 + temp_strin2 + temp_strin3
	#print v

	# now forming the query
	query = 'all x (srate(x) -> gtsix(x))'

	make_model_and_answer(v, query, name_to_var)


def q2(sent):
	s=sent[1].split(' ')
	h=[]
	x=[]
	for i in range(0,len(s)-1):
		if s[i]=="consists":
			#print i
			m=i
		
	for i in range(0,m):
			
		h.append(s[i])
	
	h=' '.join(h)
	
	for i in range(0,len(s)-1):
		if s[i]=="of":
			m=i
	for i in range(m+1,len(s)):
		x.append(s[i])
	n=' '.join(x)	
	match=''.join(sent[0])

	wn=''.join(sent[1])
		
	win=wn.find("at least 1 ducks")

	if(match=="for all matches" and h=="losing side" and win>0):
		
		flag=1
	else:
		
		flag=0
		
	query2(flag)

def q3(sent):	
	h=[]
	h1=[]
	s=sent[1].split(' ')
	for i in range(0,len(s)-1):
		if s[i]=="if":
			#print i
			m=i
							
		if s[i]=="then":
			n=i
				
	for i in range(m+1,n):
		h.append(s[i])
	
	m=' '.join(h)
	print m
	
	l=m.split(' ')
	print l
	l1=[]
	for i in range(0,len(l)-1):
		l1.append(l[i])
	rate=' '.join(l1)
	print rate
	
	
	for i in range(n+1,len(s)):
		h1.append(s[i])
	n=' '.join(h1)	
	print n
	match=''.join(sent[0])
	print match	
	wn=''.join(sent[1])
		
	win=wn.find('more sixes than fours')
	
	if(match=="for all innings" and rate=="strike rate is above" and win>0):
		flag=1
	else:
		flag=0
		
	query3(flag)	


def q4():
	print "h"

def q5():
	print "k"

def q6():	
	print "d"

def q1(sent):	
	
	s=sent[1].split(' ')
	
	h=[]
	x=[]
	for i in range(0,len(s)-1):
		if s[i]=="is":
			#print i
			m=i
		
	for i in range(0,m):
			
		h.append(s[i])
	
	m=' '.join(h)
	print m
	print "#1"
	for i in range(0,len(s)-1):
		if s[i]=="to":
			m=i
	for i in range(m+1,len(s)):
		x.append(s[i])
	n=' '.join(x)	
	match=''.join(sent[0])
	print match	
	wn=''.join(sent[1])
		
	win=wn.find("winning team")
	
	if(match=="for all matches" and m=="player of the match" and win>0) :
		flag=1
	else:
		flag=0
		
	query1(flag)	


def main():

	bats={}
	
	bowl = {}
	
	l=[]
	l1=[]
	plyi = '/home/nancy/indian_players_profile.txt'
	plynz = '/home/nancy/nz_players_profile.txt'
	f1 = '/home/nancy/odi1_inn1_bat.txt'
	f2 = '/home/nancy/odi1_inn2_bat.txt'
	f5 = '/home/nancy/odi3_inn1_bat.txt'
	f6 = '/home/nancy/odi3_inn2_bat.txt'
	f3 = '/home/nancy/odi1_inn1_bowl.txt'
	f4 = '/home/nancy/odi1_inn2_bowl.txt'
	f7 = '/home/nancy/odi3_inn1_bowl.txt'
	f8 = '/home/nancy/odi3_inn2_bowl.txt'
	fo41 = '/home/nancy/odi4_inn1_bowl.txt'
	fo51 = '/home/nancy/odi5_inn1_bowl.txt'
	fo42 = '/home/nancy/odi4_inn2_bowl.txt'
	fo52 = '/home/nancy/odi5_inn2_bowl.txt'
	fo21 = '/home/nancy/odi2_inn1_bowl.txt'
	fo22 = '/home/nancy/odi2_inn2_bowl.txt'
	
	
	#battng
	fb31 = '/home/nancy/odi2_inn1_bat.txt'
	fb41 = '/home/nancy/odi4_inn1_bat.txt'
	fb51 = '/home/nancy/odi5_inn1_bat.txt'
		
	fb32 = '/home/nancy/odi2_inn2_bat.txt'
	fb42 = '/home/nancy/odi4_inn2_bat.txt'
	fb52 = '/home/nancy/odi5_inn2_bat.txt'
	
	
	f41 = '/home/nancy/odi1_inn1_bowl.txt'
	f42 = '/home/nancy/odi2_inn1_bowl.txt'
	f43 = '/home/nancy/odi3_inn1_bowl.txt'	
	f44 = '/home/nancy/odi4_inn1_bowl.txt'
	f45 = '/home/nancy/odi5_inn1_bowl.txt'
	
	f61 = '/home/nancy/odi1_inn2_bowl.txt'
	f62 = '/home/nancy/odi2_inn2_bowl.txt'
	f63 = '/home/nancy/odi3_inn2_bowl.txt'	
	 
	
	
	f11 = '/home/nancy/player_of_match1.txt'
	f12 = '/home/nancy/player_of_match2.txt'
	f13 = '/home/nancy/player_of_match3.txt'
	f14 = '/home/nancy/player_of_match4.txt'
	f15 = '/home/nancy/player_of_match5.txt'
	
	f21 = '/home/nancy/winning_team1.txt'
	f22 = '/home/nancy/winning_team2.txt'
	f23 = '/home/nancy/winning_team3.txt'
	f24 = '/home/nancy/winning_team4.txt'
	f25 = '/home/nancy/winning_team5.txt'
	
	ft1 = '/home/nancy/toss1.txt'
	ft2 = '/home/nancy/toss2.txt'
	ft3 = '/home/nancy/toss3.txt'
	ft4 = '/home/nancy/toss4.txt'
	ft5 = '/home/nancy/toss5.txt'
	parse_for_toss(toss , ft1)
	parse_for_toss(toss , ft2)
	parse_for_toss(toss , ft3)
	parse_for_toss(toss , ft4)
	parse_for_toss(toss , ft5)
	
	parse_for_player(ply1,plynz)
	parse_for_player(ply2,plyi)
	
	add_to_dict1(bats1, f1)
	add_to_dict1(bats1, f2)
	add_to_dict1(bowl1, f3)
	add_to_dict1(bowl1, f4)
	add_to_dict1(bats2, f5)
	add_to_dict1(bats2, f6)
	add_to_dict1(bats5, fb51)
	add_to_dict1(bats5, fb52)
	add_to_dict1(bats3, fb31)
	add_to_dict1(bats3, fb32)
	add_to_dict1(bats4, fb41)
	add_to_dict1(bats4, fb42)
	
	
	add_to_dict1(bowl3, f7)
	add_to_dict1(bowl3, f8)
	add_to_dict1(bowl4, fo41)
	add_to_dict1(bowl4, fo42)
	add_to_dict1(bowl5, fo51)
	add_to_dict1(bowl5, fo52)
	add_to_dict1(bowl2, fo21)
	add_to_dict1(bowl2, fo22)
	#add_to_dict(bowl, f44)
	
	parse_for_player_of_match(pom,pomt,f11)
	parse_for_player_of_match(pom,pomt,f12)
	parse_for_player_of_match(pom,pomt,f13)
	parse_for_player_of_match(pom,pomt,f14)
	parse_for_player_of_match(pom,pomt,f15)
	
	parse_for_winning_team(win,f21)
	parse_for_winning_team(win,f22)
	parse_for_winning_team(win,f23)
	parse_for_winning_team(win,f24)
	parse_for_winning_team(win,f25)
	
	
	inpu=raw_input("your query")
	#sent="For all the matches,player of match is given to the player of the winning team".split(',')
	sent=inpu.split(",")
	w=''
	if((sent[1].find('if'))>=0):
		w=' if '
		n='if'
		grammar(w,sent)
	if((sent[1].find('consists of'))>=0):
		w=' consists of '
		n='consists of'
		grammar(w,sent,n)
	if((sent[1].find('is given to'))>=0):
		w=' is given to '
		n='is given to'
		grammar(w,sent,n)
	if((sent[1].find('and'))>=0):
		w=' and '
		n='and'
		grammar(w,sent,n)
	if((sent[1].find(' contains '))>=0):
		w=' contains '
		n='contains'
		grammar(w,sent,n)
	
			
def grammar(w,inpu,n):
	#sent=inpu.split(',')
	#s=sent[1]
	sent=inpu
	m=0
	h=[]
	x=[]
	if(sent[1].find(w)>=0):
		b=sent[1].split(w)
	desc1=b[0]
	desc2=b[1]
	"""de1=''.join(desc1)
	print de1
	e1=de1.split(' ')      #check for digit in desc1  this is a list
	print e1
	#de1=desc1.split(' ')
	
	de2=''.join(desc2)
	e2=de2.split(' ')
	print len(e2)
	in1=0
	in2=0
	for i in range(0,len(e1)):
		if((e1[i].isdigit())>0):
			in1=i
	inn1=e1[in1]
	print inn1
	for i in range(0,len(e2)):
		#print e2[i]
		if((e2[i].isdigit())>0):
			#print e2[i]
			in2=i	
	inn2=e2[in2]	
	print inn2
	dig1=desc1.split(inn1)
	dig2=desc2.split(inn2)
	print dig2
	#print dig2		
	#print desc1
	#print desc2"""
	match=''.join(sent[0])
	#print match	
	qu=[]

	qu.append(match)
	qu.append(desc1)
	qu.append(n)
	qu.append(desc2)
	print qu
	print "hhh"
	gr = nltk.parse_cfg("""
	S -> quan desc1 connector desc2
	quan -> "for all matches"|"for all innings"|"there exists player"|"there exists a match" | "there exists a player" | "in any of the matches" | "there exists player in the series"
	desc1 -> "player of match" | "losing side" | "winning side" | "who have scored more than 50 runs in batting" | "for any side there exists at least 1 bowler who has bowled more than 7 overs" | "there exists a bowler who did not claim any wicket" | "where a batsman scored hundred" | "who is less than 26 years old"
	connector -> "and" | "if"| "is given to" | "consists of" | "contains"
	desc2 -> "player of winning team" | "at least 1 ducks in the batting innings" | "at least 1 player who hit at least 1 boundary yet his strike rate was below 100"|"claimed at least 1 wicket in bowling in the same match" | "failed to get any wicket" | "went for more than 8 runs per over" | "has scored more than 250 runs in the series without any ducks in any of the matches" | "despite that the team lost"
	""")	
	
	
	print nltk.ChartParser(gr)	
	rd_parser = nltk.RecursiveDescentParser(gr)
	for tree in rd_parser.nbest_parse(qu):
		print tree	
	tree.draw()
	#print(tree.treepositions())
	l=[]
	k=[]
	l=tree.treepositions()
	
	for i in range(0,len(l)-1):
		
		if(len(l[i])>=len(l[i+1])):
			k.append(tree[l[i]])
	print k.append(tree[l[len(l)-1]])
			


	query(k)
def query(k):
	print k
	if(k[1]=='player of match' and k[3]=='player of winning team'):
		if(k[0]=='for all matches'):
			flg=1
			query1(flg)
		elif(k[0]=='there exists a match'):
			flg=0
			query1(flg)	
	if(k[1]=='losing side' and k[3]=='at least 1 ducks in the batting innings'):
		if(k[0]=='for all matches'):
			flg=1
			query2(flg)
		elif(k[0]=='there exists a match'):
			flg=0
			query2(flg)		
	if(k[1]=='winning side' and k[3]=='at least 1 player who hit at least 1 boundary yet his strike rate was below 100'):
		print "en"
		if(k[0]=='for all matches'):
			flg=1
			query4(flg)
		elif(k[0]=='there exists a match'):
			query4(flg)		
	if(k[1]=='who have scored more than 50 runs in batting' and k[3]=='claimed at least 1 wicket in bowling in the same match'):
		query5()
	if(k[1]=='for any side there exists at least 1 bowler who has bowled more than 7 overs' and k[3]=='failed to get any wicket'):
		if(k[0]=='for all matches'):
			flg=1
			query6(flg)
		elif(k[0]=='there exists a match'):
			query6(flg)	
	if(k[1]=='there exists a bowler who did not claim any wicket' and k[3]=='went for more than 8 runs per over'):
		query7()
	if(k[1]=='where a batsman scored hundred' and k[3]=='despite that the team lost'):
		if(k[0]=='for all matches'):
			flg=1
			query8(flg)
		elif(k[0]=='there exists a match'):
			query8(flg)	
	if(k[1]=='who is less than 26 years old' and k[3]=='has scored more than 250 runs in the series without any ducks in any of the matches'):
		if(k[0]=='for all players'):
			flg=1
			query9(flg)
		elif(k[0]=='there exists a player'):
			flg=0
			query9(flg)			
		
 
	
	#generate_and_solve_query1(bats, bowl)
"""	query1(bats1,bats2)
	query2(bats,bowl)
	query3(bats1,bats2)
	query5(bats1,bats2)
	query6(bats1,bats2) """
	#query8(bats1,bats2)
"""	query7()
	query4()
	query8(bats,bowl)
	query10()
	query9()
	
	query11(bats1,bats2)
	query12()
	query13()
	query14(bats1,bats2)
	query15()
	query16()
	query17()
	query18()
	query19()
	query20()"""
"""query3(bats,bowl)
	query5(bats,bowl)
	query6(bats,bowl)
	query7(bats,bowl)
	query2(bats,bowl)
	query8(bats,bowl)"""
if __name__ == "__main__":
	main()
