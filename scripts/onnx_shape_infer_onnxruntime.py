import argparse
import tempfile

import numpy as np
import onnx
import onnxruntime as ort
from onnx import helper

# shape infer by random inference in onnxruntime


def onnx_shape_infer_all(args):
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
    sess = ort.InferenceSession(tmp_file)

    # TODO support muti-inputs
    input0 = sess.get_inputs()[0]
    outputs = sess.get_outputs()
    input_data = np.random.uniform(0, 1, input0.shape).astype(np.float32)
    print(f"input shape: {input_data.shape}")
    output_names = [x.name for x in outputs]
    all_res = sess.run(output_names, {input0.name: input_data})
    all_shape = {}
    for output, res in zip(outputs, all_res):
        print(f'{output.name}:{res.shape}')
        all_shape[output.name] = res.shape
    del all_res

    # add value info for raw model
    onnx_model = onnx.load(args.model)
    for name, shape in all_shape.items():
        one_value_info = helper.make_tensor_value_info(
            name=name, elem_type=1, shape=list(shape)
        )
        onnx_model.graph.value_info.append(one_value_info)
    onnx.save(onnx_model, args.output)
    print(f"{args.output}, saved")


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument(
        "--model",
        type=str,
        # required=True,
    )
    _args = parse.parse_args()
    # _args.model = "/home/allen/ml_data/models/onnx/resnet18-v2-7.onnx"
    _args.output = f"{_args.model}.infer_shaped_onnxruntime.onnx"
    print(_args)

    onnx_shape_infer_all(_args)
