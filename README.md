# Amazon-Webscrape

## Webscrape amazon badge status using selenium


### Targeting this badge on amazon listings
![image](https://user-images.githubusercontent.com/89386946/148476118-cd0c93d2-0fb0-46e5-bbf3-5403bf03db14.png)


### Extracting these 2 pieces of data
![image](https://user-images.githubusercontent.com/89386946/148476061-aae6c534-5a3c-4947-b892-2fe59d5cf4da.png)

### Import the needed modules
  ```
  
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  import json
  
  ```

### Generate links
```
asin_link = []

#create links with super link
for i in asins:
    link_start = 'https://www.amazon.com/dp/'
    link = link_start + i
    asin_link.append(link)
    
```






### Returned
Ruturns a dictionary with the ASIN (sku) as the key, and the badge name/badge category as values
