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
    def create(cls, name, artist, genre):
        # print("Count before creating song:", cls.count)

        obj = cls(name, artist, genre)
        cls.add_song_to_count()
        cls.add_to_genre(genre)
        cls.add_to_artists(artist)
        cls.add_to_genre_count(genre)
        cls.add_to_artists_count(artist)

        # print("Count after creating song:", cls.count)
        return obj   

s1 = Song.create("Surrender", "Man of God", "Gospel")
s2 = Song.create("Lose Yourself", "Eminem", "Rap")
s3 = Song.create("Thriller", "Michael Jackson", "Pop")
s4 = Song.create("Thr", "Jackson", "Rock")
s5 = Song.create("Empire State of Mind", "Jay Z", "Hip-Hop")
s6 = Song.create("Halo", "Beyonce", "Pop")
s7 = Song.create("Maneater", "Hall and Oates", "Pop")
s8 = Song.create("Smells Like Teen Spirit", "Nirvana", "Grunge")
s9 = Song.create("Rich Girl", "Hall and Oates", "Pop")

# print(s.name)
print(Song.count)
print(Song.genre_count)
print(Song.artist_count)

