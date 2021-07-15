# VSCode Set Terminal Env From a Script

## `.vscode/settings.json`

```json
{
  // ...

  // static env for dev
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "${workspaceFolder}/python",
    "GLOG_v": "10"
  },

  // use new terminal.integrated.profiles
  "terminal.integrated.defaultProfile.linux": "bash_env",

  // terminal.integrated.profiles.PLATFORM
  "terminal.integrated.profiles.linux": {
    "bash_env": {
      "path": "/bin/bash",
      "args": ["--rcfile", "/abs_path/env_set.sh"]
    }
  }
}
```

## `/abs_path/env_set.sh`

```shell

source /path_to_xxx/env1.sh

export XXX=ABC

echo use env_set

```

## Debug

`.vscode/launch.json`

```json

"configurations": [
    {
        "name": "Python",
        "type": "python",
        "request": "launch",
        "program": "${file}",
        "console": "integratedTerminal",
        "justMyCode": false,
        // "env": {
        //     "GLOG_v": "10",
        // }
    }
]

```
