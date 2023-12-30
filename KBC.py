import time

def questions():
    '''This function contains questions'''
    
    quest = ["Q.1] Who is the creator of the Linux Kernel?", "Q.2] When did Chandrayan-3 land on moon?", "Q.3] Who was the creator of JavaScript?", "Q.4] What type of language is python?", "Q.5] What Desktop Environment does Ubuntu 22.04 use?"]
    
    optionss = ["Linus Torvalds", "Harry", "Mark Zuckerberg", "John Wick", "23 March 2023", "2 January 2022", "23 August 2023", "15 July 2022", "Bill Gates", "Tim Cook", "Guido Rossum", "Brendan Eich", "Compiled", "Interpreted", "Assembled", "Low-Level", "Gnome", "MATE", "Cinnamon", "XFCE"]
    
    answerss = ["Linus Torvalds", "23 August 2023", "Brendan Eich", "Interpreted", "Gnome"]
    
    asker(quest, optionss, answerss)
    
    # answers(optionss)
    
def answers(optioning,count):
    '''This function gives out the options'''
    
    print("Your options are : \n")
    
    lettering = ['A', 'B', 'C', 'D']

    coun = 0
    counting = count
    for i in range(2):
        
        for j in range(2):
            
            print(f"Option {lettering[coun]} : {optioning[counting]}\t\t", end=" ")
            coun+=1
            counting+=1
        
        print("\n")

def changekaro(jawablo):
    '''To test case the jawab's'''
    
    match jawablo:
        
        case 'A':
            return 0
        
        case 'B':
            return 1
            
        case 'C':
            return 2
            
        case 'D':
            return 3
            
        case _:
            
            raise ValueError("Only Option Subscript is permissible!")
    
    
    
    
def asker(quest, optioning, answersing):
    '''This function asks the questions'''
    
    correctIndex = 0
    jeetgaya = 0
    kitnaMila = 100
    paisa = []
    indexCounter = 0
    sahiindexCounter = 0
    count = 0
    for i in quest:
        
        print(f"\n\n\n{i}\n")
        
        answers(optioning, count)
        count+=4
        jawablo = input("Please enter the Option Subscript : ")
        
        nautankiVar = changekaro(jawablo.upper())
        
        indexCounter = sahiindexCounter + nautankiVar
        
        if(indexCounter>3):
            indexCounter+=1
        else:
            pass
        
        
        if(optioning[indexCounter]==answersing[correctIndex]):
            print("\n" + f"Correct Answer! You have won {kitnaMila} Rs!".center(100, " "))
            paisa.append(kitnaMila)
            kitnaMila *=10
        else:

            print("\n" + "Oh no! Your answer is incorrect...".center(100, " "))
            

        correctIndex+=1

        if(sahiindexCounter == 0):
            sahiindexCounter+=3
        else:
            sahiindexCounter+=4
            
        time.sleep(3)
        
    else:
        for i in paisa:
            jeetgaya +=i
        
        print()    
        print("\n" + "THE GAME HAS ENDED!!!".center(100, " "))
        time.sleep(3)

        if(jeetgaya>0):

            print("\n" + f"CONGRATULATIONS! You have WON RS {jeetgaya} INR!!!".center(100, " "))
        else:
            print("\n" + "HAHAHA WOH DEKHO GAREEB!!!".center(100, " "))

def main():
    '''This is the main function'''
    
    print("Welcome to KBC!".center(100," "))
    
    questions()
    
    
    
main()
