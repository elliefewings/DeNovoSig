#!/usr/bin/python3.6
#Load modules
import sys, getopt
from SigProfilerExtractor import sigpro as sig
#Set input
import sys, getopt

def main(argv):
   input = ''
   output = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('denovoSig.py -i <inputfile> -o <outputdir>')
      sys.exit(2)
   if len(sys.argv) <= 1:
      print('denovoSig.py -i <inputfile> -o <outputdir>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('denovoSig.py -i <inputfile> -o <outputdir>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputdir = arg
      else:
         print('Unknown option', opt)
         print('denovoSig.py -i <inputfile> -o <outputdir>')
         sys.exit(2)
   print('Generating De Novo signatures for input file: ', inputfile)
   print('Output directory is: ', outputdir)
   #Run De Novo sig extraction
   sig.sigProfilerExtractor("table", outputdir, inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
