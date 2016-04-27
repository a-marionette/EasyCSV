# EasyCSV


## What it does


> A python script to convert one CSV structure to another. At the moment, you must hardcode your export structure (headers) to make this work. Useful for importing CSV files directly into a DB.

## Setup

> Pick which script you would like to run. EasyCSV.py will export a single CSV stucture, while EasyCSV-x will allow for you to export 'x' number of CSV structures from your input data. 

> Open the Python file you chose and hardcode as many CSV headers as you'd like. Every header you choose must be inserted as such: DbAtts['YOUR_HEADER']. Rinse and repeat this process for any additional tables (if you chose a version of this script that allows for multiple export structures).

## Usage

* **set** -  A ':' delimited command to bind the index of an attribute in the input CSV to its corresponding new CSV attribute.

    > set:gender:12

* **show** - Shows what attributes are currently binded to their new counterpart.

* **columns**- Shows the indexes of each old CSV attribute

* **e** - Exports the data to a text file (once they have been binded)

* **help** - Shows this menu


## Changelog
* 21-April-2016 -- First version


