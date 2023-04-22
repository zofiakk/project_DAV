# Covid in South Africa
![alt text](https://github.com/zofiakk/project_DAV/blob/master/images/Flag-map_of_South_Africa.svg.png)

All of the scripts contained in a "scripts" folder are written in python. They allow to analyze and visualize the data pertaining the covid pandemic in South Africa and its neighboring countries.

Datasets used in this project contain summary statistics as well as inferential statistics (for example estimated masks usage).

## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Authors](#author)

## General Information

All of the scripts can be grouped into 3 categories. The first one is stored in the 'stationary' subfolder and allows to create non-interactive plots which can be saved to jpg format and are used in the pdf poster.
The second group consist of all of the other scripts except for 'utils.py'. They are responsible for creating interactive plots which then can be saved to separate .html files. 
The last group stores the helper functions in the 'utils.py' file. They are the functions which were used multiple times during other analyses and help to avoid code repetitions. 

## Usage
To run the script simply make sure that you have the needed files in the "data" folder and then move to the "scripts" catalogue. Then use the following command which will create the plot and save it to the "images" folder.

```python 
python <file_name.py> 1
```

To create a stationary plot simply ad the correct path to the command:

```python 
python stationary/<script_name>.py [1]
```
Usage of the following parameter '[1]' allows to save the plot rather than display it.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
Zofia Kochańska, 
Julia Smolik
