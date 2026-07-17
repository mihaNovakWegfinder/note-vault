
```
{
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "lime-adapter",
            "suppressMultipleSessionWarning": true,
            "type": "debugpy",
            "request": "launch",
            "python": "${workspaceFolder}/../.venv/bin/python",
            "module": "imob_lime_adapter",
            "args": [],
            "cwd": "${workspaceFolder}",
            "env": {
                "IMOB_DEV_MODE": "1",
                "PYTHONASYNCIODEBUG": "1",
                "OBJC_DISABLE_INITIALIZE_FORK_SAFETY": "YES",
                "DYLD_FALLBACK_LIBRARY_PATH": "/opt/homebrew/lib"
            },
            "console": "integratedTerminal",
            "justMyCode": false,
            "preLaunchTask": "uv-sync"
        }
    ]
}
```