# PF-Assignment-first
""" 
Exercise 1: Calculate the multiplication and sum of two numbers.
Given two integer numbers, return their product only if the product is equal to or lower than
1000. Otherwise, return their sum
"""
   num1=int(input("enter num1"))
   num2=int(input("enter num2"))
   sum=num1+num2
   product=num1*num2
   if(product<=1000):
       print("product",product)
   else:
       print("sum",sum)
    
"""
   Exercise 2: Print the sum of the current number and the previous number.
Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current
and previous numbers.
"""
    previous num = 0
    current num =1
    while previous num <= 10:
        current sum = current num + previous num
        print("current_number",current number,"previous number",privious_number,"sum",current_sum)
        current_number = current_number+1
        previous_number = previous_number+1
"""
    Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an
even index number.
"""
    string = input ("Entre a string:")
    index = 0
    even characters = " "
    while index < len (string) :
       if index %2 = :
           even characters = even characters + string(index)
       index+=1
    print("Characters at even position", even characters)
"""
    Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new
string.
"""
     string=(input("enter a srtring:"))
     n=int(input("Entre the number of character to remove: "))
     if n< len(string) :
         result= string[n:]
         print ("output:" result)
     else:
         print (n must be less than the length of the string.")
""" 
    Exercise 5: Check if the first and last number of a list is the same.
Write a program to print “First and Last Numbers are same” if the first and last numbers of a
given list are the same. If the numbers are different then print “Not Same”.
"""
      numbers= [115,167,289,300,450,690,850,990]
      if numbers[0] == numbers[-1]:
         print("first and last number are same")
    else:
         print("numbers are not same")
"""
    Exercise 6: Display numbers divisible by 5 from a list.
Iterate the given list of numbers and print only those numbers which are divisible by 5  
"""
      numbers=[10,15,25,30,40,55,75,90,100]
      for number in numbers: 
      if number % 5 == 0:
         print("numbers divided by 5 =",number)
"""        
Exercise 7: Print the following pattern.
1
2 2 
3 3 3
4 4 4 4
5 5 5 5 5
"""
        rows = 5
        for i in rang(1,row+1):
            print(*(i)*i)
"""
    Exercise 8: Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is the same after reverse. For example, 545, is the
palindrome numbers
"""
         num=input("enter your number:")
         num_string = string(num)
         if num_string == num_string[::-1]:
            print("this is a palindrome number")
         else:
            print("this is not a palidrome number")
"""
    Exercise 9: Create a new list from two list using the following condition
Create a new list from two list using the following condition
Given two list of numbers, write a program to create a new list such that the new list should
contain odd numbers from the first list and even numbers from the second list.
"""
          list1 = [1,3,7,8,10,13,15,18,19]
          list2 = [2,5,7,,11,12,14,16,17,20]
          new list = [] 
          for num in list1: 
              if num % 2 == 1: 
                  new list.append(num)
          for num in list2:
              if num %2 =0: 
                  new list.append(num)
          print("Our new list =", new_list)
 """
 exrcise 10: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
digits.
"""
          num=input("enter your number:")
          num_string=string(num)[::-1]
            print("a b c" .join(num_string))
