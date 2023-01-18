```mysql
create database DiseaseDB;
use DiseaseDB;
CREATE TABLE Disease (
  DiseaseID varchar(10) NOT NULL PRIMARY KEY,
  DiseaseName varchar(255),
  OmimID varchar(10)
);

CREATE TABLE Gene (
  GeneID varchar(10) NOT NULL PRIMARY KEY,
  GeneName varchar(50),
  Location varchar(50),
  Details varchar(100)
);

CREATE TABLE Effect (
  DiseaseID varchar(15) NOT NULL,
  GeneID varchar(10) NOT NULL,
  Phenotype varchar(255),
  PRIMARY KEY (DiseaseID,GeneID),
  FOREIGN KEY (DiseaseID) REFERENCES Disease(DiseaseID),
  FOREIGN KEY (GeneID) REFERENCES Gene(GeneID)
);

create table Metabolism(
    MetabolismID varchar(50) not null primary key,
    MetabolismName varchar(50),
    ChemicalFormula varchar(50),
    State varchar(50),
    Reference varchar(250),
    Details char(100) not null
);

create table Process(
    MetabolismID varchar(15) not null primary key,
    OmimID varchar(15) not null,
    foreign key (MetabolismID) references Metabolism(MetabolismID)
);

create table Map(
	DiseaseName varchar(50) not null primary key,
    mapID varchar(50)
);
```

