# define an album dictionary
albums = {}


def make_album(artist, title, tracks=None):
    """Return a dictionary of information about an album."""
    album_dict = {
        "artist": artist.title(),
        "title": title.title(),
    }
    if tracks:
        album_dict["tracks"] = tracks
    return album_dict


# add a new album to the dictionary by using the make_album function passing the artist and title and tracks
albums["The Wall"] = make_album(
    "Pink Floyd", "The Wall", ["Another Brick in the Wall", "Comfortably Numb"]
)

# add album to the albums dictionary
albums["Dark Side of the Moon"] = make_album(
    "Pink Floyd", "Dark Side of the Moon", ["Time", "Money"]
)

# add album to the albums dictionary
albums["Appetite for Destruction"] = make_album(
    "Guns N' Roses",
    "Appetite for Destruction",
    ["Welcome to the Jungle", "It's So Easy"],
)

# write the album list to a file
with open("e:\\code\\album_list.txt", "w") as file:
    for album, album_info in albums.items():
        file.write(f"Album: {album}\n")
        for key, value in album_info.items():
            file.write(f"\t{key}: {value}\n")

# print the album dictionary
print("ablum structure:", albums)
for album, album_info in albums.items():
    print(f"\nAlbum: {album}")
    for key, value in album_info.items():
        print(f"\t{key}: {value}")

# print out all albums that begin with the letter "A" from the album dictionary
print("\nAlbums that begin with the letter 'A':")
for album, album_info in albums.items():
    if album_info["title"][0].lower() == "a":
        print(f"\t{album_info['title']}")
