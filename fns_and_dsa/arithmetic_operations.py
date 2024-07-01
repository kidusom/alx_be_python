def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    match operation :
            
     case 'add' :
           ans = num1 + num2
     case 'subtract' :
            ans = num1 - num2

     case 'multiply':
            ans = num1 * num2
     case 'divide' :    
            if num2 !=0: 
               ans =num1/num2
            else: print("second number cant be zero")            

     
    print(f"Result: {ans}")

if __name__ == "__main__":
    main()