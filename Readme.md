Vivonatev
=========


### Description:
You are witnessing the writing process for an alignment pipeline for bowtie2. This pipeline will be able to match a fastq file to a number of reference genomes. Features include:
* Ability to recursively filter each reference genome
* Generate coverage vector of each genome
* Threshold for filtering and generating coverage vector (saves a lot of time)


### Arguments:

##### Mandatory:
###### -i inputfile.fastq
input file. fastq format. Only one input file allowed for now  (See improvements)
###### -d reference_directory/
Directory containing indexes of reference genomes. You must build indexes using bowtie2-build beforehand. Directory must include a name_index file listing the references genome name (provided when running bowtie2-build)

##### Optional:
###### -F
Filtering option. When going through each reference, filter out the mapped reads.
###### -C
Coverage option. For each reference, generate coverage vector.
###### -t x
Threshold. Limits -C and -F options to reads that mapped to at least x% of input file.
###### -D
Debug mode. TBD


### Future Improvements

* allow user to determine the number of processors used when running bowtie2
* allow user to include his own name index
