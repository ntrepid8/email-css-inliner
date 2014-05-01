__author__ = 'ntrepid8'
from tornado.web import RequestHandler
from premailer import Premailer
import markdown
import os
bootstrap_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..', 'css', 'bootstrap-simple.css'
    )
)


class EmailCssInlinerRequestHandler(RequestHandler):
    simple_form = """
    <!DOCTYPE html>
    <html>
    <head>
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-7507054-16', 'maasive.net');
      ga('send', 'pageview');

    </script>
    </head>
    <body>

    <h1><a href="https://maasive.net">MaaSive.net</a> <a href="http://getbootstrap.com/">BootStrap</a> Inliner</h1>

    <p>Use the form or POST to this URL to get your Markdown document converted to HTML
    and Bootstrap CSS inserted inline.  This is great for emails!</p>

    <form name="md-input" action="/" method="post">
        <div><textarea name="text" rows="12" cols="80" autofocus>Paste your markdown here!</textarea></div>
        <div><input type="submit" value="Submit"></div>
    </form>

    <div>
    This webservice makes use of the following Python Modules:
    </div>
    <div>
    <ul>
        <li>
            <strong>Tornado:</strong> <a href="https://pypi.python.org/pypi/tornado/3.2">https://pypi.python.org/pypi/tornado/3.2</a>
        </li>
        <li>
            <strong>Premailer:</strong> <a href="https://pypi.python.org/pypi/premailer/2.1.0">https://pypi.python.org/pypi/premailer/2.1.0</a>
        </li>
        <li>
            <strong>Markdown:</strong> <a href="https://pypi.python.org/pypi/Markdown">https://pypi.python.org/pypi/Markdown</a>
        </li>
    </ul>
    </div>

    <div><p>
    <em>You can also POST directly to http://inliner.maasive.net/ with your markdown text
    in the "text" field of the form to use the Bootstrap Inliner as a web-service.  Please
    note that you are rate limited to 1 request per second and will be served a 503 if
    that limit is exceeded.
    </p></div>

    <div>
    <p><a href="https://github.com/ntrepid8/email-css-inliner">Fork me on GitHub!</a></p>
    </div>

    <div>
    <p>The MIT License (MIT)</p>

    <p>Copyright (c) 2014 MaaSive.net LLC</p>

    <p>Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:</p>

    <p>The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.</p>

    </p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.</p>
    </div>

    </body>
    </html>
    """

    def get(self, *args, **kwargs):
        self.write(self.simple_form)

    def post(self, *args, **kwargs):
        md_raw = self.get_argument('text')
        md_one = ''.join([
            '<div class="content-wrapper">',
            md_to_html(md_raw),
            '</div>'
        ])
        html_text = inline_css(md_one)
        self.write(html_text)


def md_to_html(md_input):
    return markdown.markdown(md_input)


def inline_css(html_input):
    return Premailer(
        html_input,
        external_styles=[
            bootstrap_path
        ]).transform()
