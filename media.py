"""
Movie Review Program
"""

import webbrowser
import fresh_tomatoes

class Movie:
    """
    Movie class for reviews
    """
    def __init__(self, title, storyline, poster_image_url, trialer_youtube_url):
        self._title = title
        self._storyline = storyline
        self._poster_image_url = poster_image_url
        self._trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """
        Open a browser and play the trailer of the movie
        :return:
        """
        webbrowser.open(self._trailer_youtube_url)


def main():
    """
    Test Function
    """
    toy_story = Movie("Toy Story",
                      "A story of a boy and his toys that come to life",
                      "https://en.wikipedia.org/wiki/Toy_Story",
                      "https://www.youtube.com/watch?v=c3986gGp3Qs")
    #toy_story.show_trailer()
    movies.append(toy_story)
    movies.append(sing)
    # Test it
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
    exit(0)