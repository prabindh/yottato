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
            from yottato import yottato as yto
            yt = yto('config.json')

yt object has details specified in the JSON