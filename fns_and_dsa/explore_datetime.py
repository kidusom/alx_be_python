from datetime import timedelta
from datetime import datetime

def display_current_datetime ():
  current_date = datetime.now()
  print(str(current_date))

def main():
   display_current_datetime()
    

if __name__ == '__main__':
  main() 
