"""The Movie class to store each of my favorite movie attributes."""
import webbrowser


class Movie():

    """The constructor of the Movie class, initializes each instances."""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens a webbrowser to show each movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
