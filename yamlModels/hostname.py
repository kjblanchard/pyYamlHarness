import yaml

class Hostname(yaml.YAMLObject):
    yaml_tag = '!Hostname'

    def __init__(self,infrastructureKey, projectKey, serviceName):
        self.harnessApiVersion = '1.0'
        self.type = 'INFRA_DEFINITION'
        self.cloudProviderType = 'KUBERNETES_CLUSTER'
        self.deploymentType = 'KUBERNETES'
        self.infrastructure = self.infrastructure(infrastructureKey, projectKey, serviceName)

    class infrastructure(yaml.YAMLObject):
        def __init__(self, infrastructureName, projectKey, serviceName):
            self.type = 'DIRECT_KUBERNETES'
            self.cloudProviderName: infrastructureName
            self.namespace = f'uwm-{projectKey}'
            self.releaseName = f'{serviceName}'

    def CreateHostname(infrastructureName, projectKey, serviceName):
        yaml.emitter.Emitter.process_tag = Hostname.noopToRemoveOutput
        return yaml.dump(Hostname(infrastructureName, projectKey, serviceName),sort_keys=False)

    # This is needed to remove output
    def noopToRemoveOutput(self, *args, **kw):
        pass


print(Hostname.CreateHostname('hi','nou','hello'))