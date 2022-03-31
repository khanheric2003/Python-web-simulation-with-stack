#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    This function prompts the user to enter the valid action ["=","<",">","q"]  
    Inputs: user's input
    Returns: valid user's action
    '''
    #delete pass and write your code here
    action = input("Enter = to enter a URL, < to go back, > to go forward, q to quit:")
    if action in ["=","<",">","q"]:
        return str(action)
    else:  
        raise Exception("Invalid entry")
    
def goToNewSite(current, bck, fwd):
    '''
    This function will get called when option "=" was chosen, ask user to enter new website and add it in the stack
    it will ask for user's web input then append it to the web list, then give current position of it 
    Inputs: current website, backward count and forward stack
    Returns: input website
    '''   
    #delete pass and write your code here
    website = input("URL:")
    bck.push(current)
    fwd.clear()
    return website
    
def goBack(current, bck, fwd):
    '''
    This function is called when the user enters '<' during getAction(). This function used to go back to the previous site

    Inputs: current website, backward count and forward stack
    Returns: error msg and current site or previous site
    '''    
    #delete pass and write your code here
    try:
        website = bck.pop()
        fwd.push(current)
        return website
    except Exception as e:
        print("cannot go back")
        return current


def goForward(current, bck, fwd):
    '''
    This function is called when the user enters '>' during getAction(). This function used to go to the above page
    Inputs: current website, backward count and forward stack
    Returns: error msg and current site or the site above it
    '''    
    #delete pass and write your code here
    try:
        website = fwd.pop()
        bck.push(current)
        return website
    except Exception as e:
        print("cannot go forward")
        return current

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == "<":
                current = goBack(current, back, forward)
            elif action ==">":
                current = goForward(current,back, forward)
            elif action == "q":
                quit = True 
                
            
            #TO DO: add code for the other valid actions ('<', '>', 'q')
            #HINT: LOOK AT LAB 4
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    