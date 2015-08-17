import fresh_tomatoes
import media

# Creates an instance for each movie shown on the site.
# Calls the Movie class from the media module for each instance,
# and the __init_ function for the Movie class gets called.


the_empire_strikes_back = media.Movie("The Empire Strikes Back",
                        "the epic sequal to Star Wars.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/SW_-_Empire_Strikes_Back.jpg/220px-SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=8Hm-9Sai9To")


the_big_lebowski = media.Movie("The Big Lebowski",
                     "A story of a man and his rug.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/3/35/Biglebowskiposter.jpg/220px-Biglebowskiposter.jpg",
                     "https://www.youtube.com/watch?v=cd-go0oBF4Y")

star_wars = media.Movie("Star Wars","A long time ago in a galaxy far far away...",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
                             "https://www.youtube.com/watch?v=1g3_CFmnU7k")

raising_arizona = media.Movie("Raising Arizona", "A story about family",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/3/31/Raising-Arizona-Poster.jpg/220px-Raising-Arizona-Poster.jpg",
                          "https://www.youtube.com/watch?v=2AIfVoGUs6c")

the_avengers = media.Movie("The Avengers","a team of super heros save the world!",
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",
                                  "https://www.youtube.com/watch?v=eOrNdBpGMv8")

french_kiss = media.Movie("French Kiss","A love story with diamonds. In France",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/French_Kiss_film.jpg/220px-French_Kiss_film.jpg",
                           "https://www.youtube.com/watch?v=N3W5oAOZAWY")

# Creates a list of the movies and calls the open_movies_page method from the fresh_tomatoes file.

movies = [the_empire_strikes_back, the_big_lebowski, star_wars, raising_arizona, the_avengers, french_kiss]
fresh_tomatoes.open_movies_page(movies)


