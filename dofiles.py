
import json
import time 
import csv
import pandas as pd
from rariblefindelement import RaribleFindElements 



class DoFiles(RaribleFindElements):
   
   

   def __init__(self):
      super().__init__()
      self.dico = {}
           
      
       #self.json_doc = str


          
   def auction_information(self):

      try:
      
       self.dico = {'name': self.name ,'prix': self.price,'description': self.descript,'deconte': self.decont}
       self.test_dataframe = pd.DataFrame(self.dico)
       print(self.test_dataframe)
       print("success")

      except:
          print("fail to put auction information on dictionnary")
          
          
   def do_csv_file(self):
       
      self.filename = "RARIBLE_NFT_INFORMATIONS.csv"
      try:
     
         self.write_csvfile = open(self.filename,"w",encoding="utf-8")
         self.test_dataframe.to_csv("RARIBLE_NFT_INFORMATIONS.csv")
      except:
         print("failed to print informations in csv file")
          
   def do_json_file(self):

      try:

         self.json_doc = json.dumps(self.dico,indent=2)
         print(self.json_doc)
           
         with open('RARIBLE_JSON_file.json',"w",encoding="utf-8") as self.json_file :
            json.dump(self.dico, self.json_file, indent=2)
               
      except:
         
         print("failed to print informations in json file") 
           
           
           
            


if __name__=='__main__':

  d1 = DoFiles()

  d1.fist_page()
  d1.rarible_click_explore_button()
  d1.rarible_click_onsale_button()
  d1.rarible_click_apply_botton()
  d1.select_element()
  d1.take_information()   
  d1.add_information()  
  d1.auction_information()    
  d1.do_csv_file()    
  d1.do_json_file()  


   

      