#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2021 Colin Curtain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Author: Colin Curtain (ccbogel)
https://github.com/ccbogel/QualCoder
https://qualcoder.wordpress.com/
"""

import base64
import os

languages = ['de', 'el', 'es', 'fr', 'it', 'jp', 'pt']

class CreateHelperFile():
    """ Create an output python file with converted languaged into base64
    The output file is used as a helper file in QualCoder
    This helps to get around translation data failing to load depending on where qualcoder
    is called from. Important for use with pyinstaller as accessing data files does not work well.
    """

    def __init__(self):
        #super(CreateHellpderFile, self).__init__()

        header = '#!/usr/bin/python\n# -*- coding: utf-8 -*-\n\
        \n"""\nCopyright (c) 2021 Colin Curtain\n\n\
        Permission is hereby granted, free of charge, to any person obtaining a copy\n\
        of this software and associated documentation files (the "Software"), to deal\n\
        in the Software without restriction, including without limitation the rights\n\
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n\
        copies of the Software, and to permit persons to whom the Software is\n\
        furnished to do so, subject to the following conditions:\n\n\
        The above copyright notice and this permission notice shall be included in\n\
        all copies or substantial portions of the Software.\n\n\
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n\
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n\
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n\
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n\
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n\
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n\
        THE SOFTWARE.\n\n\
        Author: Colin Curtain (ccbogel)\n\
        https://github.com/ccbogel/QualCoder\n\
        https://qualcoder.wordpress.com/\n\n\
        Generated base64 helper file\n"""\n\n'

        text = header
        files = []
        for l in languages:
            files.append(l + "/" + "app_" + l + ".qm")
            files.append(l + "/LC_MESSAGES/" + l + ".mo")
            #tmp_files = os.listdir()

        for f in files:
            text += "\n"
            name = f[:2] + "_" + f[-2:]
            text += name + " = b'"
            s = self.encode_base64(f)
            text += s.decode('utf-8')
            text += "'\n"

        # write the generated file
        filename = "base64_lang_helper.py"
        f = open(filename, 'w', encoding='utf-8-sig')
        f.write(text)
        f.close()
        print("FINISHED CREATING BASE64 HELPER FILE")

    def encode_base64(self, file_path):
        """ """

        with open(file_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read())
        return base64_string


if __name__ == '__main__':
    CreateHelperFile()