class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, members):
        if members in self.__myTeam:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.__myTeam)


def main():
    classmates = Teams(['John', 'Steve', 'Tim'])

    # prints the number of members in classmates
    # returns 3
    print(f"There are {len(classmates)} members in classmates")

    # checks if Tim and Sam are in classmates
    # returns False
    print(
        f"Tim and Sam are both in classmates is {'Tim' and 'Sam' in classmates}")

    # prints out the members
    # returns John, Steve, Tim
    print("The members of classmates are: ")
    name = iter(classmates)
    for name in classmates:
        print(f"\t- {name}")

    # check to see if classmates implements the _len_ method
    # returns True
    implements = "Classmates implements the __len__ method is"
    if hasattr(classmates, '__len__'):
        print(f"{implements} {True}")
    else:
        print(f"{implements}  {False}")


main()
