# Covid in South Africa
[alt text](https://github.com/zofiakk/project_DAV/blob/master/images/Flag-map_of_South_Africa.svg.png)

All of the scripts contained in a "scripts" folder are written in python. They allow to analyze and visualize the data pertaining the covid pandemic in South Africa and its neighboring countries.

Datasets used in this project contain summary statistics as well as inferential statistics (for example estimated masks usage).

## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Authors](#author)

## General Information

All of the scripts can be grouped into 3 categories. The first one is stored in the 'stationary' subfolder and allows to create non-interactive plots which can be saved to jpg format and are used in the pdf poster.
The second group consist of all of the other scripts except for 'utils.py' and 'main.py'. They are responsible for creating interactive plots which then can be saved to separate .html files. 
The last group stores the helper functions. It consists of the 'utils.py' and 'main.py'. The first one contains all of the helper functions which were used multiple times during other analyses, while the other one allows to create all of the plots by running one command. 

## Usage
To run the script simply make sure that you have the needed files in the "data" folder and then move to the "scripts" catalogue. Then use the following command which will create the plots and save them to the "images" folder.

```python 
python main.py 1
```

It is also possible to run separate scripts responsible for the creation of a single plot by simply using the following command in the scripts folder.
For the interactive plots:

```python 
python <script_name>.py [1]
```

For the stationary images:
```python 
python stationary/<script_name>.py [1]
```
Usage of the following parameter '[1]' allows to save the plot rather than display it.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Zofia Kochańska
Julia Smolik
