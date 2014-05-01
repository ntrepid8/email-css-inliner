# email-css-inliner

A simple tornado web service that takes input in the form of a markdown text file and converts it to HTML with Bootstrap 3 CSS styles inserted inline on the html tags.

## example with the excellent Requests library

    html_content = requests.post('http://localhost:8888/',data=md.encode()).text
