#-------------Date de creation: 09 avril 2022 ---------------------------
#-------------By Josias Sehi ==> lomb12 ----------------------------------
#----------------- DESCRIPTION DU SCRIPT ----------------------------------------
""" FR : Ce script est destiné a faire du webscraping. 
     son but principale sera d'aller sur le site de vente des NFT tel que rarible.com
     afin de recolter des informations relatives a des NFTs particulierement au encheres
     et nous les renvoyer.
     
    EN: This script is intended for webscraping.
     his main goal will be to go to the NFT sales site such as rarible.com
     in order to collect information relating to NFTs, particularly at auction
     and send them back to us.     
"""
import argparse
from tkinter import Menu
from dofiles import DoFiles


class RaribleMenu(DoFiles): 

    def __init__(self):
          super().__init__()


    def user_menu(self):

        parser = argparse.ArgumentParser()
        parser.add_argument("nftdescr",help ="le resumé des informations du nft")
        args = parser.parse_args()
        print(args.nftdescr)


    def launch_rarible_find_element_page(self):

        self.fist_page()
        self.rarible_click_explore_button()
        self.rarible_click_onsale_button()
        self.rarible_click_apply_botton()
        self.select_element()
        self.take_information()   
        self.add_information()
       

    def launch_dofiles(self):
        self.auction_information()
        self.do_csv_file()
        self.do_json_file()



 
    # pont d'entrée de notre script 
    def main(self):
       try:
         self.user_menu()
         self.launch_rarible_find_element_page()
         self.launch_dofiles()
         self.driver.close()
       except:
           print("FIN DU PROGRAMME")
           self.driver.quit()

# instanciation de la class 
# acces a la fonction principale 

   
if __name__ == '__main__':       
   
    m1 = RaribleMenu()
    m1.main()
