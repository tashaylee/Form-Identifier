# Form Counter
Form counter is a webscraping tool that automates and counts the number of lead forms and different type of lead form styles on a 2U-owned webpage.

## Installation
You will need to install the below Requests and Beautiful Soup 4 python libraries using pip.

$ python -m pip install requests
$ pip3 install beautifulsoup4

## How to use Form Counter
To run Form Counter, a csv file of 2U-owned urls* is taken in as input, and will return a csv file of the total number of lead forms on each url along with the types of lead forms on each url. Since 2U-owned domains only have 2 types of lead forms: inline and homepage, this program only accounts for that.

*Note : Form Counter can only be run on 2U's suite of domain names, due to the specific naming convention of the lead forms on 2U-owned sites. For the purposes of this project for MET CS521, a csv file of urls from has already been extracted to test this program on.

## Requests Library
Requests is a python http library. In this program, the Requests library is used to call a webpage through the Requests API.

The method, requests.get().text , is used to retrieve data from the url passed into it, and .text encodes the characters in UTF-8 upon retrieving.

## Beautiful Soup 4 Library
Beautiful Soup 4 is a library for extracting html and xml files.

BeautifulSoup() creates an object that parses the html string passed into it. It accepts 2 arguments: the html string to parse, and the name of the parser. We will be using Python's built-in HTML parser.

.find_all() method returns a collection of all elements it can find that meets the requirements of the parameters passed in.
.find() method takes an html tag name and returns the first element found with the tag name.