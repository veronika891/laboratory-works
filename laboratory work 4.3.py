from Bio import SeqIO
for record in SeqIO.parse("species1&2.gb", "genbank"):
    species = record.annotations.get("source", "Неизвестный вид")
    cds_list = [f for f in record.features if f.type == "CDS"]
    if not cds_list:
        print(f"{record.id}: нет CDS\n")
        continue
    for i, cds in enumerate(cds_list, 1):
        seq = cds.location.extract(record.seq)
        if seq:
            seq = seq[:len(seq) - len(seq) % 3]
            try:
                print(f"{record.id} ({species}) CDS {i}:")
                print(f"  Translation:\n  {seq.translate()}\n")
            except Exception as e:
                print(f"{record.id} (CDS {i}): ошибка трансляции — {e}\n")
        else:
            print(f"{record.id} (CDS {i}): пустая последовательность\n")