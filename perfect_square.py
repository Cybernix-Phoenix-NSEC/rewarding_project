# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:39:44 2021

@author: deyas
"""

def is_square(n):    
   ans=0
   while ans**2<n:
       ans+=1
   if ans**2==n:
       print ("perfect sq")
   else:
       print ("not perfect sq")