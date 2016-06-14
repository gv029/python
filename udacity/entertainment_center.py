import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story", "Toys come to life", "https://a.dilcdn.com/bl/wp-content/uploads/sites/25/2014/01/toy-story-poster.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = movie.Movie("Avatar", "A marine visits an alien planet", "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg", "https://www.youtube.com/watch?v=uZNHIU3uHT4")
star_wars_VII = movie.Movie("Star Wars: The Force Awakens", "Space opera and lightsabers","http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster.jpg","https://www.youtube.com/watch?v=sGbxmsDFVnE")

movies = [toy_story, avatar, star_wars_VII]
fresh_tomatoes.open_movies_page(movies)
