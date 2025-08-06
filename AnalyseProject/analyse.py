file_name = input("Please enter the path to the .txt file: ")

try:
    with open(file_name, "r", encoding="UTF-8") as file:
        content = file.read()
        
        if content :
            print("There are informations in the txt file")
        else:
            print("There are not informations in the txt file")
        
except FileNotFoundError:
    print("❌ File not found. Please check the path and try again.")

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
    
    

def calculationChar():

   numberChar = len(content)
   print(numberChar)
   
   numberWords = content.split()
   print(len(numberWords))
   
   
   numberPhrase = 0
   
   for char in content :
       if char in [",", ".", "?", "!"]:
           numberPhrase += 1
    
   print(numberPhrase)
        
           
     
    
    








calculationChar()

        