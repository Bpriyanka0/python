from statistics import mean 

inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88] 
list_avg = mean(inp_lst) 

print("Average value of the list:\n") 
print(list_avg) 
print("Average value of the list with precision upto 3 decimal value:\n")
print(round(list_avg,3))
