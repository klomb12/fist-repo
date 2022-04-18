
from ast import Try
from cgi import test
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd 
import json



class RaribleFindElements:
    """ class pour la recuperation des informations des nfts mis au enchere sur le site rarible.com  """ 
   
    
    def __init__(self):
     self.price =[]
     self.decont =[]
     self.descript =[]
     self.name =[]
     #on_sale = []
     self.dico = {}
     self.nom = ""
     self.prix= ""
     self.description = ""
     self.deconte = ""



    
        

    # fonction pour ouvrir le navigateur chrome et lancer le site rarible.com
    def fist_page(self):
      try:
        self.driver = webdriver.Chrome(ChromeDriverManager().install()) 
        self.driver.get('https://rarible.com/')
        self.driver.maximize_window()
        time.sleep(2)  # wait for the website for 2 second 

      except:
        print("error open page")
        self.re_init()
      

    def re_init(self):
      time.sleep(10)
      self.driver = webdriver.Chrome(ChromeDriverManager().install())
      self.driver.get('https://rarible.com/')
      self.driver.maximize_window()
        

    def rarible_click_explore_button(self):
        try:
          self.driver.find_element(By.XPATH,"//span[@class='sc-bdvvtL sc-hKwDye sc-eCImPb klyGzw'][normalize-space()='Explore']").click() # find explore button and click on it 
          self.driver.find_element(By.XPATH,"//span[@class='sc-bdvvtL sc-hKwDye sc-eCImPb cUywCO'][normalize-space()='Ethereum']").click()
          time.sleep(3)

        except:
          print("failed to click on explore or ethreuim button")
          self.re_click_explore_button()




    def rarible_click_onsale_button (self):

      try:
     
          self.driver.find_element(By.XPATH,"//span[contains(text(),'On sale')]").click()         
          self.driver.find_element(By.XPATH,"//div[normalize-space()='Buy now']").click()    
          time.sleep(3)
      except:
        self.re_click_onsale_button()
        


    def rarible_click_apply_botton(self):
      try:

          self.driver.find_element(By.XPATH,"//div[normalize-space()='Open for offers']").click()  
          self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply'] ").click()  
          time.sleep(5)

      except:

        self.re_click_apply_button()
        print("failed to click explore elements") 


    def re_click_explore_button(self):

       time.sleep(5)
       self.driver.find_element(By.XPATH,"//span[contains(text(),'On sale')]").click()         
       self.driver.find_element(By.XPATH,"//div[normalize-space()='Buy now']").click()    
          


    def re_click_onsale_button(self):

       time.sleep(5)
       self.driver.find_element(By.XPATH,"//div[normalize-space()='Open for offers']").click()  
       self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply'] ").click()  
      


    def re_click_apply_button(self):

       self.driver.find_element(By.XPATH,"//div[normalize-space()='Open for offers']").click()  
       self.driver.find_element(By.XPATH,"//button[normalize-space()='Apply'] ").click()  
       time.sleep(5)

      
    def select_element(self): 
        time.sleep(2)
        try:
          self.fist_element = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-cCcXHH ebRXgR clOqDW dbbKCr']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-jCHUfY eHCPOb clOqDW htmjuM']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-dFtzxp sc-brSvTw sc-cfJLRR ebRXgR clOqDW gSCbae EGfMV fgiRQY']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-ctqQKy ffQRNb clOqDW hrYNC']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-chSlKD ebRXgR clOqDW ckvJRQ']/div[@aria-label='grid']/div[@role='rowgroup']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]")
          self.achains = ActionChains(self.driver)
          self.achains.move_to_element(self.fist_element).perform()
          time.sleep(3)
          self.fist_element.click()
          time.sleep(10)

        except:
            print("failed to select the fist element")
            self.re_select_elements()


    def re_select_elements(self):

           self.r_fist_element = self.driver.find_element(By.XPATH,"//body/div[@id='root']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-cCcXHH ebRXgR clOqDW dbbKCr']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-jCHUfY eHCPOb clOqDW htmjuM']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-dFtzxp sc-brSvTw sc-cfJLRR ebRXgR clOqDW gSCbae EGfMV fgiRQY']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN ebRXgR clOqDW']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-ctqQKy ffQRNb clOqDW hrYNC']/div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN sc-chSlKD ebRXgR clOqDW ckvJRQ']/div[@aria-label='grid']/div[@role='rowgroup']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]")
           self.r_achains = ActionChains(self.driver)
           self.r_achains.move_to_element(self.t).perform()
           time.sleep(3)
           self.r_fist_element.click()
           time.sleep(10)


    # fonction mis en place pour retourner les informations dont on a besoin 
    def take_information(self):
  
        try:
          print("value",self.nom,self.prix,self.description,self.deconte)
          self.prix = self.driver.find_element(By.XPATH,"//div[@data-marker='root/appPage/token/sidebar/header']//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN kQBJUo clOqDW']").text
          self.description = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cdWESL clOqDW']").text
          self.deconte = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cSJSBE clOqDW']").text
          self.nom = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cdWESL clOqDW']").text
          print("after_value",self.nom.replace("\n",""),self.prix.replace("\n",""),"",len(self.prix),self.description,self.deconte)
          time.sleep(7)
        except:
          # planned to return on sale nft informations 
          print("error to take information")
          self.re_take_information()
          #self.add_on_bids_information()


    def add_information(self):
      
      
      try:

           # puting information in list
          self.name.append(self.nom)
          self.price.append(self.prix)
          self.decont.append(self.deconte)
          self.descript.append(self.description)
          time.sleep(5)
         
        
     
      except:
            print("failed to add informations")

    def re_take_information(self):

          self.nom = self.driver.find_element(By.XPATH,"//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN cdWESL clOqDW']").text
          self.on_sale = self.driver.find_element(By.XPATH,"//div[@data-marker='root/appPage/token/sidebar/header']//div[@class='sc-bdvvtL sc-gsDKAQ sc-dkPtRN kQBJUo clOqDW']").text
          
         
    def add_on_bids_information(self):
          self.name.append(self.nom)
          self.price.append(self.on_sale)
          time.sleep(5)
           

if __name__=='__main__':

  r1 = RaribleFindElements()

  r1.fist_page()
  r1.rarible_click_explore_button()
  r1.rarible_click_onsale_button()
  r1.rarible_click_apply_botton()
  r1.select_element()
  r1.take_information()   
  r1.add_information()  
  

       


         
         
