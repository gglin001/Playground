# Debug TVM in VSCode

## `.vscode/settings.json`

```json
{
  "python.pythonPath": "/path/to/python",
  "python.envFile": "${workspaceFolder}/.env",
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "${workspaceFolder}/python:${env:PYTHONPATH}",
    "TVM_BACKTRACE": "1",
    "DMLC_LOG_DEBUG": "1"
  },
  "ffi_navigator.pythonpath": "/path/to/python",
  "cmake.configureSettings": {
    // using conda
    "CMAKE_PREFIX_PATH": "/path/to/lib",
    "BUILD_SHARED_LIBS": "ON",
    "USE_LLVM": "ON",
    "USE_RELAY_DEBUG": "ON",
    "USE_TARGET_ONNX": "ON",
    "USE_MKLDNN": "OFF",
    "USE_VTA_FSIM": "ON",
    "USE_STACKVM_RUNTIME": "ON",
    "USE_GRAPH_EXECUTOR": "ON",
    "USE_GRAPH_EXECUTOR_DEBUG": "ON",
    "USE_MICRO_STANDALONE_RUNTIME": "ON"
  },
  "python.analysis.extraPaths": ["python", "${fileDirname}"]
}
```

## `.vscode/launch.json`

```json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "name": "python current",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/python",
        "TVM_BACKTRACE": "1",
        "DMLC_LOG_DEBUG": "1"
      },
      "justMyCode": false
    },
    {
      "name": "gdb attach",
      "type": "cppdbg",
      "request": "attach",
      "program": "/path/to/python",
      "processId": "${command:pickProcess}",
      "additionalSOLibSearchPath": "${workspaceFolder}/build",
      "MIMode": "gdb",
      "setupCommands": [
        {
          "description": "Enable pretty-printing for gdb",
          "text": "-enable-pretty-printing",
          "ignoreFailures": true
        }
        // {
        //     // "text": "skip file ${workspaceFolder}/src/relay/backend/build_module.cc",
        //     // "text": "skip -gfi ${workspaceFolder}/*",
        // }
      ]
    }
  ]
}
```

## `.env`

```
PYTHONPATH=${workspaceFolder}/python:${PYTHONPATH}
```

## How to debug

```
0. build TVM in debug mode, using VSCode cmake-tools
1. debug python script, set breakpoint
2. start gdb attach, select pid using python script name
3. press F5 enter in C++

```
