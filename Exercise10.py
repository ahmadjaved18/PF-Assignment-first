num = input("Entre your number: ")
#num ko hum string mn convert kr rhy hyn ta k wo easy reverse ho sky
#phla colon position show krta hy or dusra colon sequence show krta hy or -1 ka mtlb hy reverse direction
num_str = str(num)[::-1]
#join humare pas python ka ek function hy
print("a b c ".join(num_str))
