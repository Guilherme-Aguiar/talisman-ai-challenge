import magic

def is_pdf(file_path):
    mime = magic.from_file(file_path, mime=True)
    return mime == 'application/pdf'

