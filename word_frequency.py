import string

from numpy import column_stack
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        with open(self.filename) as file:
            text_string = file.read()
        return text_string

        # return self.filename.readlines()

        raise NotImplementedError("FileReader.read_contents")


# praisesong = FileReader("praise_song_for_the_day.txt")
# print(praisesong.read_contents())


class WordList:
    def __init__(self, text):
        self.text = text

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        self.text = self.text.lower().strip().replace("\n", "").split(" ")
        transformed_words = []
        self.list = transformed_words
        for word in self.text:
            if word not in STOP_WORDS:
                transformed_words.append(word.strip(string.punctuation))
        return self.list
        raise NotImplementedError("WordList.extract_words")

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        counts = dict()
        for word in self.list:
            counts[word] = counts.get(word, 0) + len(word)
        return counts
        raise NotImplementedError("WordList.get_freqs")


# texty = WordList(praisesong)
# print(texty.text)


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        return print(*[str(k) + ' | ' + str(v) + " " + ("*" * v)
                       for k, v in sorted(self.freqs.items(), key=lambda x: x[1], reverse=True)], sep='\n')
        raise NotImplementedError("FreqPrinter.print_freqs")


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
