# MIT 6.100L: Problem Set Submissions

[![MIT License](https://img.shields.io/github/license/dangtrungan/mit-6.100l)](LICENSE)

Solutions to the six problem sets from MIT 6.100L, Introduction to Computer Science and Programming using Python. Each set covers a distinct programming concept: basic Python, financial calculations, the Hangman game, document similarity with TF-IDF, tree data structures and one-time pad encryption, and image steganography.

## Problem Sets

| Set | Topic | Main Files |
|-----|-------|------------|
| 0 | Python environment setup | `ps0/ps0.py` |
| 1 | Savings calculator with bisection search | `ps1/ps1a.py`, `ps1/ps1b.py`, `ps1/ps1c.py` |
| 2 | Hangman with guessing mechanics | `ps2/hangman.py` |
| 3 | Document distance and TF-IDF | `ps3/document_distance.py` |
| 4 | Binary trees, heaps, one-time pad encryption | `ps4/ps4a.py`, `ps4/ps4b.py`, `ps4/ps4c.py` |
| 5 | Color blindness filters and LSB steganography | `ps5/ps5.py` |

## Installation

Requires Python 3.8 and `numpy`, `matplotlib`, `pillow`.

```bash
git clone https://github.com/dangtrungan/mit-6.100l.git
cd mit-6.100l
pip install numpy matplotlib pillow
```

## Usage

### Play Hangman (ps2)

```bash
python ps2/hangman.py
```

### Decrypt a one-time-pad story (ps4)

```bash
python ps4/ps4c.py
```

### Simulate color blindness (ps5)

```python
from ps5 import img_to_pix, pix_to_img, filter
from PIL import Image

im = Image.open('ps5/image_15.png')
pixels = img_to_pix('ps5/image_15.png')
filtered = filter(pixels, 'red')
result = pix_to_img(filtered, im.size, 'RGB')
result.show()
```

### Extract a hidden image with LSB steganography (ps5)

```python
from ps5 import reveal_image

reveal_image('ps5/hidden1.bmp').show()
```

## Contributing

This repository stores completed coursework. Open an issue for bug reports.

## License

MIT. See [LICENSE](LICENSE).
