from os import path
import time
from xml import sax
from xml.sax.handler import ContentHandler
import xml.etree.ElementTree as ET


class SaxContentHandler(ContentHandler):
    def __init__(self):
        self.count = 0

    def startElement(self, tag, attributes):
        return

    def endElement(self, tag):
        if tag == "DOC":
            self.count += 1

    def get_count(self):
        return self.count


def count_by_sax(path):
    handler = SaxContentHandler()
    parser = sax.make_parser(['xml.sax.IncrementalParser'])
    parser.setContentHandler(handler)

    with open(rf'{path}', 'rb', buffering=32) as f:
        for chunk in f:
            parser.feed(chunk)
            count = handler.get_count()

    return count


def count_by_pullparse(path):
    parser = ET.XMLPullParser(['end'])

    with open(rf'{path}', 'rb', buffering=32) as f:
        while True:
            line = f.read()

            if line is None:
                break

            parser.feed(line)

    print('pull parse: reading events')
    return sum(1 for _ in parser.read_events())


def count_by_iterparse(path):
    count = 0
    context = ET.iterparse(path, events=('end',))
    prior_element = None

    for action, elem in context:
        if elem.tag == 'DOC':
            if prior_element is not None:
                prior_element.clear()
            prior_element = elem
            count += 1

    return count


def count_by_line(path):
    with open(path, 'r', encoding="utf-8") as file:
        return sum([1 if read_line.strip() == "</DOC>" else 0 for read_line in file.readlines()])


# docset_path = 'E:/School/Grad/infsci-2140/assignment-1/data/output/docset.trectext'
# docset_path = 'E:/School/Grad/infsci-2140/assignment-1/data/output/docset.trectext'
docset_path = 'E:/School/Grad/infsci-2140/assignment-1/data/output/docset.trecweb'

start_time = time.time()
total = 0

# total = count_by_pullparse(docset_path)
# total = count_by_iterparse(docset_path)
# total = count_by_sax(docset_path)
total = count_by_line(docset_path)

print('time', time.time() - start_time)
print('total documents', total)
