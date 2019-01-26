# yottato
Python data Organiser for Yotta sized ML tasks

Organises key information required for training classifiers.

Folder hierarchy (INPUT):
<REPO> \
    <VIDEO-FILES>         - List of large source files (ex MP4)

Folder hierarchy (OUTPUT):
<REPO> \
    <SESSION-NAME>        - Generated files for this session
    <VIDEO-FILE-FEATURES> - Extracted Data for each video file

Usage:
            cd yottato
            python setup.py install
            Then from the calling script,
            from yottato import yottato as yto
            yt = yto('config.json')

yt object has values specified in the JSON and can be accessed directly