from asgiref.sync import async_to_sync

from src.ui.gui.services.exceptions import FileNotSupported

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os


# Its going to take images and either convert them into text
# Make sure you have installed the tesseract service
class OCRService(object):

    def __init__(self, timeout=.5, debug=False):

        # supported image files according to the tesseract website
        self._supportedFiles = [
            "png",
            "jpeg",
            "jpg",
            "gif",
            "pdf",
            "bmp",
            "tiff"
        ]

        self.timeout = timeout
        self.debug = debug
        pass

    def is_file_supported(self, file_abs_path):
        basename = os.path.basename(file_abs_path)
        info = os.path.splitext(basename)
        extension = ((info[1])[1:]).lower()
        return self._supportedFiles.__contains__(extension)

    # converting the image file into string
    @async_to_sync
    async def convert_to_string(self, file_abs_path):
        if not self.is_file_supported(file_abs_path):
            raise FileNotSupported(f"The {self.__class__.__name__} can not handle this type of file : {file_abs_path}")
        try:
            text =  pytesseract.image_to_string(file_abs_path, timeout=self.timeout)
            if self.debug:
                print("[DEBUG]", text)
            return text
        except pytesseract.TesseractError:
            print("[ERROR]", "file is not supported")


# service = OCRService(debug=True)
# print(service.is_file_supported("/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/example.txt"))
# service.convert_to_string("/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/example/test.jpg")
