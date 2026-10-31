from pathlib import Path
File_Path = Path("brands.txt")
brands = File_Path.read_text()
brands = File_Path.read_text().rstrip()
brands = brands.splitlines()
for i in brands:
    print(i , " : " , len(i))