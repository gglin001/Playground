# Building pytorch in vscode using cmake

## clone repo

```bash

git clone https://github.com/pytorch/pytorch
git checkout -b release/1.8 origin/release/1.8

git submodule init
git submodule update

# if submodule has error
# git submodule foreach git reset --hard

cd third_party/fbgemm/
git submodule init third_party/asmjit
git submodule update third_party/asmjit

# or
# git submodule init --update third_party/asmjit

```

## `settings.json` in VSCode

```json
{
  "python.pythonPath": "/path/to/python",
  // for USE_SYSTEM_LIBS
  // "cmake.configureArgs": [
  //     "-DCMAKE_PREFIX_PATH=/path1/to/lib;/path2/to/lib",
  // ],
  "cmake.configureSettings": {
    "CMAKE_PREFIX_PATH": "/home/allen/.miniconda3/envs/py36/lib",
    "CMAKE_INSTALL_PREFIX": "install",
    "BUILD_SHARED_LIBS": "ON",
    "BUILD_CAFFE2": "OFF",
    "BUILD_CAFFE2_OPS": "OFF",
    "BUILDING_WITH_TORCH_LIBS": "OFF",
    "USE_CUDA": "OFF",
    "USE_ROCM": "OFF",
    "USE_FBGEMM": "ON",
    "USE_FAKELOWP": "OFF",
    "USE_QNNPACK": "OFF",
    "USE_KINETO": "OFF",
    "USE_NATIVE_ARCH": "OFF",
    "USE_NNPACK": "OFF",
    "USE_MKLDNN": "OFF",
    "USE_TENSORPIPE": "OFF",
    "USE_XNNPACK": "OFF",
    "USE_GLOO": "OFF",
    "USE_LITE_PROTO": "ON",
    "USE_DISTRIBUTED": "OFF",
    "USE_GLOG": "ON"
    // it may error when USE_SYSTEM_LIBS
    // "USE_SYSTEM_LIBS": "ON",
    // "USE_SYSTEM_ONNX": "ON",
    // "BUILD_CUSTOM_PROTOBUF": "OFF",
  }
}
```

## debug

when building pytorch in debug mode, we can debug mixin python & cpp code
