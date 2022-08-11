"""this module contains
text descrpitons,
pictures for the application"""

from enum import Enum
from pathlib import Path


class TextDescription(Enum):

    HEADER = "<h1 style='text-align: center;" \
             "color: blue;'>BOB DYLAN SONGS APP</h1>"

    IMAGE = "images/bob_dylan_photo_wordcloud.png"

    DESCRIPTION = """
    <b>DESCRIPTION</b> \
    \n
    This app enables you to see Bob Dylan songs distribution by year, \
    download dataset for particular album \
    and make cloud of words for particular year \
    \n
    <b>CONTENT</b>: \
    \n
    There are 4 columns: \
    \n
    * release_year - year when song was released first time, \
    \n
    * album - name of the album where track occurs,  \
    \n
    * title - title of the song,  \
    \n
    * lyrics - lyrics of the track  \
    \n
    <b>ACKNOWLEDGEMENTS</b>: \
    \n
    Contains only songs that Bob Dylan himself has \
    written and published. There's many songs that Bob Dylan " \
    only covered so I didn't include them.  \
    For instance album <i>World Gone Wrong</i> contains \
    only old folks songs. \
    \n
    <b>INSPIRATION</b>: \
    \n
    I'm great Bob Dylan fan. I listen to his songs almost every \
    day from many years.  \
    I also play them and sing them so now \
    I decided to make dataset and play with them on this app as well. \
    with them on this app as well. """


    DATASET = "<h2 style='text-align: center;" \
              "color: blue;'>DATASET</h2>"

    PLOT_SUBHEADER = "<h2 style='text-align: center;" \
                     "color: blue;'>SONGS DISTRIBUTION BY YEARS</h2>"

    ALBUM_SELECTION = "Select album: "

    DOWNLOAD_DATAFRAME = "DOWNLOAD YOUR DATAFRAME"

    WORDCLOUD_SUBHEADER = "<h2 style='text-align: center;" \
                          "color: blue;'>WORDCLOUD</h2>"
                          
    WORDCOUD_DESCRIPTION = "If you want to generate wordcloud " \
                           "for particular year, select " \
                           "this year on the slider, " \
                           "wordcloud will be generated automatically"
    
    DOWLOAD_WORDCLOUD = "DOWNLOAD YOUR WORDCLOUD"
    
    WORDCLOUD_FILENAME = "wordcloud.png"
