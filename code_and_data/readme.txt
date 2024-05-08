README for Code & Data Submission
"Who Becomes an Inventor in America? The Importance of Exposure in Innovation"
Authors: Alex Bell, Raj Chetty, Xavier Jaravel, Neviana Petkova, & John van Reenen

**********
**********
* Data Folder
**********
**********

*****
* Online Data Tables
*****

The data folder contains datasets that report aggregate statistics (e.g., by CZ and parent income group) that can be used to replicate many of the results in the paper. However, it does not contain all of the data necessary to replicate the paper, as the microdata for used in this paper is not publicly available. See the codebook PDF for more information on the datasets and their contents.


**********
**********
* Code Folder
**********
**********

*****
* Code to Create Tables and Figures Shown in Paper
*****
metafile.do - Defines macros and calls the following scripts:
	- tabs_main.do - Create main text tables
	- figs_main.do - Create main text figures
	- tabs_appendix.do - Create appendix tables
	- figs_appendix.do - Create appendix figures
	
The underlying data to create the figures and tables is not provided, although, as noted in the code, many of our results may be replicated with data from the publicly available online table collapses.


*****
* Code That Created Public Online Tables
*****
The folder "Code for Online Tables" contains scripts that created each online data table, as well as one script for formatting.


*****
* Additional Code Run on Tax Data
*****
irs_analysis.do
This script contains the analysis code run on tax data to create the collapses and regressions used to build figures and tables shown in the paper and appendix.