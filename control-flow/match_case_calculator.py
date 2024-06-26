firstno = float(input("Enter the first number:"))  # type: ignore 

secondno = float(input("Enter the second number:")) # type: ignore

operation = input("Choose the operation (+, -, *, /):") # type: ignore  


match operation:

   case '+' :
        ans = firstno + secondno

   case '-' :
        ans = firstno -secondno

   case '*' :
       ans =  firstno * secondno

   case '/' :
        
        if secondno != 0:
            
         ans = firstno / secondno

        else:
        
         print('invalid')
   case SyntaxError:

    print('input error')
 
print(f'The result is{ans}')
  