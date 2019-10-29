import sys
print("Input the name: ", sys.argv[1])
string = sys.argv[1]
string = string.upper()
str = 0
for i in string:
  str += ord(i)
str = str^0x5678
str = str^0x1234
print("the passcode is : ", str)

print('Here is the demo for my case id')
string = "rxp"
print('the input is : ', string)
string = string.upper()
str = 0
for i in string:
  str += ord(i)
str = str^0x5678
str = str^0x1234
#print('the input is : ', string)
print("the passcode is : ", str)