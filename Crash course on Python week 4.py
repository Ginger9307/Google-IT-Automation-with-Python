#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Stings. More String Methods
# Function returns the initials of the words contained in the phrase received, 
# in upper case. For example: "Universal Serial Bus" should return "USB"; 
# "local area network" should return "LAN”.

def initials(phrase):
    words = phrase.split(" ")
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


# In[2]:


# Stings. Practice Quiz
# 1. The is_palindrome function checks if a string is a palindrome. A palindrome is a string 
# that can be equally read from left to right or right to left, omitting blank spaces, 
# and ignoring capitalization. Function returns True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the end of one string, and to the front
		# of the other string. 
		if letter != " ":
			new_string = new_string + letter.lower()
			reverse_string = letter.lower() + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


# In[3]:


# Stings. Practice Quiz
# 3. If we have a string variable named Weather = "Rainfall", which of the following 
# will print the substring or all characters before the "f"Weather = "Rainfall"

Weather = "Rainfall
print(Weather[:4])


# In[4]:


# Stings. Practice Quiz 
# 4. Nametag function uses the format method to return first_name and the first initial 
# of last_name followed by a period. 

def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 


# In[ ]:


# Stings. Practice Quiz
# 5. 

def replace_ending(sentence, old, new):
	# if the old string is at the end of the sentence 
	if sentence[-len(old):] == old:
		# reducing sentence by removing old syting from the end 
		sentence = sentence[:len(sentence) - len(old)]
		# adding new sentence to the reduced sentence
		new_sentence = sentence + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"


# In[7]:


# Lists. Practice Quiz 
# 1. Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for file_n in filenames:
    if file_n[-4:] == ".hpp":
	    newfilenames.append(file_n.split(".")[0] + ".h")
	    newfilenames.append(file_n)
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# In[8]:


# Lists. Practice Quiz
# 2. Create a function that turns text into pig latin: a simple text transformation that modifies each word
# moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.

def pig_latin(text):
  newwords = []
  # Separate the text into words
  words = text.split(" ")
  for word in words:
    # Create the pig latin word
    newword = word + word[:1] + "ay"
    newwords.append(newword[1:])
  # Turn the list back into a phrase
  return " ".join(newwords)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# In[10]:


# Lists. Practice Quiz
# 3. The permissions of a file in a Linux system are split into three sets of three permissions: read, write, 
# and execute for the owner, group, and others. Each of the three values can be expressed as an octal number
# summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written 
# with a string using the letters r, w, and x or - when the permission is not granted.
# make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for number in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if number >= value:
                result += letter
                number -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


# In[14]:


# Lists. Practice Quiz
# 5. The group_list function accepts a group name and a list of members, and returns a string with the format: 
# group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". 
# Make the function to do that.

def group_list(group, users):
  return group + ": " + ", ".join(users)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


# In[13]:


# Lists. Practice Quiz
# 6. Make the guest_list function that reads in a list of tuples with the name, age, and profession of each party guest,
# and prints the sentence "Guest is X years old and works as __." for each one.  

def guest_list(guests):
	for guest in guests:
		name, age, prof = guest
		print("{} is {} years old and works as {}".format(name, age, prof))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""


# In[15]:


# Dictionaries. Practice Quiz
# 1. The email_list function receives a dictionary, which contains domain names as keys, and a list of users 
# as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+"@"+domain)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# In[16]:


# Dictionaries. Practice Quiz
# 2. The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a 
# list of their groups as values. 

def groups_per_user(group_dictionary):
	user_groups = {}
	# go through group_dictionary
	for group, users in group_dictionary.items():
		# go through the users in the group
		for user in users:
			# add the group to the the list of groups for this user, creating the entry in the dictionary if necessary
			if user not in user_groups:
			   user_groups[user] = []
			user_groups[user].append(group)   

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


# In[17]:


# Dictionaries. Practice Quiz
# 5. The add_prices function returns the total price of all of the groceries in the  dictionary.

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for price in basket.values() :
		# Add each price to the total calculation
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


# In[18]:


# Module 4 Graded Assessment
# 1. The format_address function separates out parts of the address string into new strings: house_number and 
# street_name, and returns: "house number X on street named Y". The format of the input string is: 
# numeric house number, followed by the street name which may contain numbers, but never by themselves, 
# and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 

def format_address(address_string):
  # Declare variables
  house = 0
  list_street = []
  # Separate the address string into parts
  parts = address_string.split(" ")
  # Traverse through the address parts
  for word in parts:
      # Determine if the address part is the
      # house number or part of the street name
      if word.isnumeric() == True:
          house = int(word)
      else:
          list_street.append(word)
  street = " ".join(list_street)
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"
print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"
print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# In[19]:


# Module 4 Graded Assessment
# 2. The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Write this function in just one line?

def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# In[27]:


# Module 4 Graded Assessment
# 4. A professor with two assistants, Jamie and Drew, wants an attendance list of the students, 
# in the order that they arrived in the classroom. Drew was the first one to note which students arrived, 
# and then Jamie took over. After the class, they each entered their lists into the computer and emailed them 
# to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed 
# a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list 
# as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list 
# of the students as they arrived.

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  list2.extend(list1)
  return list2
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


# In[21]:


# Module 4 Graded Assessment
# 4. Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start 
# and end, and returns a list of squares of consecutive numbers between start and end inclusively.

def squares(start, end):
	return [ x*x for x in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# In[24]:


# Module 4 Graded Assessment
# 5. def car_listing(car_prices):
def car_listing(car_prices):  
  result = ""
  for car, price in  car_prices.items():
    result += "{} costs {} dollars".format(car, price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


# In[25]:


# Module 4 Graded Assessment
# 6. Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into
# dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is 
# a partial list, but Rory's list has more current information about the number of guests. Combine both 
# dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary 
# taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  final_guests = {}
  for guest in (guests2, guests1):
    final_guests.update(guest)
  return final_guests 
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))


# In[26]:


# Module 4 Graded Assessment
# 7. Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, 
# not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case.

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha() == True: 
    # Add or increment the value in the dictionary
      if letter.lower() not in result:
          result[letter.lower()] = 1
      else:
          result[letter.lower()] += 1  
      
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}
print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


# In[ ]:




