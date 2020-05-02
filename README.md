# SeniorProject
Code used for my project, "Protein Similarities of Significantly Beneficial Probiotics"


[gene list and database for *Bifidobacterium bifidum*] 
(https:www.ncbi.nlm.nih.gov/genome/881?genome_assembly_id=264013)

[gene list and database for *Escherichia coli*]
(https:www.ncbi.nlm.nih.gov/genome/167?genome_assembly_id=649986)

[gene list and database for *Bifidobacterium longum subsp. infantis*] (https:www.ncbi.nlm.nih.gov/genome/183?genome_assembly_id=313084)

E.coli file inputted at [database for B.bifidum] (https:blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&PROG_DEFAULTS=on&PROG_DEF=blastp&BLAST_SPEC=MicrobialGenomes_1681&DB_GROUP=AllMG)
Ran with all default parameters.
Downloaded as an XML.
Produced file named: BBEC-906YD5Z7016-Alignment.xml

E.coli file inputted at [database for B.longum subsp. infantis](https:blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&PROG_DEFAULTS=on&PROG_DEF=blastp&BLAST_SPEC=MicrobialGenomes_1682&DB_GROUP=AllMG)
Ran with all default parameters.
Downloaded as an XML.
Produced file named: BLEC-97PU416Z016-Alignment.xml

B.longum subsp. Infantis file inputted at[database for B.bifidum] (https:blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&PROG_DEFAULTS=on&PROG_DEF=blastp&BLAST_SPEC=MicrobialGenomes_1681&DB_GROUP=AllMG)
Ran with all default parameters.
Downloaded as an XML.
Produced file named: BBBL-906Z512G014-Alignment.xml

Commands to run parser:
input XML files from BLAST
Obtains list of proteins including organism and WP number
‘python3 parser.py -i BBEC-906YD5Z7016-Alignment.xml -o bbec.file’
‘python3 parser.py -i BBBL-906Z512G014-Alignment.xml -o bbbl.file’
‘python3 parser.py -i BLEC-97PU416Z016-Alignment.xml -o blec.file’

Removes organism
‘cat sortedblec.file | perl -pse 's/\[...*\]g' >> regexblec.file’
‘cat sortedbbbl.file | perl -pse 's/\[...*\]g' >> regexbbbl.file’
‘cat sortedbbec.file | perl -pse 's/\[...*\]g' >> regexbbec.file’

Removes WP number
‘cat regexbbbl.file | perl -pse 's/WP_...*\.1g' >> pbbbl.file’
‘cat regexbbec.file | perl -pse 's/WP_...*\.1g' >> pbecl.file’
‘cat regexblec.file | perl -pse 's/WP_...*\.1g' >> pblec.file’

Alphabetically sorts files
‘sort -o psortedbbbl.file pbbbl.file’
‘sort -o psortedbbec.file pbbec.file’
‘sort -o psortedblec.file pblec.file’

psorted*.file files were then cleaned of hypothetical, multispecies,
and duplicate proteins using excel to get clean*.txt files

Similarities found to make next set of child nodes 
in my “Merkle Tree”
‘comm -12 cleanBlec.txt cleanBbec.txt > bbblecec.txt’
‘comm -12 cleanBlec.txt cleanBbbl.txt > bbecblbl.txt’
‘comm -12 cleanBbec.txt cleanBbbl.txt > blecbbbb.txt’

Similarities of previous child nodes (now parent nodes)
to find final child nodes
All of these commands lead to the same file, but were each ran
to ensure sameness.
‘comm -12 bbblecec.txt bbecblbl.txt > ec3bl3bb2.txt’
‘comm -12 blecbbbb.txt bbblecec.txt > bb3ec3bl2.txt’
‘comm -12 bbecblbl.txt blecbbbb.txt > bl3bb3ec2.txt’
