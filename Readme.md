Vivonatev
=========


## Description:
This is the work in progress for an alignment pipeline for bowtie2. This pipeline will be able to match a fastq file to a number of reference genomes. Features include:
* Ability to recursively filter each reference genome
* Generate coverage vector of each genome
* Threshold for filtering and generating coverage vector (saves a lot of time)

## Revive
Revive is the new redesigned pipeline.

usage: revive {-i input / -1 mate_1 -2 mate_2} {action[s]} [options]



### Arguments:
##### Mandatory:
###### -i inputfile.fastq
Non-paired, fastq input file (can be replaced by -m1 & -m2)
###### -m1 / -m2 input_mates_1/2.fastq
Paired fastq input files

#### Actions
##### -L 
Keeps the log for each reference instead of deleting them
##### -F 
Filters all mapped read for each reference
##### -C
Genereage coverage vector for each reference

##### Optional:
###### -d <directory>
directory containing reference index (and possibly original fasta genome)
###### -n index_file
File containing the refence names in '-d' to map to. default is 'directory/name_index' (see index format)
###### -t x
Threshold. Limits -C and -F options to reads that mapped to at least x% of input file. (def 0)
###### -c N
Allows the user to specify the number of cores when running samtools and  (def 2)

### Name_index Format
Name_index is the file containing the information on which references to map:


### Requirements:
* Bowtie2
* Samtools
* picard-tools
* python2.7


### Installation
You can move the executable to your path. 
Before running, you MUST change line 7 to match where picard-tools is installed on your computer.  


## Other Scripts
### isAboveThreshold
Simple script the check if a mapping is above a certain treshold. Uses the output of bowtie2.
Can be usefull when selecting which references to filter/cover.

### vect2.py
Short program to transform the output of mpileup into a vector. Used with '-C' option.

### btindexer
Small script designed to generate the name_index

usage: btindexer name_index ref_name ref_fasta

## Future Improvements
* Implement option for other alignment tool (maybe bwa?)
* Implement comments in name_index
