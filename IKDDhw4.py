#!/usr/bin/python
#coding=utf-8

query = raw_input("input :")
q=query.decode('utf-8')

M = [[0, 0.5, 0], [0.5, 0, 1], [0.5, 0.5, 0]]
V = [0.33, 0.33, 0, 0.33, 0]
V2 = [0, 0, 0, 0, 0]

filename=['page1.txt','page2.txt','page3.txt','page4.txt','page5.txt']
j = 0
right=[0,0,0,0,0]
for i in filename :
	f = file(i)  
	while True :
		line = f.readline()
		data = line.decode('big5')
		if( len( line ) == 0 ) :
			break
		if((q in data) == True) :
			right[j]=1
	f.close()
	j +=1
#for k in range(5) :
#	if (right[k]==1) :
#		print filename[k]

def PR():
	V2[0] = M[0][0]*V[0] + M[0][1]*V[1] + M[0][2]*V[3]
	V2[1] = M[1][0]*V[0] + M[1][1]*V[1] + M[1][2]*V[3]
	V2[3] = M[2][0]*V[0] + M[2][1]*V[1] + M[2][2]*V[3]

while True:
	PR()
	if (abs(V[0]-V2[0]) < 0.001 and abs(V[1]-V2[1]) < 0.001 and abs(V[3]-V2[3]) < 0.001):
		break
	else:
		V[0] = V2[0]
		V[1] = V2[1]
		V[3] = V2[3]

V[2] = V[0]*0.33 + V[3]*0.5
V[4] = V[2]

rank = [0, 1, 2, 3, 4]
for i in range(4, -1, -1):
	for j in range(i):
		if (V[j] > V[j+1]):
			V[j], V[j+1] = V[j+1], V[j]
			rank[j], rank[j+1] = rank[j+1], rank[j]
#print rank
#print V

count=1

print "+----+------------+"
for i in range(4,-1,-1) :
	if (right[rank[i]]==1):
		print "\b|",
		print "%-3d" % count,
		print "\b|",
		print "%-11s" % filename[rank[i]],
		print "\b|"
		print "+----+------------+"
		count+=1
