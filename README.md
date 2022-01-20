<p align="center">
    <img src="https://www.cis-openscraper.com/static/images/stack/selenium-logo.png" width="300">
</p>

# Robo v1.0.4

Robo is a python script that automates the generation and the download of the images on wombo.ai.

## Getting started

- [Requirements](#requirements)
- [Installing](#installing)
- [How to use](#how-to-use)
- [Configuration](#configuration)

## Requirements

- Python 3.10
- pip (v21.3.1)

## Installing

Install all required packages from the requirements.txt.

```shell
cd robo
pip install -r requirements.txt
```

## How to use

The usage of the script can be simple as navigating to the robo destination folder and executing the main python script file.

```shell
cd robo
python main.py
```

## Configuration

### Adding your words

To add your words of choice, navigate into the robo folder and add your words in the words.txt file. Every new word should be placed on a new line.

```shell
monkey attack
this is like free money
night programming with ambient lights
northern lights
aurora
life is not easy
coding makes me crazy
```

### Choosing your styles

By default the styles will be picked randomly. Should you need to limit the styles that will be used for the generation of the images add them as an argument separated with a comma.

```shell
python main.py "hd,vibrant"
```

The above execution of the script will randomly switch between those two styles and generate the images based on them. You can also choose only one style by adding only one style as an argument.

#### Available styles 
    
| Style             |                                                                                    
| ------------------|
| no_style          |                                                
| steampunk         |                                                                                                   
| fantasy           |                                                            
| syntwave          |  
| ukiyoe            |
| vibrant           |   
| psychic           |
| pastel            |
| hd                |
| etching           |
| mystical          |
| baroque           |
