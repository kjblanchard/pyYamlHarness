from flask_restful import Resource, Api, reqparse
import yamlModels.hostname as hostnameModel
import InputData

def GetApi(app):
    return Api(app)

class ApiEntry(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('infrastructureKey', required=True)  # add args
        parser.add_argument('projectKey', required=True)
        parser.add_argument('projectName', required=True)
        args = parser.parse_args() 
        bodyAsClass = InputData.GetInputDataFromJson(args)
        yamlData = hostnameModel.Hostname.CreateHostname(bodyAsClass.infrastructureKey, bodyAsClass.projectKey,bodyAsClass.projectName)
        print(yamlData)
        return yamlData, 200  # return data and 200 OK code
    pass