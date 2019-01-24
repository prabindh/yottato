"""
Convert given UCF dir, to CurtainRaiser file
Use the generated file in CurtainRaiser config json as,
"trainingfilelist" : "<filename>.json"

Requires:
ffprobe (from FFMPEG) in executable path
"""
import sys, os, glob, math, json
from subprocess import PIPE, run

def generateCRConfigFromUCF(repoPath, ucfPath):
    imageList = []
    entries = []
    imageList.extend(glob.glob(os.path.join(repoPath, ucfPath, '**', '*.avi'), recursive=True))
    for file in imageList:
        fullPath = os.path.join(repoPath, ucfPath, file)
        file = os.path.normpath(fullPath)
        file = file.split(os.sep)
        name = file[-1]
        className = file[-2]        
        result = run(["ffprobe","-v","error", "-select_streams", "v:0", "-show_entries", "stream=duration", "-of", "default=noprint_wrappers=1:nokey=1", fullPath], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        duration = result.stdout.replace('\n', '')
        slices = []
        events = []        
        events.append(className)
        slice = {'start': "00:00:00", "duration":math.floor(float(duration)), "classes": events}        
        slices.append(slice)
        entry = {'name': os.path.join(ucfPath, className,name), "slices": slices}
        entries.append(entry)
    CRConfig = {"files": entries}
    return CRConfig

def writeCurtainRaiserList(repoPath, ucfPath, jsonName):
    entries = generateCRConfigFromUCF(repoPath, ucfPath)
    with open(os.path.join(repoPath, jsonName), 'w') as fp:
        json.dump(entries, fp, sort_keys=True, indent=4)
    
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print ("Usage: <script> <global Repo absolute path> <UCF-101 directory path in repo> <json output filename>")
        sys.exit(0)
    writeCurtainRaiserList(sys.argv[1], sys.argv[2], sys.argv[3])