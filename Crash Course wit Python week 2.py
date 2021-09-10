#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 4. Students in a class receive their grades as Pass/Fail. 
# Scores of 60 or more (out of 100) mean that the grade is "Pass". 
# For lower scores, the grade is "Fail". In addition, scores above 95 (not included) 
# are graded as "Top Score". Fill in this function so that it returns the proper grade.

def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail


# In[2]:


# 6. Complete the body of the format_name function. 
# This function receives the first_name and last_name parameters and then returns 
# a properly formatted string.

def format_name(first_name, last_name):
	if first_name != "" and last_name != "":
	    string = "Name: " + last_name + ", " + first_name
   
	elif first_name == "" and last_name == "" :   
	    string = ""
	
	else:
	    string  = "Name: " + last_name + first_name  
	# code goes here	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


# In[3]:


# 7. The longest_word function is used to compare 3 words. 
# It should return the word with the most number of characters 
# (and the first in the list when they have the same length). 
# Fill in the blank to make this happen.

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) > len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))


# In[ ]:


# 10.The fractional_part function divides the numerator by the denominator, 
# and returns just the fractional part (a number between 0 and 1). 
# Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, 
# the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	if denominator > 0:
		return (numerator % denominator / denominator)
	else:
	    return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

