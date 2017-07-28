# 25.07.2017
def make_album(name_artist, name_album, album_tracks=''):
    """Displays a description of the music album."""
    if album_tracks:
        info_album = {'artist': name_artist, 'album': name_album,
                      'tracks': album_tracks}
        return info_album
    else:
        info_album = {'artist': name_artist, 'album': name_album}
        return info_album


while True:
    print("\n(enter 'q' or 'Q' at any time to quit)")
    artist = input("Enter the artist name: ")
    if artist.lower() == 'q':
        break
    album = input("Enter the name of the album: ")
    if album.lower() == 'q':
        break

    artist_album = make_album(artist, album)
    print(artist_album)
