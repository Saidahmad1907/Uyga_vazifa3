import os

class FindFile:
    @staticmethod
    def check_file():
        home_dir = os.path.expanduser('~')
        downloads_dir = os.path.join(home_dir, 'Downloads')
        file_path = os.path.join(downloads_dir, 'product_list.docx')
        return os.path.isfile(file_path)

if FindFile.check_file():
    print("Fayl mavjud.")
else:
    print("Fayl mavjud emas.")

