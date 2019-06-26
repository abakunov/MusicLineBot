import lyricsgenius
genius = lyricsgenius.Genius("7nsiYIJtBivganA-cnAWA0net-S6-fNrqjflYvkwVqYDqEIfiyLtm2llL-OxNZCz")
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]


def find_out(artist, song_name):
    song = genius.search_song(song_name, artist)
    a = {}
    try:
        a['song'] = song.title
        a['artist'] = song.artist
        a['text'] = song.lyrics
        print(song.lyrics)
    except AttributeError:
        a = {}

    return a


