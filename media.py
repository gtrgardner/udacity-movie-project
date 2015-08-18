import webbrowser

# Create a class named Movie.

class Movie():
    """This class stores movie related information: The movie title,
    a story tagline, image url, trailer url, and the movie's stars."""
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, starring):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.stars = ("Starring ") + starring
# Play the movie trailer.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
