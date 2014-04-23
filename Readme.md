Vivonatev
=========


### Description:
This is the work in progress for an alignment pipeline for bowtie2. This pipeline will be able to match a fastq file to a number of reference genomes. Features include:
* Ability to recursively filter each reference genome
* Generate coverage vector of each genome
* Threshold for filtering and generating coverage vector (saves a lot of time)


### Arguments:

##### Mandatory:
###### -i inputfile.fastq
input file. fastq format. Only one input file allowed for now  (See improvements)
###### -d reference_directory/
Directory containing indexes of reference genomes. You must build indexes using bowtie2-build beforehand. Directory may include a name_index file listing the references genome name (provided when running bowtie2-build)

##### Optional:
###### -F
Filtering option. When going through each reference, filter out the mapped reads.
###### -C
Coverage option. For each reference, generate coverage vector.
###### -t x
Threshold. Limits -C and -F options to reads that mapped to at least x% of input file. (def 0)
###### -n index_file
File containing the refence names in '-d' to map to. default is 'directory/name_index'
###### -bc N
Allows the user to specify the number of cores to run bowtie2 mapping with. (def 1)
###### -S
Sampling mode, disable -C, -F and exceptions for threshold below -t. Saves time by canceling samtools execution
###### -D
Debug mode. TBD


### Requirements:
* Bowtie2
* Samtools
* picard-tools
* python2.7


### Installation
You can move the executable to your path. Before running, you MUST change line 85 to match where picard-tools is installed on your computer.  


### Future Improvements
* TBA
