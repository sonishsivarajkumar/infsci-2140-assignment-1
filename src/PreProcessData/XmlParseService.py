import re


class XmlParseService:
    def __init__(self):
        # this dict holds compiled regexes to speed up matching
        self.regex_dict = {}

        # special case to catch non-tagged text content in the web collection
        self.regex_web = re.compile(r'</DOCHDR>([\s\S]+)</DOC>', flags=re.M)
        # replace regex to scrub HTML tags
        self.regex_html_tag = re.compile(r'</?.*?>', flags=re.M | re.DOTALL)

    def extract_element_content(self, tag, content):
        # compile a regex for this tag on demand
        if tag not in self.regex_dict:
            self.regex_dict[tag] = re.compile(rf'<{tag}>([\s\S]*?)<\/{tag}>', flags=re.M)

        # match the element pattern and return its inner text
        regex = self.regex_dict[tag]
        match = regex.search(content).group(1).strip()

        return match

    def extract_html_text(self, content):
        # find the content of the webpage (requires regex because it's not element-enclosed)
        raw_match = self.regex_web.search(content).group(1).strip()
        # clean up the HTML tags inside the content by regex replace
        match_untagged = self.regex_html_tag.sub('', raw_match).strip()

        return match_untagged
