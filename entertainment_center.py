import fresh_tomatoes
import media

# Creates an instance for each movie shown on the site.
# Calls the Movie class from the media module for each instance,
# and the __init_ function for the Movie class gets called.


the_empire_strikes_back = media.Movie("The Empire Strikes Back",
                                      "The epic sequal to Star Wars.",
                                      "http://bit.ly/1Ksk2Ya",
                                      "https://www.youtube.com/watch?v=8Hm-9Sai9To",
                                      "Harrison Ford, Carrie Fisher, Mark Hamill")


the_big_lebowski = media.Movie("The Big Lebowski",
                               "A story of a man and his rug.",
                               "http://bit.ly/1Ksk8Pn",
                               "https://www.youtube.com/watch?v=cd-go0oBF4Y",
                               "Jeff Bridges, John Goodman, Steve Buscemi")

star_wars = media.Movie("Star Wars",
                        "A long time ago in a galaxy far far away...",
                        "http://bit.ly/1gS401T",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k",
                        "Harrison Ford, Carrie Fisher, Mark Hamill")

raising_arizona = media.Movie("Raising Arizona",
                              "A story about family",
                              "http://bit.ly/1LgnUOD",
                              "https://www.youtube.com/watch?v=2AIfVoGUs6c",
                              "Nicolas Cage, Holly Hunter")

the_avengers = media.Movie("The Avengers",
                           "A team of super heros save the world!",
                           "http://bit.ly/1flJV3d",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                           "Robert Downey Jr, Scarlett Johansson, Chris Evans")

french_kiss = media.Movie("French Kiss",
                          "A love story with diamonds. In France",
                          "http://bit.ly/1KskkOL",
                          "https://www.youtube.com/watch?v=N3W5oAOZAWY",
                          "Meg Ryan, Kevin Kline")

# Creates a list of the movies and calls the open_movies_page method from the fresh_tomatoes file.

movies = [the_empire_strikes_back, the_big_lebowski, star_wars,
          raising_arizona, the_avengers, french_kiss]
fresh_tomatoes.open_movies_page(movies)


