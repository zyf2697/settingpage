import yaml


class ReadData:

    def return_data(self):
        with open("D:\mytools\yidong_work_setting\data\setting_data.yaml", "r", encoding="utf-8") as f:
            data = yaml.load(f)
            return data