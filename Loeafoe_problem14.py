#Dean Loeafoe
#Problem 14
#Longest Collatz Sequence

#Execution might take a while since this is brute force
#Each int is converted to an unsigned int after creation

report_number = 0 #Keeps track of the current number being tested - will not be modified
report_number = 0 + 2**32 #Convert to unsigned int
report_number = 0 #Reset unsigned int to zero

high_number = 0 #Keeps track of the number that created the highest chain
high_number = high_number + 2**32 #Convert to unsigned int
high_number = 0 #Reset unsigned int to zero

high_chain = 0 #Keeps track of the count of the highest chain
high_chain = high_chain + 2**32 #Convert to unsigned int
high_chain = 0 #Reset unsigned int to zero

current_number = 0 #Keeps track of the current number being tested - will be modified for calculations
current_number = current_number + 2**32 #Convert to unsigned int
current_number = 0 #Reset unsigned int to zero

current_chain = 0 #Keeps track of the current chain count
current_chain = current_chain + 2**32 #Convert to unsigned int
current_chain = 0 #Reset unsigned int to zero

for x in range(1, 1000000):
  
  current_number = x #Number being tested - will be modified for calculations
  report_number = x #Number being tested - will not be modified in case it has to be stored as the new high_number
  
  while current_number > 0:
    
    #Base Case: If the current number drops to 1, the chain counting will stop
    if current_number == 1:
      current_chain += 1

      #Record new high number and chain count if this number's chain count is higher than the high count
      if current_chain > high_chain:
        high_chain = current_chain
        high_number = report_number
        
      #Reset the chain count and break out of this loop
      current_chain = 0
      break
        
    #Divide by 2 if the current number is even
    elif current_number % 2 == 0:
      current_number = current_number/2
      current_chain += 1
      
    #Multiply by 3 and add 1 if the current number is odd
    elif current_number % 2 == 1:
      current_number = ((current_number * 3) + 1)
      current_chain += 1

#Report findings
print(str(high_number) + " produced the longest chain with a count of " + str(high_chain))