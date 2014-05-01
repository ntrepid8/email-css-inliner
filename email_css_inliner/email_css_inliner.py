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
<html style="font-family:sans-serif; font-size:62.5%"><body style='background-color:#fff; color:#333; font-family:"Helvetica Neue", Helvetica, Arial, sans-serif; font-size:14px; line-height:1.428571; margin:0' bgcolor="#fff"><div style="padding:1em">
<h1 style='color:inherit; font-family:"Helvetica Neue", Helvetica, Arial, sans-serif; font-size:36px; font-weight:500; line-height:1.1; margin:0.67em 0; margin-bottom:10px; margin-top:20px'>
<a href="https://maasive.net" style="background:transparent; color:#428bca; text-decoration:none">Maasive.net</a> <a href="http://getbootstrap.com/" style="background:transparent; color:#428bca; text-decoration:none">Bootstrap</a> Inliner</h1>
<p style="margin:0 0 10px">Use the form or POST to this URL to get your Markdown document converted to HTML and Bootstrap CSS inserted inline. This is great for emails!</p>
<form name="md-input" action="/" method="post">
    <div><textarea name="text" rows="12" cols="80" autofocus>Paste your markdown here!</textarea></div>
    <div><input type="submit" value="Submit"></div>
</form>
<p style="margin:0 0 10px">This webservice makes use of the following Python Modules:</p>
<ul style="margin-bottom:10px; margin-top:0">
<li>
<strong style="font-weight:bold">Tornado:</strong> <a href="https://pypi.python.org/pypi/tornado/3.2" style="background:transparent; color:#428bca; text-decoration:none">https://pypi.python.org/pypi/tornado/3.2</a>
</li>
<li>
<strong style="font-weight:bold">Premailer:</strong> <a href="https://pypi.python.org/pypi/premailer/2.1.0" style="background:transparent; color:#428bca; text-decoration:none">https://pypi.python.org/pypi/premailer/2.1.0</a>
</li>
<li>
<strong style="font-weight:bold">Markdown:</strong> <a href="https://pypi.python.org/pypi/Markdown" style="background:transparent; color:#428bca; text-decoration:none">https://pypi.python.org/pypi/Markdown</a>
</li>
</ul>
<h2 style='color:inherit; font-family:"Helvetica Neue", Helvetica, Arial, sans-serif; font-size:30px; font-weight:500; line-height:1.1; margin-bottom:10px; margin-top:20px'>An Example with Python <a href="http://docs.python-requests.org/en/latest/" style="background:transparent; color:#428bca; text-decoration:none">Requests</a>
</h2>
<pre style='background-color:#f5f5f5; border:1px solid #ccc; border-radius:4px; color:#333; display:block; font-family:Menlo, Monaco, Consolas, "Courier New", monospace; font-size:13px; line-height:1.428571; margin:0 0 10px; padding:9px; white-space:pre-wrap' bgcolor="#f5f5f5"><code style='background-color:transparent; border-radius:0; color:inherit; font-family:Menlo, Monaco, Consolas, "Courier New", monospace; font-size:inherit; padding:0; white-space:pre-wrap' bgcolor="transparent">import requests
html_content = requests.post('http://inliner.maasive.net/',data={'text':'**some markdown!**'}).text
</code></pre>
<p style="margin:0 0 10px"><em>You can also POST directly to http://inliner.maasive.net/ with your markdown text in the "text" field of the form to use the Bootstrap Inliner as a web-service. Please note that you are rate limited to 1 request per second and will be served a 503 if that limit is exceeded.</em></p>
<p style="margin:0 0 10px"><a href="https://github.com/ntrepid8/email-css-inliner" style="background:transparent; color:#428bca; text-decoration:none">Fork me on GitHub!</a></p>
<div style="background-color:#f5f5f5; border:1px solid #e3e3e3; border-radius:3px; box-shadow:inset 0 1px 1px rgba(0, 0, 0, 0.05); margin-bottom:20px; min-height:20px; padding:9px" bgcolor="#f5f5f5">
The MIT License (MIT)

Copyright (c) 2014 MaaSive.net LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</div>
</div></body></html>
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
