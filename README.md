# Wordle Helper
This was a quick lunchtime project to see if I could create a simple Python program to help solve Wordle puzzles by filtering 
all the possible five-letter words according the information I have about _required_, _wrong_, and _known_ letters in a 
given Wordle puzzle.

You can [play Wordle](https://www.powerlanguage.co.uk/wordle/) online in your browser for free.

## Usage
This program utilizes the built-in word list on macOS located at `/usr/share/dict/words` by default. Specify a different source of words by specifying the `-d` commandline parameter. The program expects a file with one word per line.

There are three possible filters which can be used in any combination to reduce the number of possible words according to the
information you have based on your Wordle guesses.

```
% python3 wh.py --help
usage: wh.py [-h] [-d WORD_SOURCE] [-r REQUIRED_LETTERS] [-w WRONG_LETTERS]
             [-k KNOWN_LETTERS]

Filter possible Wordle solutions.

optional arguments:
  -h, --help            show this help message and exit
  -d WORD_SOURCE, --dict WORD_SOURCE
                        Specify the path to a list of dictionary words
  -r REQUIRED_LETTERS, --req REQUIRED_LETTERS
                        Specify the letters that are known to be present in
                        the word in a simple string. For example, 'xyz'.
  -w WRONG_LETTERS, --wrong WRONG_LETTERS
                        Specify the letters that are known to be missing in
                        the word in a simple string. For example, 'abc'.
  -k KNOWN_LETTERS, --known KNOWN_LETTERS
                        Specify positions of known letters using '_' for
                        missing letters. For example, '_er__'.
```

Here's an example of the Wordle puzzle from Jan. 25, 2022.

```
% python3 wh.py -r "ras" -w "eimton" -k "s__ar"
salar
sugar
2 possible words.
```
