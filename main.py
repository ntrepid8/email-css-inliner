__author__ = 'ntrepid8'
from email_css_inliner.email_css_inliner import EmailCssInlinerRequestHandler
import tornado.options
import tornado.ioloop
import tornado.web
import logging
logger = logging.getLogger(__name__)


def main():
    tornado.options.define(
        "port", default=8888, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    logger.info('md to html with inline css starting...')
    application = tornado.web.Application(
        [(r"/", EmailCssInlinerRequestHandler), ],
        debug=False,
        autoreload=True
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
