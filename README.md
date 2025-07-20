# Speech Recognition System

## Overview
This basic Speech-to-Text system uses Python and the `SpeechRecognition` library to transcribe short audio clips.

## Requirements
- Python 3.x
- `speechrecognition`
- `pyaudio` (for microphone input, optional)
- A `.wav` audio file

## Setup
```bash
pip install SpeechRecognition
pip install pyaudio  # Only if you plan to use microphone input
```

## Usage
1. Place your `.wav` file in the same directory and name it `sample.wav` (or change the file name in `main.py`).
2. Run the script:
```bash
python main.py
```

## Sample Output
```text
Transcription:
Hello, this is a test of the speech recognition system.
```