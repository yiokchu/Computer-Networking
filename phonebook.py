class Phonebook(object):
    """Represents a phone book."""

    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        """Adds the name and number to the phone book."""
        self.entries[name] = number

    def get(self, name):
        """Returns the number if name is in the phone book,
        or None otherwise."""
        return self.entries.get(name, None)

    def __str__(self):
        """Returns the string representation of the phone book."""
        result = ""
        keys = list(self.entries.keys())
        keys.sort()
        for key in keys:
            result += key + ":" + self.entries[key] + "\n"
        return result


def main():
    """Testing function for PhoneBook."""
    book = Phonebook()
    for name in range(10):
        book.add("Name" + str(name), "524-4682")
    print(book)
    for name in range(10):
        print(book.get("Name" + str(name)))

if __name__ == "__main__":
    main()
