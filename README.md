# email-css-inliner

A simple tornado web service that takes input in the form of a markdown text file and converts it to HTML with Bootstrap 3 CSS styles inserted inline on the html tags.

## example with the excellent Requests library

    html_content = requests.post('http://localhost:8888/',data=md.encode()).text

## Installation

On Ubuntu 12.04 LTS run the following commands to make sure you have all the build requirements:

    $ sudo apt-get install libxml2-dev libxslt1-dev python-dev build-essential
    $ sudo pip install tornado premailer markdown
