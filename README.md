# dataplot
## Purpose 
Plot data from hdf5 file
- Using python-jupyter , plotly and highchart
- Using kivy desktop app

## How to use
```
git clone https://github.com/manthanrtilva/dataplot.git
cd dataplot
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
### Run Jupyter
```
jupyter-notebook
```
### Run Kivy
```
python kivy_graph.py
```
### Generate sample dataset
File name `sample.hdf5` is already there which is sample dataset. But user can generate their own dataset more sample points and/or more data points.
```
>python createDataSet.py -h
usage: createDataSet.py [-h] [-d DAYS] [-i INTERVAL] [-n NUMBERS] [-m MINUS]
                        filename

positional arguments:
  filename              hdf5 file name

optional arguments:
  -h, --help            show this help message and exit
  -d DAYS, --days DAYS  data for numbers of days(>0)
  -i INTERVAL, --interval INTERVAL
                        number of seconds between two records(>0)
  -n NUMBERS, --numbers NUMBERS
                        numbers of data points(>0)
  -m MINUS, --minus MINUS
                        data can be minus
```
With `-d` you can define for how many days you want to generate sample data.

With `-i` you can define how much interval you want to keep between two data sample.

With `-n` you can define how many data points you want to generate

With `-m` You can define whether you want to generate only positive data OR positive/nagative both.
###
__NOTE:__ 
- Data Samaples : Numbers of points in one line
- Data Points : Numbers of line(data sources)
