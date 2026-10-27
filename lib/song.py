
class Song:
    count = 0
    genres = []
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update the total number of songs
        Song.count += 1

        # Keep track of unique genres
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Keep track of unique artists
        Song.artists.add(artist)

        # Count songs per genre
        Song.genre_count[genre] = (
            Song.genre_count.get(genre, 0) + 1
        )

        # Count songs per artist
        Song.artist_count[artist] = (
            Song.artist_count.get(artist, 0) + 1
        )

    @classmethod
    def create(cls, name, artist, genre):
        return cls(name, artist, genre)


Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")
