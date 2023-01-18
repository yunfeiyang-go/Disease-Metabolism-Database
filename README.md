# Disease-Metabolism-Database
A course project for Database Concept in SJTU

## Goal
+ Obtain information from HMDB and construct a database to store information on relevant metabolic markers, metabolomics and supporting literature for important diseases (Including Obesity，Diabetes，Phenylketonuria，Prostate cancer，Lung Cancer，Thyroid cancer，Colorectal cancer，Ovarian cancer)
+ Work out human metabolic pathway map KEGG using Cytoscape.js, showing metabolic markers for each disease and their variations, characteristics 
+ Web UI provides access to information on diseases, metabolites, reactions, pathways, etc. 
+ Get gene-relative information corresponding to the stored diseases from OMIM, such as gene ID, name, pathway, etc.


## Data Source
+ **The Human Metabolome Database**

  HMDB is the world's largest and most comprehensive organism-specific metabolomics database. It contains richly annotated, multiple-checked, and widely referenced information on all currently known human metabolites, including chemical structures, names or identifiers, detailed text descriptions, references, chemical classifications, biological roles, disease associations, genetic associations, chemical and enzymatic reactions, metabolic pathways, and more. HMDB supports a wide range of interactive web queries, allowing metabolomics researchers to identify and annotate human (and other mammalian) metabolomics data by text, structure, quality or spectral matching.
+ **Online Mendelian Inheritance in Man**

  OMIM is a comprehensive, authoritative, and timely research resource for carefully organized descriptions of human genes and phenotypes and the relationships between them. It is a continuation of MIM, but unlike the original database, OMIM synthesizes and summarizes new and important information based on expert review of the biomedical literature. OMIM features powerful search capabilities, a user-friendly display of genetic/phenotypic relationships, and links organized by topic to a variety of external resources.


## Usage
+ Install Python, Django and MySQL.
+ Initialize

  ```python manage.py migrate```

+ Import data into database.

  The data can be found in ./data in .csv format.

  A useful tool is **Navicat**, which is visual and handy.

+ Use the website

  ```python manage.py runserver 8000```

  Then enter the URL in the browser: http://127.0.0.1:8000/. With different suffix, you can acheive different functions.

  You can get more information in the Tutorial page: http://127.0.0.1:8000/Tutorial.
