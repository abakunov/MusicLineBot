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
        a['url'] = song.url
        providers = song.media
        for provider in providers:
            if provider['provider'] == 'youtube':
                a['utube'] = provider['url']
    except AttributeError:
        a = 0

    return a


