import re
List = [(25, 13), (22, 19)]
# Given list
print("Orignal list : ", List)
temp = re.sub(r'[\[\]\(\), ]', '', str(List))
# Using set
result =  [int(i) for i in set(temp)]
# Result
print("Digits Extracted: ",result)
