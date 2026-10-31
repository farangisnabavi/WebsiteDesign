from pathlib import Path
File_Path = Path("brands.txt")
brands = File_Path.read_text()
brands = File_Path.read_text().rstrip()
brands = brands.splitlines()
brand_text = ""
for brand in brands:
    brand_text += " "
    brand_text += brand.rstrip()
    print(brand_text)