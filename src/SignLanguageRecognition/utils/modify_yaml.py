import ruamel.yaml

yaml = ruamel.yaml.YAML(typ="rt")


def modify_yaml(file_path, write_file_path, key, value):
    with open(file_path, "r") as f:
        # data = yaml.load(f, Loader=ruamel.yaml.RoundTripLoader)
        data = yaml.load(f)
        data[f"{key}"] = f"{value}"
        # print(data)
    with open(write_file_path, "w") as file:
        # yaml.dump(data, file, Dumper=ruamel.yaml.RoundTripDumper)
        yaml.dump(data, file)
    print("done!")


modify_yaml(
    "/home/amadgakkhar/code/SignLanguageRecognition/yolov5s.yaml",
    "/home/amadgakkhar/code/SignLanguageRecognition/custom_yolov5s.yaml",
    key="nc",
    value="6",
)
