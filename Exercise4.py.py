string = input ("Entre a string: ")
n = int(input("Entre the number of character to remove: "))
#jo hum remove value dy gy usko string k words se kam hna chaiay
if n < len(string):
#string k bad bracket mn n ka mtlb h k humare pas remove words k sath string likhi ae or colon ka mtlb hy bad valy words ae
    result = string[n:]
    print("output:", result)
else:
    print("n must be less than the length of the string.")