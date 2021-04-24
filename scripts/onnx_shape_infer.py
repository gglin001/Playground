import argparse

import onnx
import onnx.shape_inference


def onnx_shape_infer(args):
    onnx_model = onnx.load(args.model)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    onnx.save(onnx_model, args.output)
    print(f"{args.output}, saved")


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "--model",
        # required=True,
        type=str,
    )
    _args = parse.parse_args()
    # _args.model = f"/home/allen/ml_data/models/onnx/resnet18-v2-7.onnx"
    _args.output = f"{_args.model}_shape_infer.onnx"

    onnx_shape_infer(_args)
