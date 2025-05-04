#Задание 1, вариант 8

from Bio import SeqIO
files = ["species1.gb", "species2.gb"]
records = [rec for file in files for rec in SeqIO.parse(file, "genbank")]
SeqIO.write(records, "species1&2.gb", "genbank")
print("Объединённый файл сохранён как species1&2.gb")