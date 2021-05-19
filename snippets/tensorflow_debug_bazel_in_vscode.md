# Debug TensorFlow in VSCode

## clone repo

```bash

git clone https://github.com/tensorflow/tensorflow
# git checkout ...

```

## install bazel

```bash

# download bazel from https://github.com/bazelbuild/bazel/releases
# install bazel to ~/.local/bin
# export PATH ...

```

## configure

```bash

# configure for build
./configure

```

## quick test debug c++

```bash

# quick test debug
# -c dbg --can_be--> --copt="-g" --strip=never
bazel build --copt="-O0" -c dbg //tensorflow/c/kernels:tensor_shape_utils_test

# set breakpoint in
# tensorflow/c/kernels/tensor_shape_utils_test.cc

```

`launch.json` for quick test debug

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "debug test",
      "type": "cppdbg",
      "request": "launch",
      "program": "${workspaceFolder}/bazel-bin/tensorflow/c/kernels/tensor_shape_utils_test",
      "args": [],
      "stopAtEntry": false,
      "cwd": "${workspaceFolder}",
      "environment": [],
      "externalConsole": false,
      "MIMode": "gdb",
      "miDebuggerPath": "/usr/bin/gdb",
      "sourceFileMap": {
        "/proc/self/cwd/tensorflow": "${workspaceFolder}/tensorflow"
        // "/proc/self/cwd/external": "${workspaceFolder}/bazel-tensorflow_master/external"
      },
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
  ]
}
```

## debug mixin python&c++ code

```bash

# build build_pip_package
# -c dbg --can_be--> --copt="-g" --strip=never
bazel build --copt="-O0" -c dbg  //tensorflow/tools/pip_package:build_pip_package

# gen wheel
# ./bazel-bin/tensorflow/tools/pip_package/build_pip_package ./tf_wheel

```

`demo.py`

```python
import sys  # isort :skipe
# debug tf
sys.path.insert(0, 'bazel-bin/tensorflow/tools/pip_package/build_pip_package.runfiles/org_tensorflow')  # isort :skipe
import tensorflow as tf  # isort :skipe
import os

print(os.getpid())
print(tf.__file__)

a = tf.add([1, 2, 3], [-1, -2, -3])
print(a)

```

`launch.json` for debug

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
            "console": "integratedTerminal"
        },
        {
            "name": "(gdb) Attach",
            "type": "cppdbg",
            "request": "attach",
            "program": "/path_to/python",
            "processId": "${command:pickProcess}",
            "MIMode": "gdb",
            // ref: https://github.com/microsoft/vscode-cpptools/issues/6019
            // https://code.visualstudio.com/docs/cpp/cpp-debug#_locate-source-files
            "sourceFileMap": {
                "/proc/self/cwd/tensorflow": "${workspaceFolder}/tensorflow",
                // "/proc/self/cwd/external": "${workspaceFolder}/bazel-tensorflow_master/external",
            },
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
        },
```

## generate `compile_commands.json`

see [tf-bazel-compilation-db](https://github.com/gglin001/tf-bazel-compilation-db)

after running shell script, copy `bazel-tensorflow/compile_commands.json` (or other path) to `${workspaceFolder}/compile_commands.json`

`c_cpp_properties.json`

```json
{
  "configurations": [
    {
      "name": "Linux",
      "includePath": ["${workspaceFolder}/**"],
      "defines": [],
      "compilerPath": "/usr/bin/clang-10",
      "cStandard": "c11",
      "cppStandard": "c++14",
      "intelliSenseMode": "linux-clang-x64",
      // use compile_commands.json
      "compileCommands": "${workspaceFolder}/compile_commands.json"
    }
  ],
  "version": 4
}
```
