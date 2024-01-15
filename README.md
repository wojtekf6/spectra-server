# spectra-server

## Introduction
Spectra server - use to get video from camera and emit on socket.

## Requirements
This project requires Python 3.x. Dependencies are listed in the `requirements.txt` file.

## Installation
1. Clone the repository:
   ```
   git clone [repository URL]
   ```
2. Navigate to the project directory:
   ```
   cd [project directory]
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration
Configure the application settings in the `config.py` file. Available settings:

- `PORT`: The port on which the server will run (default is 5000).
- `NAMESPACE`: Socket path (default is "/video").
- `FRAME_WIDTH`: Width of the video frame (default is 640).
- `FRAME_HEIGHT`: Height of the video frame (default is 480).

Example `config.py`:
```python
PORT = 5000
NAMESPACE = "/video"
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
```

## Running the Project
To run the project, execute:
```
python main.py
```

## Device as an access point
- RaspberryPi: https://learn.adafruit.com/setting-up-a-raspberry-pi-as-a-wifi-access-point/install-software
- Nvidia Jetson: https://www.myzhar.com/blog/the-myzharbot-project/software/nvidia-jetson-tx1-access-point/