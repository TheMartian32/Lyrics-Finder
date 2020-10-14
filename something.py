import webbrowser


def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue

        return inp


def find_lyrics():
    """
    Finds the lyrics of a song by redirecting you to a new URL by using the artist
    and song name.
    """

    # Finding artist and song name
    print('\n--------------------')
    artist = ask_for('Artist: ', _type=str)
    song = ask_for('Song: ', _type=str).lower()
    print('--------------------')

    # Formats song to fit URL
    def formatter(string_arg=str):
        """
        If theres a space in the name it adds a dash to fit the URL

        Args:
            string_arg (str, optional): String that should be an artist or song. Defaults to str.
        """
        # For every character in the string that was passed in
        for i in range(0, len(string_arg), 1):
            # If the character its iterating through is a space, do the following
            if string_arg[i] == ' ':
                # Replace the string at that index with a dash
                string_arg = string_arg.replace(string_arg[i], '-')
        # Return the newly formatted string
        return string_arg

    # Formats song and artist
    song = formatter(song)
    artist = formatter(artist)

    # Opens new formmated URL
    webbrowser.open(
        f'https://genius.com/{artist}-{song}-lyrics')


if __name__ == "__main__":
    print('\nYou wont be able to find every song on here.')
    find_lyrics()
    #  Executes at the end to see if the user wants to repeat the program.
    repeat = ''
    while True:
        #  Asks to repeat the script.
        print(
            '\nTyping Y will loop over the script, typing N will quit it.')
        repeat = ask_for('\n: ', _type=str).lower()

        if repeat[0] == 'y':
            find_lyrics()
            continue

        if repeat[0] == 'n':
            break
