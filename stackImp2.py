def main():
    stack = []

    #Push    
                       
    #Display Menu
    print("A.Push a number (i.e., integer) on the top of the stack.")
    print("B.Pop a number (i.e., integer) from the top of the stack.")
    print("C.Dispslay the value of the number (i.e., integer) on the top of the stack")
    print("D.Indicate whether the stack is EMPTY or NOT EMPTY")
    print("E.End program")

    #Get user input
    selection = input("Enter a letter that corresponds to the desired stack operation")
   

    #Loop as long as selection is not E/e
    while selection != 'E' or 'e':
    print("A.Push a number (i.e., integer) on the top of the stack.")
    print("B.Pop a number (i.e., integer) from the top of the stack.")
    print("C.Dispslay the value of the number (i.e., integer) on the top of the stack")
    print("D.Indicate whether the stack is EMPTY or NOT EMPTY")
    print("E.End program")
        if selection == 'A' or selection == 'a':
           stack.append(1)
           #print("Stack Push:",stack)
           stack.append(3)
           #print("Stack Push:",stack)
           stack.append(5)
           #print("Stack Push:",stack)
           stack.append(7)
           print("Stack Push:",stack)
           break 
           
        elif selection == 'B' or selection == 'b':
             stack.append(1)
             stack.append(3)
             stack.append(5)
             stack.append(7)
             
             print("Stack Pop:",stack.pop())
             break
        elif selection == 'C' or selection == 'c':
            print("Top of the Stack:",stack[-1])
            break 
           
        elif selection == 'D' or selection == 'd':
            if len(stack) == 0:
                print("The stack is EMPTY!")
            else:
                 print("The stack is NOT EMPTY,",stack)
        selection = input("Enter a letter that corresponds to the desired stack operation")        
             
             # print("D.Indicate whether the stack is EMPTY or NOT EMPTY")
main()
