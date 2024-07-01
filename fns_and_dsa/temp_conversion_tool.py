C_TO_F = 0.555
F_TO_C= 1.8

def convert_to_celsius(temp):
  return temp * C_TO_F  

def convert_to_fahrenheit(temp):   
  return temp * F_TO_C

def main():
 while True:
  temp = int(input('Enter the temperature to be converted:'))
  temp_type = input('Is this temperature in Celsius or Fahrenheit? (C/F):')
  if temp_type == 'C':
      ans = convert_to_fahrenheit(temp)
  else : 
      ans = convert_to_celsius

  print(ans)      
  
if __name__ == "__main__":
  main()        