"""
PdfKit

Usage:
    pk (-k | --mark) <FILE> <CATALOGUE_NUMBER> <FIRST_PAGE_NUMBER>
                          [--first=<FIRST_NUMBER>]
    pk (-h | --help)
    pk --version

Arguments:
    FILE                the PDF files
    CATALOGUE_NUMBER    the page number of the catalogue
    FIRST_PAGE_NUMBER   the page number of the first page for the content
    LAST_PAGE_NUMBER    the page number of the last page for the content

Options:
    -k --mark       Generates bookmarks for every page through specifying
                    the first and the last page for a PDF.
                    It will create a new pdf file named "marked.pdf"
                    rather than overwrite the inputted file.

    --first=<FIRST_NUMBER>
                    specify the last page for the content [default: lastPage]

    -h --help       Show this screen.

    --version       Show version.

Examples:
    pk -k D:/a.pdf 10 15
    pk -k D:/a.pdf 10 15 --first 300

Tips:
    The file name and path may not contain blanks

"""
import os
import sys


cwd = os.getcwd()
sys.path.insert(0, os.path.split(cwd)[0])
#increase the capacity of the stack,
#otherwise will cause: maximum recursion depth exceeded while calling a Python object
sys.setrecursionlimit(10000)

from pdf.kit import add_bookmarks
from docopt import docopt

arguments = docopt(__doc__, version='v1.0.0')

#options mapping
opt_func = {
    '--mark': add_bookmarks
}

if arguments['--mark']:
    opt_func['--mark'](
        arguments['<FILE>'][0:],
        arguments['<CATALOGUE_NUMBER>'],
        arguments['<FIRST_PAGE_NUMBER>'],
        arguments['--first']
    )