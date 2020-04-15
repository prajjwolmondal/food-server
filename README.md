# food-server

I love trying out new places to eat at, but a problem I frequently encounter is WHERE DO I EAT? First I have to find a list of places that serve the cuisine I'm feeling at the moment, which involves either looking said cuisine on Google Places API, Yelp and/or seeing if there's a BlogTO article on it. Then I go down the rabbit hole of looking up reviews, price point, menu items, location of the place and finally end up going to Popeyes cause its the best and I know what to get there (3 piece chicken combo with a fuck ton of their spicy sauce on top). 

So I'm building this to help me find places quicker and easier. Based on the preferences, distance from the postal code, food-server will find you places that are in your price point and in the cuisine you're feeling. Furthermore, if you've got a list of places you've been meaning to hit up but never remember then food-server will pull those in(if relevant).

## Stack used:
- Flask for the backend server
- MongoDB for the DB
- ?? for the frontend
- Google Places API
