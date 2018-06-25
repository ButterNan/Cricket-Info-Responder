import nltk
import sys
from nltk.corpus import wordnet as wn

def lemmalist(str):
    syn_set = []
    for synset in wn.synsets(str):
        for item in synset.lemma_names:
            syn_set.append(item)
    return syn_set

def expand(arglist):
	newl=arglist
	for i in arglist:
		newl=newl + lemmalist(i)		
	return newl

def parse_for_comm(file):
	commentary = open(file,'r')

	commentary_parse= []
	ans = []
	for line in commentary:
		temp1 = line[:-1]
		temp2 = temp1.split(' ')
		commentary_parse.append(temp2) 
	#print commentary_parse	
	return commentary_parse	
def answer(inpu):
	text=nltk.word_tokenize(inpu)
	k=nltk.pos_tag(text)
	print k
	print "full"
	
	fname = '/home/nancy/mydataset/ind.txt'
	fl=open(fname,'r')
	fname1 = '/home/nancy/mydataset/newz.txt'
	fl1=open(fname1,'r')
	name=''
	for i in range(0,len(k)):
		
		if(k[i][1]=='NNP'):
			if(k[i+1][1].find('VBD')>=0):
				name=k[i][0]
			else:
				name=k[i][0]	
			#print name
		if(k[i][0]=='match'):
			print "yes"
			if(k[i-1][0]=='first' and i<=len(k)):
				#print k[i-1][0]	
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
						for i in temp:
							if(i.find(name)>=0): 
								print "kj"
								fname='/home/nancy/mydataset/odi1_commentary_inn1.txt'
								flgnam=1
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
						for i in temp:
							if((i.find(name)>=0)): 
								print "kjhgg"
								fname='/home/nancy/mydataset/odi1_commentary_inn2.txt'		
				else:				
					fname1='/home/nancy/mydataset/odi1_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi1_commentary_inn2.txt'			
					print "file"		
							
			elif(k[i-1][0]=='second' and i<=len(k)):	
				print k[i-1][0]	
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
						for i in temp:
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi2_commentary_inn1.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
						for i in temp:
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi2_commentary_inn2.txt'
				else:				
					fname1='/home/nancy/mydataset/odi1_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi1_commentary_inn2.txt'			
					print "file"				
			elif(k[i-1][0]=='third' and i<=len(k)):	
				print k[i-1][0]	
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi3_commentary_inn1.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi3_commentary_inn2.txt'	
				else:				
					fname1='/home/nancy/mydataset/odi1_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi1_commentary_inn2.txt'			
					print "file"				
			elif(k[i-1][0]=='fourth' and i<=len(k)):	
				print k[i-1][0]	
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi4_commentary_inn2.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
							i
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi4_commentary_inn1.txt'
				else:				
					fname1='/home/nancy/mydataset/odi1_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi1_commentary_inn2.txt'			
					print "file"				
					
			elif(k[i-1][0]=='fifth' and i<=len(k)):	
				print k[i-1][0]	
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi5_commentary_inn1.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
					
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi5_commentary_inn2.txt'
				else:				
					fname1='/home/nancy/mydataset/odi1_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi1_commentary_inn2.txt'			
					print "file"				
						
				
			elif(k[i+1][1]=='CD' and k[i+1][0]=='1' and i<len(k)):
			
				m=k[i+1][0]
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi1_commentary_inn1.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
							
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi1_commentary_inn2.txt'
				else:				
					fname1='/home/nancy/mydataset/odi1_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi1_commentary_inn2.txt'			
					print "file"				
			elif(k[i+1][1]=='CD' and k[i+1][0]=='2' and i<len(k)):
			
				m=k[i+1][0]
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
							
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi2_commentary_inn1.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
							
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi2_commentary_inn2.txt'
				else:				
					fname1='/home/nancy/mydataset/odi2_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi2_commentary_inn2.txt'			
					print "file"				
			elif(k[i+1][1]=='CD' and k[i+1][0]=='3' and i<len(k)):
			
				m=k[i+1][0]
				print m
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi3_commentary_inn1.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi3_commentary_inn2.txt'
				else:				
					fname1='/home/nancy/mydataset/odi3_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi3_commentary_inn2.txt'			
					print "file"				
			elif(k[i+1][1]=='CD' and k[i+1][0]=='4' and i<len(k)):
			
				m=k[i+1][0]
				print m
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi4_commentary_inn2.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi4_commentary_inn1.txt'
				else:				
					fname1='/home/nancy/mydataset/odi4_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi4_commentary_inn2.txt'			
					print "file"				
			elif(k[i+1][1]=='CD' and k[i+1][0]=='5' and i<len(k)):
			
				m=k[i+1][0]
				print m
				if(name!=''):
					for line in fl1:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi5_commentary_inn1.txt'
					for line in fl:                 
						temp = line[:-1]
						temp = temp.split(',')
		
						for i in temp:
						
							if((i.find(name)>=0)): 
								print "kj"
								print name
					
								fname='/home/nancy/mydataset/odi5_commentary_inn2.txt'	
				else:				
					fname1='/home/nancy/mydataset/odi5_commentary_inn1.txt'
					fname2='/home/nancy/mydataset/odi5_commentary_inn2.txt'			
					print "file"
	
	for i in range(0,len(k)):
		if((k[i][1].find('VBD')>=0)  and (k[i-1][1].find('NNP')>=0)):
			print "khh"
			#print k[i][0]
			if(k[i][0].find('dismiss')>=0):
				nam=[]
				nam1=k[i][0]
				nam.append(k[i][0])
				#print nam
				#print nam1
				l2=expand(nam)              #synonyms for dismissed
				print l2
				h=[]
				prscom=parse_for_comm(fname)
				h=prscom
				ct=0
				#for m in range(0,len(l2)):
				#	x=l2[m]
				#this dsnt work
				
							
					
				#print h
				if(k[i-1][1].find('NNP')>=0):          #ryder name
					#print "he"
					for line in range(0,len(h)):

						d=h[line]
						#print d
						nm=str(k[i-1][0])
						for g in range(0,len(d)):
							#print d[g-1]
							if nm in d[g]:
								#print d
							
								if((d[g-1].find('to')>=0) and (g<(len(d)-1))):
									if(d[g+1].find('OUT')>=0):
										if(k[0][0]=='when'):
							
											#print d
											#print "ent"
											print h[line-1]
										elif(k[0][0]=='how'):
											print d[g:]	
							
						
					
				
		elif(k[i][1].find('NNP')>=0):
			print "klkhfhgh"
			#print k[i][0]
			if(k[i+1][0].find('out')>=0):
				nam=[]
				nam1=k[i][0]
				nam.append(k[i][0])
				#print nam
				#print nam1
				l2=expand(nam)              #synonyms for dismissed
				#print l2
				h=[]
				print "eggg"
				prscom=parse_for_comm(fname)
				h=prscom
				print fname
				ct=0		
				for line in range(0,len(h)):
				
						d=h[line]
						#print d
						nm=str(k[i][0])
						#print nm
						for g in range(0,len(d)):
							#print d[g-1]
							#print d[g]
							if nm in d[g]:
								#print d
								#print "jj"
								if((d[g-1].find('to')>=0) and (g<(len(d)-1))):
									if(d[g+1].find('OUT')>=0):
										if(k[0][0]=='when'):
							
											#print d
											print "ent"
											print h[line-1]
										elif(k[0][0]=='how'):
											print d[g:]	
		elif(k[i][1]=='JJ' and (k[i-1][1].find('NNP')>=0)):
			
			#print k[i][0]
			nam=[]
			nam1=k[i][0]
			nam.append(k[i][0])
			#print nam
			#print nam1
			l2=expand(nam)              #synonyms for adjective
			#print l2
			#print synsets
			print "active"
			h=[]
			prscom=parse_for_comm(fname)
			h=prscom
			ct=0
			print fname
			#print h
			ovrr=[]
			ovrr1=[]
			ind=[]
			for line in range(0,len(h)):
				d=h[line]
				nm=str(k[i-1][0])
				for g in range(0,len(d)):
					#print d[g-1]
					#print d[g].find(nm)
					if nm in d[g]:
							
						if((d[g-1].find('to')>=0)):
							if((d[g+1].find('1')>=0) or (d[g+1].find('SIX')>=0) or (d[g+1].find('FOUR')>=0)  or (d[g+1].find('2')>=0)):
								if(k[1][0]=='what' and k[2][0]=='overs'):
									
									ovr1=h[line-1]
									over=''.join(ovr1)
									ov=over.split('.')
									ovrr.append(over)
									ovrr1.append(ov)
									print over
									ind.append(line-1)
									#print ov[0]
									#print "over"
									print ovrr
			
					
				
								
						
		elif(k[i][1]=='JJ' and (k[i][0]!='second' or k[i][0]!='first' or k[i][0]!='third' or k[i][0]!='fourth' or k[i][0]!='fifth') and (k[i-1][1]!='NNP')):
			#l2=expand(nam)              #synonyms for adjective
			#print l2
			#print "hh"
			h=[]
			
			lst=[]
			lst.append(k[i-1][0])
			
			bst=expand(lst)
			print bst
			print "best sysnets"
			if(k[i-1][1]=='JJS'):
				prscom=parse_for_comm(fname1)
				prscm=parse_for_comm(fname2)
				h=prscom
				h1=prscm
				for line in range(0,len(h)):
					d=h[line]
					nm=str(k[i][0])
					#print nm
					best=''.join(h[line])
					for g in range(0,len(d)):
						#print d[g-1]
						#print d
						if nm == d[g] and best.find('FOUR')>=0:
							#print "ggf"
							print h[line]
						elif(best.find('SIX')>=0 or best.find('FOUR')>=0):
							#print "fff"
							print h[line-1]	
				for line in range(0,len(h1)):
					d=h1[line]
					nm=str(k[i][0])
					#print nm
					best=''.join(h1[line])
					for g in range(0,len(d)):
						#print d[g-1]
						#print d
						if nm == d[g] and best.find('FOUR')>=0:
							#print "ggf"
							print h1[line]			
				
						elif(best.find('FOUR')>=0 or best.find('FOUR')>=0):
							
							print h1[line-1]
					
		
		elif((k[i][1].find('NN')>=0) and (k[i][0].find('powerplay')>=0)):
			prscom=parse_for_comm(fname1)
			h=prscom
			print fname1
			prsn=parse_for_comm(fname2)
			h1=prsn
			ov=[]
			bowl=[]
			if(k[i+1][1].find('VB')>=0):
				
				for line in range(0,len(h)):
					d=h[line]
					for g in range(0,len(d)):
						if(((d[g].find('powerplay')>=0) or (d[g].find('Powerplay')>=0)) and d[g-1].find('batting')>=0):
							print h[line]
							if(k[0][0]=='when'):
								ov.append(h[line+1])
							elif(k[0][0]=='who'):
								d=h[line+2]
								bowl.append(d[0])	
				print ov
					
			elif(k[	i-2][1]=='RB'):
				print "g"
				for line in range(0,len(h)):
					d=h[line]
					for g in range(0,len(d)):
						if(((d[g].find('powerplay')>=0) or (d[g].find('Powerplay')>=0)) and (d[g-1].find('batting')>=0)):
							if(k[0][0]=='who'):
								print h[line+2]
							#if(k[0][0]=='who' and (line<len(h)-2)):
							#	d=h[line+2]
							#	bowl.append(d[0])
				#print bowl	
				
		elif(k[i][1]=='NN' and k[i][0]=='weather'):
			print k[i][0]
			h=[]
			print fname1
			prscom=parse_for_comm(fname1)
			h=prscom
			ct=0
			for line in range(0,len(h)):
				d=h[line]					
				nm=['afternoon','weather','sunny']
				for g in range(0,len(d)):
						while(ct<len(nm)):
							
							#print nm[ct]
							if(d[g].find(nm[ct])>=0):
								print "equal"
								print h[line]
							ct=ct+1
						ct=0				
								
			
	fn=open(fname,'r')		
	for i in range(0,len(k)):
		if(k[i][1]=='NNP'):
			print k[i][0]
			
				

					
			
		

				
				
				
		
	
	
def main():
	inpu=raw_input("query")
	answer(inpu)
	
	
if __name__ == "__main__":
	main()
