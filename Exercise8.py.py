num = input("Entre your number: ")
#num ko hum string mn convert kr rhy hyn ta k wo easy reverse ho sky
#phla colon position show krta hy or dusra colon sequence show krta hy or -1 ka mtlb hy reverse direction
num_str = str(num)
if num_str == num_str[::-1]:
   print("This is a palindrome number")
else:
     print("This is not a palindrome number")