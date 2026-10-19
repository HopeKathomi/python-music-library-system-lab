class Song:
    count = 0
    genres = []
    artists = set()
    genre_count ={}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genre(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls,genre):
        count = 0
        count += 1
        cls.genre_count[genre] = count

    @classmethod
    def add_to_artists_count(cls,artist):
        count = 0
        count += 1
        cls.artists_count[artist] = count

    @classmethod
    def create(cls,name, artist, genre):
        obj = cls(name, artist, genre)
        cls.add_song_to_count()
        cls.add_to_genre(genre)
        cls.add_to_artists(artist)
        cls.add_to_genre_count(genre)
        cls.add_to_artists_count(artist)
        return obj
    
s1 = Song.create("Surrender", "Man of God", "Gospel")
s2 = Song.create("Lose Yourself", "Eminem", "Rap")
s3 = Song.create("Thriller", "Michael Jackson", "Pop")
s4 = Song.create("Thr", "Jackson", "Rock")
# print(s.name)
print(Song.count)
print(Song.genre_count)
print(Song.artists_count)

