import json

class InputData(object):
    def __init__(self, infrastructureKey, projectKey, projectName):
        self.infrastructureKey = infrastructureKey
        self.projectKey = projectKey
        self.projectName = projectName

def GetInputDataFromJson(obj):
        return InputData(obj['infrastructureKey'], obj['projectKey'], obj['projectName'])