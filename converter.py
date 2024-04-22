import m2cgen as mt
import pickle


def convert_model_to_c(model, export_path: str):
    code = mt.export_to_c(model)
    with open(export_path, "w") as file:
        file.write(code)
        file.close()


def convert_model_to_java(model, export_path: str):
    code = mt.export_to_java(model)
    with open(export_path, "w") as file:
        file.write(code)
        file.close()
