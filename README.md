# pigeon

Download and convert spreadsheet (XLSX) financial data from the Network Rail transparency website into to tab-separated files (TSV). 

A shell and python-script implementation to scrape and download data from URL the Network Rail transparency website URL [here](https://www.networkrail.co.uk/who-we-are/transparency-and-ethics/transparency/our-information-and-data/)

## What it does

In the root diretory execture the ```run.sh``` script as follows:

    $ ./run.sh

The script then:

* Convert the HTML ```index.html``` on the transpanency URL to JSONL and filters the output find only data related to expenditude over £25k
* Downloads and renames the associated XLSX into files with names in the format ```YYYYMM``` to the ```data``` subdirectory
* Extracts the financial data into a set of TSV files in the ```output``` directory


### Pre-requisites

These shell and Python scripts have been tested under a current Linux Mint installation and assume the following are installed

* Python 3.x: versions 3.x of the `python` programming language [here](https://www.python.org/)
* jq: the lightweight and flexible command-line JSON processor [here](https://stedolan.github.io/jq/)
* curl: the command line tool and library for transferring data with URLs [here](https://curl.haxx.se/)

### `python` dependencies

For ease of use manage package `python` packages dependencies with a local virtual environment `venv`:

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

### If missing, install the `python virtualenv` package

    $ sudo apt install virtualenv

# Licenses

Information used in this example is provided is by Network Rail [here](https://www.networkrail.co.uk/transparency/datasets/)

Otherwise these scripts are released under a MIT license 
