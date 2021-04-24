import argparse
import os
import tempfile

import numpy as np
import onnx
import onnxruntime as rt
from onnx import helper


def onnx_dump_all(args):
    onnx_model = onnx.load(args.model)

    # add outputs to onnx_model
    outputs = [
        onnx_model.graph.node[idx].output[0]
        for idx in range(len(onnx_model.graph.node))
    ]
    for output_name in outputs:
        intermediate_layer_value_info = helper.ValueInfoProto()
        intermediate_layer_value_info.name = output_name
        onnx_model.graph.output.append(intermediate_layer_value_info)

    # save modified model to tempfile
    tmp_file = tempfile.NamedTemporaryFile().name
    onnx.save(onnx_model, tmp_file)

    # dump outputs for every blob
    onnx_model = onnx.load(tmp_file)
    sess = rt.InferenceSession(tmp_file)

    # TODO support muti-inputs
    input0 = sess.get_inputs()[0]
    outputs = sess.get_outputs()
    if args.input:
        input_data = np.load(args.input)
    else:
        input_data = np.random.uniform(0, 1, input0.shape).astype(np.float32)
    print(f"input shape: {input_data.shape}")
    output_names = [x.name for x in outputs]
    all_res = sess.run(output_names, {input0.name: input_data})

    if args.output:
        os.makedirs(args.output, exist_ok=True)
    for output, res in zip(outputs, all_res):
        print(f'{output.name}:{res.shape}')
        if args.output:
            to_save = f"{args.output}/{output.name}.npy"
            np.save(to_save, res)
            print(f"saved to file: {to_save}")


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "--model",
        type=str,
        # required=True,
    )
    parse.add_argument(
        "--input",
        type=str,
        default=None,
    )
    parse.add_argument(
        "--output",
        type=str,
        default=None,
    )
    _args = parse.parse_args()
    # _args.model = "/home/allen/ml_data/models/onnx/resnet18-v2-7.onnx"
    print(_args)

    onnx_dump_all(_args)
