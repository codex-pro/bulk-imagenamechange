# SWAMI KARUPPASWAMI THUNNAI

import xlrd
import tqdm
from PIL import Image


def rename():
    workbook = xlrd.open_workbook("name.xlsx")
    sheet = workbook.sheet_by_index(0)
    for i in tqdm.tqdm(range(sheet.nrows)):
        if i == 0:
            continue
        original_file_name = sheet.cell_value(i, 0)
        new_file_name = sheet.cell_value(i, 1)
        try:
            image = Image.open("images/{}".format(original_file_name))
            image.save("output/{}".format(new_file_name))
        except Exception as e:
            with open("log.txt", "a") as log:
                log.write("Missing: {}\n".format(original_file_name))


if __name__ == "__main__":
    rename()
