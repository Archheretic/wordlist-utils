# wordlist-utils

#### Small utility programs that can be used to create or improve wordlists for password cracking.

## Quick Instructions

### filecombiner.py
Use this to combine wordlist, check filecombiner.py for instructions.

### simple_permutator.py
Use this to create permutations of different word combinations.

### wordlist_validator.py
Use this to create a valid Wordpress MD5 wordlist from a random wordlist.
This program might generate too many digit variations of a a single passwords, if the wordlist gets
too big then remove some of the loops in function:  def add_digits(password)

### wordList_num_appender.py
You should most likely use wordlist_validator.py instead of this.
This can be used to add numbers to the end of each word in a wordlist, it will also
turn the first character of any word into uppercase.

### Other tips:
To remove duplicates in a wordlist
$ sort wordlistContainingDupes.text | uniq > wordListWithoutDupes.txt
