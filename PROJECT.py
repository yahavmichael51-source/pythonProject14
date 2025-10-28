liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    },
    "TIL FURTHER NOTICE": {
        "artist": "Travis",
        "duration": (4, 45),
        "genre": "Rap"
    },
    "Ghost town": {
        "artist": "Kanye",
        "duration": (2, 45),
        "genre": "Rap"
    },
    "Over": {
        "artist": "carti",
        "duration": (1, 45),
        "genre": "rap"
    }
}
def check_song(playlist, newsongs):
    for title, song in newsongs.items():
        playlist[title] = song
def search_song(liked_songs):
        while True:
            song_to_search = input(f'Enter song to search:')
            if song_to_search == ".":
                break
            if song_to_search in liked_songs:
                decision = input(f'Do you want to delete the song?')
                if decision == "yes":
                    del liked_songs[song_to_search]
                elif decision =="no":
                    pass
def delete_by_artist(liked_songs):
    songs_to_delete = []
    artist = input(f'enter the songs of the artist u want to delete')
    for song in (liked_songs):
        if liked_songs[song]["artist"] == artist:
            songs_to_delete.append(song)
    if songs_to_delete:
        for song in songs_to_delete:
            del liked_songs[song]



def main():

    pass


