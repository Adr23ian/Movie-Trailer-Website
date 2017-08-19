import fresh_tomatoes   # Imports the fresh_tomatoes.py file and its contents
import media            # Imports the media.py file and its contents

# Below are my favorite movie instances - all related to Math & Fight

beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "From the heights of notoriety to the depths of \
    depravity, John Nash Jr. a mathematical genius \
    experienced it all.",
    "https://upload.wikimedia.org/wikipedia/en/b/b8"
    "/A_Beautiful_Mind_Poster.jpg",
    "https://www.youtube.com/watch?v=JV2PSWSyi0s")

good_will_hunting = media.Movie(
    "Good Will Hunting",
    "Will Hunting has a genius-level IQ but \
    chooses to work as a janitor at MIT.",
    "https://upload.wikimedia.org/wikipedia/en/b/"
    "b8/Good_Will_Hunting_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=QSMvyuEeIyw")

rain_man = media.Movie(
    "Rain Man",
    "Raymond has savant syndrome and adheres to strict routines.",
    "https://upload.wikimedia.org/wikipedia/en"
    "/b/b2/Rain_Man_poster.jpg",
    "https://www.youtube.com/watch?v=KKC3W0awjm0")

the_imitation_game = media.Movie(
    "The Imitation Game",
    "Based on the real life story of legendary \
    cryptanalyst Alan Turing.",
    "https://upload.wikimedia.org/wikipedia/en"
    "/5/5e/The_Imitation_Game_poster.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM")

october_sky = media.Movie(
    "October Sky",
    "From the coal mine to outer space",
    "https://upload.wikimedia.org/wikipedia/en/7"
    "/73/October_sky_poster.jpg",
    "https://www.youtube.com/watch?v=zxJQgYPXjN4")

gladiator = media.Movie(
    "Gladiator",
    "Maximus is a powerful Roman general, loved by the \
    people and the aging Emperor, Marcus Aurelius.",
    "https://upload.wikimedia.org/wikipedia/en"
    "/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=owK1qxDselE")

# List of my favorite movie objects
movies = [beautiful_mind, good_will_hunting, rain_man,
          the_imitation_game, october_sky, gladiator]

# Generates My Favorite Movies website
fresh_tomatoes.open_movies_page(movies)
