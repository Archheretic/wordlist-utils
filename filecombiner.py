import shutil

# Change the content of this list.
wordlist_to_combine = ['norwegianWords01.txt','ordliste_passord_topp_125.txt']

with open('combined_wordlist.txt','wb') as wfd:
    for f in wordlist_to_combine:
        with open(f,'rb') as fd:
            shutil.copyfileobj(fd, wfd, 1024*1024*10)