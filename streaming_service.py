##
# streaming service.py
# You have found recent employment at a Movie streaming service and have
# the task to create a program that will keep track of all the Movies on
# the site. You decide that you will implement a system in Python that will
# allow you to keep track of all the movies, along with how long each one
# lasts. You realise that this should be automatic, but for this early
# prototype, you are happy to enter data by hand.

# Eddie Wallace
# Started: 24/05/2021


def force_int(msg=str, min=-1, max=int):
    """forces the user to input a intiger within the specified range

    Args:
        msg (str): the meassage that will appear to the user when
        they are providing an input
        min (int, optional): the minimum valid value. Defaults to -1.
        max (int): the maximum valid value

    Returns:
        int: [description]
    """
    valid = False
    intiger = min - 1
    while not valid:
        valid = True
        try:
            intiger = int(input(msg))
        finally:
            if intiger < min or intiger > max:
                valid = False
    return intiger


class Movie:
    LONGEST_MOVIE_LEN_S = 172800
    SHORTEST_MOVIE_LEN_S = 101

    def format_len(length_s=int) -> dict:
        """Formats the length of the Movie from S to H:M:S

        Args:
            length_s (int): length of the movie in seconds

        Returns:
            dict: teh formatted length of the movie
        """
        mins, secs = divmod(length_s, 60)
        hrs, mins = divmod(mins, 60)
        formated_length = (hrs, mins, secs)
        return formated_length

    def __init__(self, name=str, length_s=int) -> None:
        """Builder for the Movie object

        Args:
            name (str): the name of the Movie
            length_s (int): teh length of the Movie in seconds
        """

        self.name = name
        self.length_s = length_s
        self.formated_len = Movie.format_len(length_s)

    def change_len(self, new_len_s=int):
        """Changes the length of the Movie in s then calls
        the format_len method

        Args:
            new_len_s (int): the new length of the movie in seconds
        """
        self.length_s = new_len_s
        self.formated_len = Movie.format_len(new_len_s)


def add_movie(movies=dict):
    LEN_MSG = 'what is the length of the movie in S must be a positive int:\n'
    movie_name = input('What is the name of the movie:\n').lower()
    if movie_name not in movies:
        movie_len = force_int(LEN_MSG, Movie.SHORTEST_MOVIE_LEN_S,
                              Movie.LONGEST_MOVIE_LEN_S)
        movies[movie_name] = Movie(movie_name, movie_len)
    else:
        print('movie already exists')

    return movies


def edit_len(movies=dict):
    NEW_LEN_MSG = 'What is the new len of the movie must be positive int\n'
    movie_name = input('What is the name of the movie\n').lower()
    if movie_name in movies:
        new_len = force_int(NEW_LEN_MSG, Movie.SHORTEST_MOVIE_LEN_S,
                            Movie.LONGEST_MOVIE_LEN_S)
        movies[movie_name].change_len(new_len)
    return movies


def del_movie(movies=dict):
    movie_name = input('What is the name of the movie\n').lower()
    if movie_name in movies:
        del movies[movie_name]
        print('Movie successfully deleted')
    else:
        print('movie not registered')
    return movies


def get_len(movies):
    movie_name = input('What is the name of the movie\n').lower()
    if movie_name in movies:
        print(f'Length S: {movies[movie_name].length_s}, '
               'Length formatted: '
              f'{":".join(movies[movie_name].formated_len)}')


def print_all_info(movies):
    print("List of all movies with corresponding info:")
    for movie in movies.values():
        print(f'Name: {movie.name}, Length (S): {movie.length_s}, Length '
              f'Formatted: {":".join(movie.formated_len)}')


def menu():
    movie_dict = {}
    POS_CHOICES = ['a', 'd', 'e', 'l', 'p', 'q']
    while cont := input('Would you like to continue(Y|N)\n').lower() == 'y':
        print("""
Please enter:
(A) to Add a movie
(D)	to Delete a movie
(E)	to Edit the length of a movie
(L)	to get the Length of a movie
(P)	to print out all the movies and their times
""")
        choice = input().lower().strip()
        if choice not in POS_CHOICES:
            print('Invalid input')
        elif choice == 'a':
            movie_dict = add_movie(movie_dict)
        elif choice == 'd':
            if len(movie_dict) > 0:
                movie_dict = del_movie(movie_dict)
            else:
                print('there are no movies registered')
        elif choice == 'e':
            edit_len(movie_dict)
        elif choice == 'l':
            get_len(movie_dict)
        elif choice == 'p':
            print_all_info(movie_dict)
        else:
            print('ERROR')


if __name__ == '__main__':
    menu()
