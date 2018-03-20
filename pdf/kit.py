import PyPDF2
import sys
import os


def add_bookmarks(file, catalogue_num, first_page_num, first_num):
    """
    Add bookmarks to the given PDF file
    It will create a copy of the PDF in the same directory

    :param file: the path of the PDF
    :param catalogue_num: the page number of the catalogue in PDF
    :param first_page_num: the page number of the first page of the content in PDF
    :param last_page_num: the page number of the last page of the content
    :return: None
    """
    try:
        print(file)
        with open(file, mode='r+b') as pdf:
            # If the last page is not specified, the page number of the original PDF is read as the last page of the default content.
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            last_page_num = pdf_reader.getNumPages()

            # Copy that and export the content to it
            merger = PyPDF2.PdfFileMerger()
            merger.append(pdf)
            merger.addBookmark('Contents', int(catalogue_num)-1)
            if first_num == '':
                bookmark_num = int(first_page_num)
            else:
                bookmark_num = int(first_num)
            for page_number in range(int(first_page_num)-1, int(last_page_num)):
                merger.addBookmark(str(bookmark_num), page_number)
                bookmark_num += 1
            output_pdf_path = clone(file)
            with open(output_pdf_path, mode='wb') as output_pdf:
                merger.write(output_pdf)
    except FileNotFoundError as e:
        print('File not found: {}'.format(e.filename))
        sys.exit(1)
    except ValueError as e:
        print('Please check your page number')
        sys.exit(1)


def clone(pdf):
    """
    Clone a new pdf.
    The name of the copy will be added the prefix : 'copy_'

    :param pdf: the path of the pdf to be copied
    :return: the path of the copy
    """
    file_name = 'copy_' + os.path.basename(pdf)
    file_path = os.path.split(os.path.realpath(pdf))[0] + '\\' + file_name
    # parts = ['copy', pdf]
    # product_name = '_'.join(parts)
    with open(pdf, mode='rb') as src:
        data = src.read()
        with open(file_path, mode='wb') as output:
            output.write(data)
    return file_path