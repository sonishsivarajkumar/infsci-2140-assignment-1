from Classes.Path import DataWebDir
from PreProcessData.SafeFileStreamService import SafeFileStreamService
from PreProcessData.XmlParseService import XmlParseService

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.


class TrecwebCollection:

    def __init__(self):
        # 1. Open the file in Path.DataWebDir.
        # 2. Make preparation for function nextDocument().
        # NT: you cannot load the whole corpus into memory!!

        # since we're not allowed to parse the XML the right way, I wrote
        # a small helper to handle retrieval of data from XML
        self.xmlService = XmlParseService()

        # open the corpus file
        self.file = SafeFileStreamService(DataWebDir, '</DOC>')

    def nextDocument(self):
        # 1. When called, this API processes one document from corpus, and returns its doc number and content.
        # 2. When no document left, return null, and close the file.
        # 3. the HTML tags should be removed in document content.
        xml = self.file.next()

        if xml is None:
            return None

        docNo = self.xmlService.extract_element_content('DOCNO', xml)
        content = self.xmlService.extract_html_text(xml)

        return [docNo, content]
