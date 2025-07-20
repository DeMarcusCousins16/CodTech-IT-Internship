# Neural Style Transfer

## Overview
This script implements neural style transfer using PyTorch and VGG19 to apply an artistic style to a content image.

## Requirements
- Python 3.x
- torch
- torchvision
- Pillow
- matplotlib

## Setup
```bash
pip install torch torchvision pillow matplotlib
```

## Usage
1. Place a `content.jpg` and `style.jpg` in the project directory.
2. Run the script:
```bash
python main.py
```
3. The styled image will be saved as `output.png`.

## Sample Output
An artistic rendering of `content.jpg` using the style of `style.jpg`.