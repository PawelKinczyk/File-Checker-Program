from pathlib import Path
from openpyxl import load_workbook
import openpyxl.utils.exceptions as ex


def list_to_string(list):
    str = ''
    for i in list:
        str += (i+' ')
    return str


def check_files(folder_path, file_path, status_var, file_extension):
    try:
        # Get path files
        p = Path(folder_path)
        folder = p.glob('*')

        # Collect names inside folder
        file_list = []
        for i in folder:
            if file_extension == False:
                file_list.append(Path(i).stem)
            else:
                file_list.append(Path(i).name)

        # Open excel file
        excel = load_workbook(filename=file_path)

        excel_sheet = excel.worksheets[0]  # Pick defaul worksheet

        # Get listed names of files

        excel_list = []
        for i in excel_sheet['A']:
            excel_list.append(i.value)

        # Search for listed files in folder

        n = 0
        for i in excel_list:
            n += 1
            sheet_cell = 'B{}'.format(n)
            if i in file_list:
                excel_sheet[sheet_cell] = "True"
            else:
                excel_sheet[sheet_cell] = "False"

        # Return not listed files inside folder

        m = n+1
        sheet_cell = 'B{}'.format(m)
        other_files = list(set(file_list) - set(excel_list))
        excel_sheet[sheet_cell] = list_to_string(other_files)

        # Overwrite excel

        excel.save(filename=file_path)
        excel.close()
        status_var.set("Done without errors")

    except ex.InvalidFileException as e:
        status_var.set("Error: Please pick excel file")
    except Exception as e:
        status_var.set("Error: " + str(e))
