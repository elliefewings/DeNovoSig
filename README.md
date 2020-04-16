# DeNovoSig

## Wrapper to run Python SigProfilerExtractor module
Takes input tab separated file, identifies novel mutation signatures and outputs results in local directory
## Installation
### Requires:
Python3.6  
SigProfilerExtractor module: <https://github.com/AlexandrovLab/SigProfilerExtractor>

### Install SigProfilerExtractor
Install module  
`$ pip install SigProfilerExtractor`
   
Install desired reference genome (GRCh37 is programme default, create issue or contact author for additional reference functionality).   
```
$ python3.6  
>> from SigProfilerMatrixGenerator import install as genInstall  
>> genInstall.install('GRCh37')
```
SigProfilerExtractor may require additional modules, view module page linked above for details.
## Usage
`$ ./denovoSig.py -i <inputfile> -o <outputdir>`   
See [example_input.txt](../master/example_input.txt) for an example of input.   
***NOTE*** that a title is required for rownames or error occurs.   
Output directory should not already exist.   
## Example
```
$ ./denovoSig.py -i /path/to/example_input.txt -o /path/to/output/dir
```
