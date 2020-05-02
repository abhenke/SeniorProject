#! /usr/bin/env python3.4
import sys
import getopt
import re
from Bio import SeqIO
from Bio.Blast import NCBIXML

def main():
    optInput = False #Is there input storage
    optOutput = False #Is there an output file storage
    optSequence = False #Is seq kept storage

    #Command Line Prompts
    print("Reading command line prompts...")
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'i:so:')

    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    if (len(opts) == 0):
        print("Error: need input [-i]")
        sys.exit(2)

    print("Arguments used: ", opts)
    for (opt, arg) in opts:
        #option for input file
        if (opt == '-i'):
            optInput = True
            inputFile =  arg
        #option for output file
        if (opt == '-o'):
            optOutput = True
            output = arg
    #open and clean the file and return
    if (optInput == True):
        print("Opening input file...")
        openFile = open(inputFile)
        blast_records = NCBIXML.parse(openFile)
        print(blast_records)
        if (optOutput == True):
            f = open(output, "a+") 
            for blast_record in blast_records:
                descriptions = blast_record.descriptions
                if len(descriptions) !=0:
                    f.write(blast_record.query + "\n")
        else:
            for blast_record in blast_records:
                descriptions = blast_record.descriptions
                if len(descriptions) !=0:
                    print(blast_record.query + "\n")

if __name__ == "__main__":
    main()
