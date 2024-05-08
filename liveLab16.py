"""
EXERCISE 1

Consider the following list of best-selling music artists, with a focus
on artist who have sold more than 250 million records:
    
    https://en.wikipedia.org/wiki/List_of_best-selling_music_artists
    
Are we allowed to scrape the data from this page with a program? What should 
we check?
"""

"""
EXERCISE 2

Having verified this, download the page in Python; put it into a soup object
"""

"""
EXERCISE 3

Short: Create a csv file with the table of artists who have sold 250 million 
records or more

Long:
A Find all the tables in this page. How many are there?
B. Create a object with just the first table; does it have the set of artists
who have sold more than 250M records?
C. Extract a object with all the rows in this table.
D. Convert the rows into elements of a list
E. Create a dataframe and export  it as a CSV file
"""