# Python3 program to implement
# the above approach
 
# Function to calculate the
# salary of the person
def computeSalary( basic, grade):
     
    hra = 0.2 * basic
    da = 0.5 * basic
    pf = 0.11 * basic
     
    # Condition to compute the
    # allowance for the person
    if grade == 'A':
        allowance = 1700.0
    elif grade == 'B':
        allowance = 1500.0
    else:
        allowance = 1300.0;
     
    gross = round(basic + hra + da +
                    allowance - pf)
                     
    return gross
 
# Driver code
if __name__ == '__main__':
     
    basic = 10000
    grade = 'A'
     
    # Function call
    print(computeSalary(basic, grade));