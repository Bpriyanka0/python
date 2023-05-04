dic = {'study': [5, 3, 7], 
             'to': [11, 4, 2, 6], 
             'night': [10, 9]}
  
# print original dictionary
print("The original dictionary is : " ,dic)
  
# Sort Dictionary key and value List
# Using sorted() and loop
sort_dict = {}
for key in sorted(dic):
    sort_dict[key] = sorted(dic[key])
  
# printing result 
print("The sorted dictionary : " , sort_dict) 
