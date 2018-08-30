Mel_Rent_Map
===
This script aims at finding where is a better place to rent a house in Melbourne. "Better" means there are more infrastructures around within a short distance, such as supermarkets, banks, GPs, etc.

How to draw the map:
---
I used gmplot which is based on Google Map, and is very easy to use. 
I drew circles to mark a infrastructure with a certain radius. Different color means different kind of infrastructure.\
Blue = Supermarkets (Woolworths & Coles)\
Black = Banks (CBA & ANZ)\
Red = GPs

The inner deeper area means a shorter distance (200m), the outer lighter area means a longer distance (1000m). The middle area means 500m.

How to get the data:
---
Just use Google API service. I used GooglePlaces library to get the coordinates of infrastructures. You will need to apply for Google API service to get an api_key if you would like to use GooglePlaces. There is a 12 months free trial for this service.

We used text_search function in GooglePlaces to search the key words. However, there is a 20 results limit in a page, so I used pagetoken to get more results, but the upper limit is 60 results.

Besides, during the usage of pagetoken, I have to add a 2 seconds' sleep, or there could be an Invalid Request Error.

The effect is shown below (A little ugly, LOL).
![Image text](https://raw.githubusercontent.com/SilenceGTX/Mel_Rent_Map/master/13.JPG)
