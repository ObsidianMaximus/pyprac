def checkingForInt(a):
    '''This method is there to check if the value entered is between 5 and 9 or not.'''
    
    try : 
        
        int(a)
    
    except:
        
        raise ValueError("Only integer input is allowed.") from None
        
        # to avoid another exception inside of an exception, follow as in doc https://peps.python.org/pep-0409/
        
    if(int(a)<5 or int(a)>9):
            
        raise ValueError("Incorrect value entered, please adhere to the statement asked.")
    
   
    if(int(a)>=5 and int(a)<=9):
        
        print("\nThe number is valid.")
        
    
    print("\nThe program executed successfully. Thank you.")
  
    


def main():
    '''This is the main function'''
    
    a = input("Enter a number between 5 and 9 [or type 'quit' to exit the program] : ")
        
    if (a.lower()=="quit"):
        print("\nExiting the program ...\n")
        exit(0)
        
    else:
        
        # print(checkingForInt.__doc__)
        checkingForInt(a)       # calling the checking function
        
# print(main.__doc__)
main()                  # calling the main function




'''
More on the exception part at line 8 - https://stackoverflow.com/questions/52725278/during-handling-of-the-above-exception-another-exception-occurred

raise <Exception> from <Context Exception> is the syntax. The "context" is basically the "parent" of the exception you are creating. By default the parent context is the previous exception in the call stack (the one caught by except:). So by explicitly setting context to None we say "do not provide any previous context". Which means that our final syntax for throwing clean exceptions inside our "except-catcher blocks" is raise <the new exception> from None. 
'''
