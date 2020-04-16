import yaml

"""
Singleton Configuration that takes in the configuration specified by the user in the `config.yaml`
"""
configuration_abs_path = "/Users/eddie/Documents/SchoolProjects/pick-tool-team01-melji/src/ui/gui/configuration/config.yaml"


class Configuration:
    class __Configuration:
        def __init__(self):
            with open(configuration_abs_path, "r") as stream:
                try:
                    self.config_values = yaml.safe_load(stream)
                    print(self.config_values)
                except yaml.YAMLError as e:
                    print(e)

        def get_intake_values(self, service):
            if self.config_values:
                if service.__contains__("none"):
                    return self.config_values["intake"]
                else:
                    try:
                        data = self.config_values["intake"][service]
                        return data
                    except:
                        return self.config_values["intake"]

    instance = None

    def __init__(self):
        if not Configuration.instance:
            Configuration.instance = Configuration.__Configuration()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def get_intake_values(self, service="none"):
        return Configuration.instance.get_intake_values(service)


configuration = Configuration()
print(configuration.get_intake_values(service="splunk"))
