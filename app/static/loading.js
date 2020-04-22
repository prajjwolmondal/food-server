// NOT USED CURRENTLY

function fetch_places_data(){
	axios.get("/fetch_google_restaurants")
	.then(data => {
		console.log('FETCH JS');
		console.log(data.data);
		return data.data;
	})
	.then(data => {
		axios.post("/redirect_search", {
			cuisine: data.cuisine,
			restaurant_list: data.restaurant_list,
			next_page_token: data.next_page_token
		})
	})
}

window.onload = fetch_places_data;