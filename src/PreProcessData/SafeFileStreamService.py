import traceback


# Since both TrectextCollection and TrecwebCollection stream data out of a large file
# I wrote a small service that manages this so both can benefit
class SafeFileStreamService:
    def __init__(self, path, delimiter):

        # open the file and record the delimiter
        self.delimiter = delimiter
        self.file = open(path, 'r', encoding="utf-8")

    def next(self):
        try:
            content = []

            # read into the variable `content` until we encounter the delimiter
            # (in this case </DOC>), then break and return
            while True:
                # grab the new line
                read_line = self.file.readline()

                # if the read brings back an empty, this is the end of the file
                if read_line == '':
                    self.__cleanup()
                    return None

                # append the line to our running "content" var
                content.append(read_line)

                # if we hit the delimiter, return what we have
                if read_line.strip() == self.delimiter:
                    return "".join(content)
        except:
            # just a catch to make sure the file gets closed in the event
            # of a problem
            self.__cleanup(is_error=True)

        return None

    def __cleanup(self, is_error=False):
        # report an error if thrown
        if is_error:
            ex = traceback.format_exc()
            print('ERROR:', ex)

        # close file
        if self.file:
            self.file.close()
