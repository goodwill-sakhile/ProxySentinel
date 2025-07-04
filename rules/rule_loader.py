import yaml

class RuleLoader:
    def __init__(self, config_path="config/config.yaml"):
        self.config_path = config_path

    def load_rules(self):
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)
