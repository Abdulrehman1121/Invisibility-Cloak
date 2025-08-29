# Green Invisibility Cloak

A Python project that creates a real-time invisibility cloak effect using OpenCV and NumPy. The program detects green-colored fabric and replaces it with a pre-recorded background, giving the illusion of disappearing.

## Features
- Real-time video processing using webcam
- Detects green cloth as the "cloak"
- Smooth masking using morphological operations and Gaussian blur
- Fullscreen display for immersive effect


## Requirements
- Python 3.13
- OpenCV
- NumPy

Install dependencies using pip:

```bash
pip install opencv-python numpy
````

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/Green-Invisibility-Cloak
```

2. Navigate to the project folder:

```bash
cd Green-Invisibility-Cloak
```

3. Run the program:

```bash
python green_invisibility_cloak.py
```

4. Make sure you have a green cloth ready for the effect. Press **`q`** to quit.

## How It Works

1. **Background Capture:** The program first captures the static background for a few seconds.
2. **Color Detection:** It converts each video frame to HSV color space and detects green color.
3. **Masking:** Smooths the mask using morphological operations and Gaussian blur.
4. **Combining Frames:** Replaces green regions with the captured background to create the invisibility effect.

## License

This project is open-source and available under the MIT License.

✨ Enjoy creating your own green invisibility cloak!
