# Building pytorch in vscode using cmake

## clone repo

```bash

git clone https://github.com/pytorch/pytorch
git checkout -b release/1.8 origin/release/1.8

git submodule update --init --recursive

# if submodule has error
# git submodule foreach git reset --hard

```

## edit `tools/setup_helpers/cmake.py`

ref: https://gist.github.com/gglin001/115ab012750aeb86fbda9975fa49f47c

## `settings.json` in VSCode

```json
{
  "python.pythonPath": "/path_to_python",
  // for USE_SYSTEM_LIBS, maybe fail in building
  // "cmake.configureArgs": [
  //     "-DCMAKE_PREFIX_PATH=/path1/to/lib;/path2/to/lib",
  // ],
  "cmake.configureSettings": {
    "CMAKE_PREFIX_PATH": "/path_to_conda_envs_env_name/lib",
    "CMAKE_INSTALL_PREFIX": "/repos_to/pytorch/torch",
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
    "USE_GLOG": "ON",
    "BUILD_PYTHON": "ON"
    // for debug
    // "USE_OPENMP": "OFF"
    // it may error when USE_SYSTEM_LIBS
    // "USE_SYSTEM_LIBS": "ON",
    // "USE_SYSTEM_ONNX": "ON",
    // "BUILD_CUSTOM_PROTOBUF": "OFF",
  },
  "python.analysis.extraPaths": ["${workspaceFolder}"],
  // "python.envFile": "${workspaceFolder}/.env",
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}"
  }
}
```

## `launch.json` in VSCode

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": false
    },
    {
      "name": "(gdb) Attach",
      "type": "cppdbg",
      "request": "attach",
      "program": "/path_to/python",
      "processId": "${command:pickProcess}",
      "MIMode": "gdb",
      "miDebuggerPath": "/usr/bin/gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        },
        {
          "description": "Skip stdio-common files",
          "text": "-interpreter-exec console \"skip -gfi stdlib/*.c\""
        }
      ]
    }
    // build setup.py or use tasks.json
    // {
    //     "name": "setup.py",
    //     "type": "python",
    //     "request": "launch",
    //     "program": "${workspaceFolder}/setup.py",
    //     "console": "integratedTerminal",
    //     "justMyCode": false,
    //     "env": {
    //         "DEBUG": "1",
    //         "LD_LIBRARY_PATH": "/path_to/pytorch/build/lib",
    //         "LIBRARY_PATH": "/path_to/pytorch/build/lib",
    //     },
    //     "args": [
    //         "develop",
    //     ]
    // },
  ]
}
```

## `tasks.json` in VSCode

```json
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build setup.py",
      "type": "shell",
      "command": "DEBUG=1 LD_LIBRARY_PATH=/path_to/pytorch/build/lib /path_to/python setup.py develop",
      "problemMatcher": [],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

## debug

when building pytorch in debug mode, we can debug mixin python & cpp code

`demos/demo.py`, do not run it at `/path_to/pytorch`

```python
import sys  # isort: skip
import os  # isort: skip # fmt: off
sys.path.insert(0, '/path_to/pytorch')
import torch  # isort: skip

torch.set_num_threads(1)
# c++ debuger attach pid
print(os.getpid())
print(torch.__file__)

a = torch.Tensor([-1, 2, -3])
b = torch.Tensor([1, -2, 3])

# c++ add breakpoint at "aten::add"
# search below interface
# aten::add.Tensor(Tensor self, Tensor other, *, Scalar alpha=1) -> Tensor
c = torch.add(a, b)
print(c)

```
