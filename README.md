# Get automatically simirality words pair in document to use Magnitude
This project provides a task for automatic extraction of synonyms using pretrained fasttext+magnitude.

・Magnitude  
https://github.com/plasticityai/magnitude

## Index
- [Dependencies](#Dependencies)
- [Usage](#Usage)
- [Result](#Result)

## Dependencies
This code is written by `Python 3.7`. Library dependent in `requirements.txt`.

|  library  |  version  |
| ---- | ---- |
|  pymagnitude  |  0.1.143  |
|  neologdn  |  0.5.1  |
|  pandas  |  1.1.5  |
|  mecab-python3  |  1.0.3  |

## Usage
Get simirality words pair to use magnitude+fasttext model quickly you run under command.

```:teminal
$ cd src
$ python find_synonym.py
```

### Select pretrained model
You can select pretrained model below 3 types.

|  TH  |  TH  |
| ---- | ---- |
|  TD  |  TD  |
|  TD  |  TD  |

### Use original text file
You want to use originl text file. Put your original file under `input/`.  
And you want to rename file, use under command to get synonym.

```
$ cd src
$ python find_synonym.py --text_file_path=../input_data/{Your original text file}
```

