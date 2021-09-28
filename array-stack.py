# Andrea Joseph C00166106
# Certification of Authenticity:
# I certify that this assignment is entirely my own work. 


def main():
    

    #Create Empty List 
    stack = []
    isStackEmpty = bool(stack)

    #Display the Menu 
    print("A.Push a number (i.e., integer) on the top of the stack.")
    print("B.Pop a number (i.e., integer) from the top of the stack.")
    print("C.Display the value of the number (i.e., integer) on the top of the stack")
    print("D.Indicate whether the stack is EMPTY or NOT EMPTY")
    print("E.End program")
    print()

    #Get user Input 
    selection = input("Enter a letter that corresponds to the desired stack operation")

    #Loop until selection is E or display error message
    while selection !=  'e' or selection != 'E':
         if selection == 'A' or selection == 'a':
             stack.append(1)
             stack.append(3)
             stack.append(5)
             stack.append(7)
             print("Stack Push:",stack)
             print()
         
         elif selection == 'B' or selection == 'b':
             if len(stack) == 0:
                 print("Error! the stack is empty")
                 print()
             else:    
                 print("Stack Pop:",stack.pop())
                 print()
         
         elif selection == 'C' or selection == 'c':
             if len(stack) == 0:
                 print("Error! the stack is empty")
                 print()
             else:    
                 print("Top of the Stack:",stack[-1])
                 print()
         
         elif selection == 'D' or selection == 'd':
                if len(stack) == 0:
                    print(bool(stack))
                    print("Is the stack empty?", isStackEmpty)
                    print()
                else:
                   
                   print("Is the stack empty?",isStackEmpty)
                   print()
              
               
         elif selection == 'E' or selection == 'e':
             break
         else:
           print("Invalid Option! Please Enter A,B,C,D or E.")
           print()
           

         print("A.Push a number (i.e., integer) on the top of the stack.")
         print("B.Pop a number (i.e., integer) from the top of the stack.")
         print("C.Display the value of the number (i.e., integer) on the top of the stack")
         print("D.Indicate whether the stack is EMPTY or NOT EMPTY")
         print("E.End program")
         print()
               
         selection = input("Enter a letter that corresponds to the desired stack operation")        
         print()
    
main()
