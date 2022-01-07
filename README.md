# Amazon-Webscrape

## Webscrape amazon badge status using selenium


### Targeting this badge on amazon listings
![image](https://user-images.githubusercontent.com/89386946/148476118-cd0c93d2-0fb0-46e5-bbf3-5403bf03db14.png)


### Extracting these 2 pieces of data
![image](https://user-images.githubusercontent.com/89386946/148476061-aae6c534-5a3c-4947-b892-2fe59d5cf4da.png)

### Deploying
```
import badge_scrape

asins = ['']
data = badge_scrape(asins)

print(data)
    
```

### Returned
Ruturns a dictionary with the ASIN (sku) as the key, and the badge name/badge category as values
