__author__ = 'ntrepid8'
from tornado.web import RequestHandler
from premailer import Premailer
import markdown
import logging
import os
bootstrap_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..', 'css', 'bootstrap-simple.css'
    )
)


class EmailCssInlinerRequestHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.write('post document to this URL to have CSS inlined')

    def post(self, *args, **kwargs):
        md_one = ''.join([
            '<div class="content-wrapper">',
            md_to_html(self.request.body.decode('utf-8')),
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
