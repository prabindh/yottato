# yottato

## Python data file Organiser

Organises key information required for training classifiers.

## Folder hierarchy (INPUT):
- `<REPO>` \
   - `<VIDEO-FILES>`         - List of large source files (ex MP4)

## Folder hierarchy (OUTPUT):
- `<REPO>`
   - `<SESSION-NAME>`        - Generated files for this session \

      - `<VIDEO-FILE-FEATURES>` - Extracted Data for each video file


## Installation via pip:

`pip install git+https://github.com/prabindh/yottato.git#egg=yottato`

### Usage:
            `from yottato import yottato as yto`
            `yt = yto('config.json')`
            `yt object has details specified in the JSON`

## Usage via setup
```
            cd yottato

            python setup.py install

            Then from the calling script,

            from yottato import yottato as yto

            yt = yto('config.json')
```
yt object has values specified in the JSON and can be accessed directly
