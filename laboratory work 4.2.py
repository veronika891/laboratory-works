#Задание 2, вариант 8

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
records = list(SeqIO.parse("species1&2.gb", "genbank"))
gc_data = [(record.id, gc_fraction(record.seq), record.annotations.get("source", "Неизвестный вид")) for record in records]
gc_data.sort(key=lambda x: x[1])
for record_id, gc_content, species in gc_data:
    print(f"{record_id} ({species}): GC = {gc_content:.6f}")