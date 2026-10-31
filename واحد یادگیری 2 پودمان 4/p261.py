from pathlib import Path
File_Path = Path("brands.txt")
brands = ""
flag = True
while flag:
    xstring = input("enter your phone brand: ")
    xstring += "\n"
    brands += xstring
    flagCheck = input("wanna continue? True/False ")
    if flagCheck == "False":
        flag = False
File_Path.write_text(brands)
