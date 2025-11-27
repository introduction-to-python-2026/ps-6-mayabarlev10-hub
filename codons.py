def create_codon_dict(file_path):
   with open(file_path, 'r') as fl:
        rows = fl.readlines()

   dict = {}
   for row in rows:
       row = row.strip().split('\t')
       codon = row[0]
       amino = row[2]
       dict[codon] = amino
   return (dict)


