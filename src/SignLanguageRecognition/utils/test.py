import ruamel.yaml

yaml = ruamel.yaml.YAML(typ="safe")
with open("/home/amadgakkhar/code/SignLanguageRecognition/yolov5s.yaml", "r") as f:
    orig = yaml.load(f)
    print("Original \n", orig["head"])

with open(
    "/home/amadgakkhar/code/SignLanguageRecognition/custom_yolov5s.yaml", "r"
) as f:
    cust = yaml.load(f)
    print("Custom \n", cust["head"])
