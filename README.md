# food-server

I love trying out new places to eat at, but a problem I frequently encounter is WHERE DO I EAT? First I have to find a list of places that serve the cuisine I'm feeling at the moment, which involves either looking said cuisine on Google Places API, Yelp or seeing if there's a BlogTO article on it. Then I go down the rabbit hole of looking up reviews, price point, menu items, location of the place and finally end up going to Popeyes cause its close by and I know what's good there(3 piece chicken combo with a fuck ton of their spicy sauce on top). 

So I'm building this to help me find places just a tad bit quicker and easier. Based on the preferences, distance from the postal code, food-server will find you places that are in your price point and in the cuisine you're feeling. Furthermore, if you've got a list of places you've been meaning to hit up but never remember then food-server will pull those in(if relevant).

## Stack used:
- Flask for the backend server
- MongoDB for the DB
- ?? for the frontend
- Google Places + Yelp API for getting restaurants from

## Milestones

1. Fetching data from the Places + Yelp API
2. Saving/fetching user data from mongoDB
3. Able to suggest places based on user preferences 
4. Making the frontend
5. TBD
