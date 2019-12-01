"""
Wylistuj wszystkie pliki we wskazanym katalogu
wynik zapisz w c:\\temp\\skan_<cur_date>.txt

"""

import os
import datetime

def skan_folder(path):
    data = os.listdir(path)
    cur_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"skan_{cur_date}.txt"
    if "temp" not in os.listdir("c:\\"):
        os.mkdir("c:\\temp")
    with open(f"C:\\temp\\{filename}", "w") as f:
        f.write("\n".join(data))
    print("Skończone, wyniki w: ", filename)


dane = os.popen("dir").read()
print(dane)

# os.system("dir")

# skan_folder("C:\\Program Files")

# print(os.getcwd())
# old_cwd = os.getcwd()
# if "temp" not in os.listdir("c:\\"):
#     os.mkdir("c:\\temp")
# os.chdir("c:\\temp")


# # print(data)
# with open("nowy_plik.txt", 'w') as f:
#     f.write("To jest nowy plik")
#
# os.chdir(old_cwd)