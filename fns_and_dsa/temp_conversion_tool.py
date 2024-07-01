CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(temp):
  return temp * CELSIUS_TO_FAHRENHEIT_FACTOR 

def convert_to_fahrenheit(temp):   
  return temp * FAHRENHEIT_TO_CELSIUS_FACTOR

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