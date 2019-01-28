"""
Data organiser for ML tasks.

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

"""
import json
import glob
import os, sys, math

# Throws exceptions

class yottato():
    def __init__(self, configPath=None):
        usage = "Usage: \n \
            from yottato import yottato as yto \n \
            yt = yto('config.json path')"                
        self.configPath = configPath            
        if configPath is None:
            print (usage)
            raise Exception('Config JSON path not provided')
        else:
            self.__loadConfig(configPath)

    def __getVideoTrainConfig(self, config):
        for videoConfig in config['training']:
            if videoConfig["modality"] == "video":    
                return videoConfig
        raise Exception('Video training entry not found')
        
    def __getVideoFilesJson(self, jsonFile):
        if not os.path.exists(jsonFile):
           raise Exception("Config path [", jsonFile, "] doesn't exist")    
        with open(jsonFile, "r") as configFile:
            return json.load(configFile)
    def __getAudioTrainConfig(self, config):
        for audioConfig in config['training']:
            if audioConfig["modality"] == "audio":    
                return audioConfig
        raise Exception('Audio training entry not found')
           
    def __loadConfig(self, configPath):
        if not os.path.exists(configPath):
           raise Exception("Config path [", configPath, "] doesn't exist")
        with open(self.configPath, "r") as configFile:
            self.config = json.load(configFile)
            self.repoDir = self.config['globaldataRepo']
            if not os.path.exists(self.repoDir):
               raise Exception("Global repo path [", self.repoDir, "] doesn't exist")
            self.classes = self.config['classes']            
            self.trainsPerTest = math.ceil(self.config['traintestsplit'] / (100 - self.config['traintestsplit']))     
            self.sessionName = self.config['sessionname']
            self.workDir = os.path.join(self.repoDir, self.sessionName)
            self.featureFileName = self.config['featurefile']
            self.videoConfig = self.__getVideoTrainConfig(self.config)
            self.videoLoadToMemory = self.videoConfig["loadtomemory"]
            self.videoBatchSize = self.videoConfig["batchsize"]
            self.videoFileListJsonFile = self.videoConfig['trainingfilelist']
            if not os.path.exists(os.path.join(self.repoDir, self.videoFileListJsonFile)):
                print ("Training input video filelist json [", os.path.join(self.repoDir, self.videoFileListJsonFile, "] doesn't exist, skipping")
                self.videoFilesJson = None
            else:
                self.videoFilesJson = self.__getVideoFilesJson(os.path.join(self.repoDir, self.videoFileListJsonFile))
            self.videoLearningRate = self.videoConfig['learningrate']
            self.videoDecay = self.videoConfig['decay']
            self.videoEpochs = self.videoConfig['epochs']
            self.videoAlgorithm = self.videoConfig['algorithm']
            self.videoSeqLength = self.videoConfig['sequencelength']
            
            #Audio
            self.audioConfig = __getAudioTrainConfig(self.config)
            self.audioAlgorithm = self.audioConfig["algorithm"]
            self.audioFileListJsonFile = self.audioConfig['trainingfilelist']
            if not os.path.exists(os.path.join(self.repoDir, self.audioFileListJsonFile)):
                print ("Training input audio filelist json [", os.path.join(self.repoDir, self.audioFileListJsonFile), "] doesn't exist, skipping")
                self.audioFilesJson = None
            else:
                self.audioFilesJson = self.__getaudioFilesJson(os.path.join(self.repoDir, self.audioFileListJsonFile))
            
            
  
