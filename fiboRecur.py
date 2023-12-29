def fibonacci(limit):
    '''Enter the limit of the fibonacci series'''
    
    if (limit == 0):
        return 0
    elif (limit==1):
        return 1
    elif (limit>1):
        
        return fibonacci(limit - 1)+fibonacci(limit - 2)
        


def main():
    '''Main function'''
    
    lim = int(input("Enter the limit of the fibonacci series : "))
    
    print(f"The fibonacci series for limit = {lim} is {fibonacci(lim)}")
    
    
    
main()          # calling the main function
