import argparse

import onnx
import onnx.shape_inference


def onnx_shape_infer(fp):
    output = f"{fp}_shape_infer.onnx"
    onnx_model = onnx.load(fp)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    onnx.save(onnx_model, output)
    print(f"{output}, saved")


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("--input", required=True, type=str)
    args = parse.parse_args()

    onnx_shape_infer(args.input)
