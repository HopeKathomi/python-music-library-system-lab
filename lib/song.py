class Song:
    count = 0
    genres = []
    artists = set()
    genre_count ={}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls,artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def create(cls,name, artist, genre):
        obj = cls(name, artist, genre)
        cls.add_song_to_count()
        cls.add_to_genre(genre)
        cls.add_to_artists(artist)
        cls.add_to_genre_count(genre)
        cls.add_to_artists_count(artist)
        return obj    

s1 = Song.create("Lose Yourself", "Eminem", "Rap")
s2 = Song.create("Thriller", "Michael Jackson", "Pop")
s3 = Song.create("Empire State of Mind", "Jay Z", "Hip-Hop")
s4 = Song.create("Halo", "Beyonce", "Pop")
s5 = Song.create("Maneater", "Hall and Oates", "Pop")
s6 = Song.create("Smells Like Teen Spirit", "Nirvana", "Grunge")
s7 = Song.create("Rich Girl", "Hall and Oates", "Pop")
s8 = Song.create("Back in Black", "AC/DC", "Rock")

# print(s.name)
print(Song.count)
print(Song.genre_count)
print(Song.artist_count)

