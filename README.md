
# Overview

Pathologic file generator (PLFG) is implemented to assist and facilitate the curation progress of the _Methanococcus jannashii_ pathway genome database. This tool is not only useful for current genome curation, but could also be utilized by every curator and make their work easier. The main concept behind this tool is to convert a csv annotated file that contains all the curated information about a genome of interest into a pathologic file. A pathologic file (pf format example at [1]) contains genes and their features that are associated with the genome. This file constitutes one of the requirement files that must be inserted into the Pathologic component of Pathway Tools in order to generate a genome metabolic map. The workflow of tool is captured in Figure 1.
<br />
<br />
<br />
![pipeline_generator](https://user-images.githubusercontent.com/60938391/157713657-2cac2a7b-5af1-4aab-b799-5a51c82da93b.png)
```
Figure 1: Process of Pathologic File Generation.
```


# Technical Description

For the purposes of pathologic file generation, two classes were created, namely
EC_Validation and pathologic_generation. The two classes were utilized through
a main function in which all the required actions for the generation of the final
product, namely pathologic files, were implemented.

EC_validation class is associated with one function, namely EC_check. The
EC_check function :

- It takes as input an EC number that is associated with the current gene (csv
    cell).
- The EC number is checked to see if it could be split into four different parts
    by utilizing the dot character as a separator. Also, EC is checked if the first
    part is an integer and simultaneously greater than or equal to 1 and less than
    or equal to 7.
- Returns a boolean that captures whether the current EC number has the
    correct EC syntax.


The pathologic_generation class is associated with 2 functions, namely separator
and Tie2_filler. The separator function:

- It takes as inputs the dataframe which is created from a csv file and two
    integers, namely start and stop, which are the margins of separation between
    the two genome’s investigations.
- returns the separated dataframe which is associated with the information of
    one research.

The Tie2_filler function:

- It takes as inputs the current row (gene) of the two comparative genome’s
    investigations, the temporary pathologic file, the index of current row (gene)
    in whole dataframe.
- For every ID gene, it writes in the pathologic file its ID, ACCESSION-2,
    NAME, SYNONYM, REPLICON, STARTBASE, ENDBASE, DBLINK and
    PRODUCT TYPE.
- Also, for every gene, one or more EC numbers are written if they exist after
    their EC syntax check.
- If one EC number has wrong EC syntax, the program breaks and an error
    message is printed to the user that notifies them that in the specific row the
    EC number syntax must be changed.

In the main function, the system requires the user to input the path of the csv file
and the replicon name. Then the pathologic file generation procedure is classified
into two stages. The first stage is associated with the preparation of the csv file. The
csv file is imported and converted to a dataframe. Then the dataframe is separated
into two different dataframes, one per comparative genome’s investigation. In the
second stage, the pathologic file is gradually written (per gene) by utilizing the
function Tier2_filler, which is associated with the pathologic_generation class. The
main function’s pipeline which is corresponded with the mechanism of pathologic
generation tool is captured in Figure 2.
<br />
<br />
<br />
![pathologic_function](https://user-images.githubusercontent.com/60938391/157714062-869ad4b3-7152-40c3-858a-317a93cc1bb3.png)

```
Figure 2: The main function’s pipeline of pathologic generator tool.
```


# Pathologic File Generation Example

An example of the required format of the csv file that may be given in the pathologic
file generator file is captured in the Figure 3. This file corresponds to the sub-file
in which all the annotations for the curation progress of the genome of _Methanocaldococcus jannaschii_ were written. 
<br />
<br />
<br />
![Csv](https://user-images.githubusercontent.com/60938391/157714094-30bb5651-45b0-43ce-a5a1-59f533566022.png)

```
Figure 3: A sample of the csv file that includes all the annotations that were implemented during the curation of PGDB of Methanocaldococcus jannaschii.
```

The columns that are utilized by the pathologic
file generator tool are the ID (both from MJ_2005 and MJ_BioCyc), EC, PMID,
description, NAME, start, end, and product type. The output (pathologic file) of
the pathologic generator tool that takes as input the above file is captured in Figure 4.
<br />
<br />
<br />
![Tier2pf](https://user-images.githubusercontent.com/60938391/157714106-d90cc788-bf67-4951-a6b2-a96652ba8655.png)

```
Figure 4: A sample of the pathologic file of the curated   PGDB that was generated from the curation csv file by utilizing
the pathologic file generator tool.
```
# References
<br />
[1] https://bioinformatics.ai.sri.com/ptools/tpal.pf

