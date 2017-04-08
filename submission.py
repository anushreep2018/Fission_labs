# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:30:29 2017

@author: Anushree
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 02:14:06 2017

@author: Anushree



We are trying to find out smallest prime factor of  numberof questions in each contest.

Since  we need only the smallest prime factor of a number, we need to check the divisibility of the number with only prime numbers
upto the square root of that number.Because we will get prime factor only till sqrt(n),otherwise the number itslef is the smallest 
prime factor.

Generate prime numbers using variant seive of eranthoses 

Check prime numbers from 2 onwards until the square root of larget number or until all smallest prime factors are fetched
     --Check for each contest if smallest prime is already found 
     --If smallest prime is not found then check divisibility with this prime
     --If it is divisible update the smallest prime factor for that contest
     --Also mark the mutiples of this prime number as not prime so that they are not checked if they are prime or not
          


This differes from Seive of Erathoses because we do not get all prime number till sqaure root of N but we stop when we have found 
smallest prime number for all contests.

"""

import sys
import math

def main():
    
    print("Input: \n")
    problems=[]
    #Get line by line input from user
    try:
        while True:
            line = input()
            if line:
                num=int(line)
                if num<=1000000 and num>=1:
                    problems.append(num)
                else:
                    sys.exit(2)
            else:
                break
    
        if (problems[0]!=len(problems)-1):    
            sys.exit(3)
            
    #Check if input is in correct form       
    except SystemExit as e:
        if e.code==2:
            print("T and N not in specified range")
        if e.code==3:
            print("Length mismatch between T specified and N's entered")
        return
       
    #Take the largest no of problems,lar,out of all contest and find primes till sqrt(lar)
    lar=max(problems[1:])
    contests=problems[0]
    
    sqrt_lar=int(math.sqrt(lar))
    
    #Flag is true if the index at that place is a prime    
    flag=[True for i in range(0,sqrt_lar+1)]
     
    #Flag is false if smallest prime is not yet found for that contest
    found_p=[False for i in range(0,contests+1)]
    
    #Stores the smallest prime for every contest,initialed with number itself
    small_p=[problems[i] for i in range(0,contests+1)]
    
    pr=2
    count=0
    
    
    #Loop until prime <=sqrt_lar or all the contests have got smallest prime
    while(pr<=sqrt_lar and count!=contests):
    
        #See if pr is a prime  by checking the flag
        if(flag[pr]==True):
            
        #If pr is prime ,check divisibility with this prime for all the contest which do not have smallest prime yet
             for k in range(1,contests+1):#
                if(found_p[k]==False):
                    if(problems[k]%pr==0):
                        small_p[k]=pr
                        count=count+1
                        found_p[k]=True
                        
        #Since this prime is checked ,mark flag false for multiples of this prime as they cannot be prime                
        for i in range(pr*2,sqrt_lar,pr):
            flag[i]=False

        pr=pr+1
    
    #Print the result :First one is problem solved by herbal ,second one is problem solved by naren
    print("Output: \n")
    for i in range(1,contests+1):
        print("%s %s \n"%(small_p[i],problems[i]-small_p[i]))

if __name__ == "__main__":
    main()  
    
    
    
    
    
    
    
    
    
    
    
    
    
