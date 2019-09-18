#!/usr/bin/python3

def check (input):                  
	p=set (input) 
	data={'0','1'}
	if data==p or data=={'0'} or data=={'1'}:
	 print("It is a valid input")


binary=input("enter the binary data\n")      #taking input
check (binary)                    
one='1'
count=binary.count(one)
#print("count is:",count)
if count%2==0:                                         #addding parity bit
	binary=binary+'1'
	print("The parity data :  ",binary)      #data with parity
else:
	binary=binary+'0'
	print("The parity data :  ",binary)
print("\n")
newbinary=binary.replace("010","0100")  
newbinary= newbinary+"0101"                    #for insertion of 0
print("transmitted data:   ",newbinary)
