import webbrowser


class Movie():
    def __init__(self, movie, movie_storyline, poster, trailer_youtube):
        # create a method with self and 4 other parameters
        self.title = movie
        self.storyline = movie_storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube
        # assign the values to another variables with self

        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
            # declare webbrowser.open to play the trailer
