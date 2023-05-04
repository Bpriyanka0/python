# Python code to find the URL from an input string
 
def Find(string):
    x=string.split()
    res=[]
    for i in x:
        if i.startswith("https:") or i.startswith("http:"):
            res.append(i)
    return res
             
# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))