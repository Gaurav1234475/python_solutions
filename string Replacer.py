import re

def substitutor():
      
    sentence1 = "Python is very Hard."
    
    print(re.sub(r"Hard", "Easy", sentence1))
      
    sentence2 = "Thank you very much."
      
    print(re.sub(r"very", "so", sentence2))
  
substitutor()