def make_album(name_artist, name_album, album_tracks=''):
    """Displays a description of the music album."""
    if album_tracks:
        info_album = {'artist': name_artist, 'album': name_album,
                      'tracks': album_tracks}
        return info_album
    else:
        info_album = {'artist': name_artist, 'album': name_album}
        return info_album


artist_album = make_album('mari nakamoto', 'unforgettable!')
print(artist_album)
artist_album = make_album('isao suzuki trio', 'blow up')
print(artist_album)
artist_album = make_album('tsuyoshi yamamoto trio', 'misty!', 7)
print(artist_album)
