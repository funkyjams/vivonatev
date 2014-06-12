Vivonatev
=========


## Description:
Vivonatev is a NGS mapping pipeline using Bowtie2 and Samtools. This pipeline can match NGS reads to large amounts of 
reference genomes. Features include:

* Can map both single-end and paired-end NGS reads
* Ability to recursively filter out each reference genome
* Extract positively mapped reads 
* Generate coverage vector of each genome
* Threshold for filtering and generating coverage vector (saves a lot of time)


## Revive
Revive is the name of the pipeline executable:

usage: revive {-i input / -1 mate_1 -2 mate_2} {action[s]} [options]



### Arguments:
##### Mandatory:
###### -i inputfile.fastq
Non-paired, fastq input file (can be replaced by -m1 & -m2)
###### -m1 / -m2 input_mates_1/2.fastq
Paired fastq input files

#### Actions
##### -L 
Keeps the log for each reference instead of deleting them (log_refname)
##### -F 
Filters out all mapped read for each reference
##### -C
Genereage coverage vector for each reference (refname_cov.vec)
##### -E 
Extract the reads mapped to reference in separate file (map_refname.fq)

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
Name_index is the file containing the information on which references to map. Format:

| # Ref_name  | Ref_fasta    | Ref_length |
| ----------- | ------------ | ---------- |
| hiv         | AF_033819.fa | 9315       |
| ebv         | NC_007605.fa | 174280     |

The reference fasta can be defined with an absolute path if necessary, otherwise Revive will look in the current directory. The 
index file can include comments (starting with #).


### Requirements:
* Bowtie2
* Samtools
* Bam2fastq (from Hudson Alpha)
* python2.7


### Installation
To install Vivonatev, you can simply move the executables to your path (~/bin/, /usr/local/bin/ or other). 


## Other Scripts
These other scripts may be helpful when working with Vivonatev.

### isAboveThreshold
Simple script the check if a mapping is above a certain treshold. Uses the output of bowtie2.
Can be usefull when selecting which references to filter/cover.

### vect2.py
Short program to transform the output of mpileup into a vector. Used with '-C' option.

### btindexer
Small script designed to generate the name_index

usage: 
    btindexer name_index ref_name ref_fasta


## Future Improvements
* Implement option for other alignment tool (maybe bwa?)
* Quiet mode (keep output to a minimal)
