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

    <h1>MaaSive.net BootStrap Inliner</h1>

    <p>Use the form or POST to this URL to get your Markdown document converted to HTML
    and Bootstrap CSS inserted inline.  This is great for emails!</p>

    <form name="md-input" action="/" method="post">
        <div><textarea name="text" rows="12" cols="80" autofocus>Paste your markdown here!</textarea></div>
        <div><input type="submit" value="Submit"></div>
    </form>

    <div>
    <em>You can also POST directly to http://inliner.maasive.net/ with your markdown text
    in the "text" field of the form to use the Bootstrap Inliner as a web-service.
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
