# Buster-Block 🛒
----

<div align="center" width="30">

<img src="https://i.pinimg.com/originals/bc/22/8a/bc228a0c9fa6eddd97557149f5453247.jpg " width='300'/>

</div>

### Development 🧐
----

The person in charge of the IT department requires a team of Data Engineers to carry out the design, development and presentation of software that allows working with a set of data. In the same way, these can be presented on a board that facilitates tactical decision-making in the medium and long term.

The objectives to be achieved in this project are the following:
- Develop a python application that performs an ETL starting from
a plain text file *(.csv)* to a relational database *(PostgreSQL)*
- Develop an API with a graphical interface for the use of the python application that performs ETL
- Develop functionalities that allow transformations, ABM and queries on a relational database
- Develop tests on the developed python application
- Design and develop a dashboard in MicroStrategy that consumes data from a relational database

### Dataset 📚
----
Our initial dataset corresponds to 6 csv format files:
1. **cities.csv**: Information of the cities
2. **customer.csv**: Customer information
3. **prod_cat_info.csv**: Product information by category
4. **store_types.csv**: Information about the types of stores
5. **stores.csv**: Store information
6. **transactions.csv**: Transaction information

[Descargar](https://drive.google.com/drive/folders/1Du778xOcXmX5q-TZbXokoEkQBt4ONyF6?usp=share_link "Dataset")

### Folders structure 📂
----
- Analisis: 
    - EDA
    - Dataset
    - Insight
- Buster-Block:
    - api
        - logs
    - data_client
    - database
    - docs
        - source
    - utils
        - config
        - db
            - logs
        - etl
            - logs
        - logs
        - test
    - webapp
        - .streamlit
        - pages
            - uils_pages

### Previous requirements ⏮️
----
- Python > 3.7.0
[Descargar Python](https://www.python.org/downloads/ "Python")
- PostgreSQL > 10.0.0 
[Descargar Docker](https://www.docker.com/products/docker-desktop/ "Docker")


### Setup ⚙️
----
```
Important!

.env -> Edit the database credentials
```
### Windows
----
```
Go to the working directory
```
```
Open command console
```
```
docker-compose up -d
```
```
python -m venv env
```
```
env/scripts/activate
```
```
pip install -r requirements.txt
```
```
python Buster-Block/api/api.py
```
```
Open new terminal
```
```
env/scripts/activate
```
```
cd Buster-Block/webapp
```
```
streamlit run home.py
```
### Mac/Linux
----
```
Go to the working directory
```
```
Open command console
```
```
docker-compose up -d
```
```
python3 -m venv env
```
```
suorce env/bin/activate
```
```
pip install -r requirements.txt
```
```
python3 BusterBlock/api/api.py
```
```
Open new terminal
```
```
suorce env/bin/activate
```
```
cd Buster-Block/webapp
```
```
streamlit run home.py
```
