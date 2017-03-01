from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import requests
from bs4 import BeautifulSoup
import scrapy
from lxml import html
from os.path import basename
from urllib.parse import urljoin
import re
import os
import random
import time

ALL_DYLAN = "urls-dylan.txt"

# RegEx compile
COPYRIGHT = '\n\nCopyright'
copyright_pattern = re.compile('[C|c]opyright')


# read all urls
with open(ALL_DYLAN, "r") as fin:
    all_urls = fin.read()

urls = all_urls.split('\n')

print("Total urls: ", len(urls))

count = 0 
# download each URL
for url in urls:
    # get filename
    print("Trying url: ", url)
    o_file = url.rsplit('/', 2)    # url is 'http://bobdylan.com/songs/abandoned-love/'
    o_file = o_file[1] + ".txt"    # output filename 'abandoned-love.txt'
    # if already downloaded, ignore it
    if os.path.exists(o_file):
        sz = os.path.getsize(o_file)
        if sz > 1:
            print("File exists: ", o_file)
            continue

    # open the url
    print("Fetch: ", url)
    res_html = requests.get(url).text
    soup = BeautifulSoup(res_html, "lxml")

    # parse the html
    soup_headline   = soup.find_all(class_="headline")
    soup_credit     = soup.find_all(class_="credit")
    soup_lyrics     = soup.find_all(class_="lyrics")

    # get text from first element. ASSUMES only 1 element of each
    txt_headline = ""
    txt_credit  = ""
    txt_lyrics  = ""
    if soup_headline is not None:
        txt_headline = soup_headline[0].text
    if soup_credit is not None:
        txt_credit  = soup_credit[0].text
    if soup_lyrics is not None:
        txt_lyrics = soup_lyrics[0].text

    # search and replace multiple tabs
    txt_headline    = "".join( txt_headline.split('\t') )
    txt_credit      = "".join( txt_credit.split('\t') )
    txt_lyrics      = "".join( txt_lyrics.split('\t') )
    # weird trick to put copyright statement on a new line
    txt_lyrics      = copyright_pattern.sub(COPYRIGHT, txt_lyrics)  

    # create output file
    with open(o_file, "wt") as fout:
        fout.write(txt_headline)
        fout.write('\n')
        fout.write(txt_credit)
        fout.write('\n')
        fout.write(txt_lyrics)
        fout.flush()
    print("Done: ", o_file)

    count += 1

    # sleep
    nsleep = random.randint(1, 6)
    print("Sleeping....", nsleep)
    time.sleep( nsleep)

print("--- Fetched files: ", count)



