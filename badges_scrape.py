from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def badge_scrape(asins: list,path: str):
    #add your asins in this list
    
    #create an empty list
    asin_link = []
    
    #create links with super link
    for i in asins:
        link_start = 'https://www.amazon.com/dp/'
        link = link_start + i
        asin_link.append(link)
    
    #create dict from lists
    asin_list = dict(zip(asins, asin_link))
    
    #empty list for returned val
    value_list = []
    
    #path to webdriver
    driver = webdriver.Edge(path)
    
    #For loop to extract data
    for key in asin_list:
       
        #get link for asin
        link = str(asin_list[key])
    
        #try to find the best sellers badge
        try:
            #execute link
            driver.get(link)
            #find element
            badge=driver.find_element(By.CLASS_NAME,"ac-badge-wrapper").text
        
            #format element
            x = int(badge.find('by'))
            badge.strip('  ')
            badge = (badge.replace("\n", " "))
            badge = badge[0:x]
            badge = badge.replace('for','in')
            badge = badge.split('in',1)
            
            #more filtering of returned data
            try:
                badge = badge.split('for')
            except:
                pass        
            badge_list = []
            for i in badge:
                badge = i.strip()            
                badge_list.append(badge)
            value_list.append(badge_list)
        
        except:
            
            #try to find the #1 badge
            try:
                #execute link
                driver.get(link)
                
                #find element
                badge=driver.find_element(By.CLASS_NAME,"badge-link").text
               
                #formatting
                badge = badge.split('in',1)
                badge_list = []
                for i in badge:
                    badge = i.strip()
                    badge_list.append(badge)
                value_list.append(badge_list)
    
            #define if no badges
            except:
                na_val = 'N/A N/A'
                na_val = na_val.split(' ')
                value_list.append(na_val)
    
    #put results in dict
    return_dict = dict(zip(asin_list,value_list))
    return_string = json.dumps(return_dict)
    
    return return_string

