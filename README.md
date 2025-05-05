# Performance Monitor Client

A command-line client for connecting to the Performance Monitor server.

## Downloads

Download the client for your operating system:

- **Windows** : [Artifact download URL](https://github.com/Mickyverma24/client-cli/actions/runs/14834462307/artifacts/3061187537)
- **Linux** : [Artifact download URL](https://github.com/Mickyverma24/client-cli/actions/runs/14834462307/artifacts/3061182521)
- **Mac** : [Artifact download URL](https://github.com/Mickyverma24/client-cli/actions/runs/14834462307/artifacts/3061181427)

## Usage Instructions

1. Download the client for your respective operating system.
2. Connect to the main server using the following commands:
3. Get your auth_key and host_url from the frontend or dashboard [Here](https://pmfrontend.netlify.app/)

### Windows:

```cmd
pmclient.exe connect --auth_key [your_api_key] --host_url [Host_URL]
```

### Linux:

```bash
./pmclient.exe connect --auth_key [your_api_key] --host_url [Host_URL]
```

### macOS:

```bash
./pmclient.exe connect --auth_key [your_api_key] --host_url [Host_URL]
```

4. To disconnect kill the terminal or just do

```bash
pmclient.exe disconnect
./pmclient.exe disconnect
```

## Notes

- If you encounter any issues while downloading or using the CLI, please contact me at vermaravi8809@gmail.com
- This is a simple CLI tool for connecting your computer or server to the main server via socket connection to monitor system performance.
- Built using the psutil and platform libraries in Python.
- It won't harm your pc tested with all os and it's open to public you can see code, Basic code are there.

## How i Made this [Click Here](https://github.com/Mickyverma24/performance-hub-server)
