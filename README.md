# Sign Language Recognition Model

Enhancing Brazilian Sign Language Recognition through Skeleton Image Representation

---

## Overview

This repository contains a simplified version of the code for training a Sign Language Recognition (SLR) model based on skeleton images, as described in the paper:

> **Alves, Carlos Eduardo GR, Francisco de Assis Boldt, and Thiago M. Paixão. "Enhancing Brazilian Sign Language Recognition through Skeleton Image Representation." arXiv preprint arXiv:2404.19148 (2024).**

This version is designed for quick-start experiments and user-friendliness. For the full experimental codebase, see the [original repository](https://github.com/Dudu197/sign-language-recognition).

---

## Table of Contents
- [Overview](#overview)
- [Requirements & Installation](#requirements--installation)
- [Dataset](#dataset)
- [Directory Structure](#directory-structure)
- [Training](#training)
- [Results](#results)
- [Citation](#citation)
- [License](#license)

---

## Requirements & Installation

- **Python 3.7+**
- All required libraries are listed in `requirements.txt`.

**Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## Dataset

This code was tested using the MINDS-Libras dataset, but can be adapted for other sign language datasets as well:

### MINDS-Libras
- 20 signs, 12 signers, 5 repetitions per sign.
- [Download preprocessed MINDS-Libras data](https://drive.google.com/file/d/1qx2JudpjPgpp4-fpJ7YVMrszWV4lYPCd/view?usp=drive_link)
- Place the dataset in the `datasets` folder.

### Libras-UFOP
- 56 signs, 5 signers, 8–16 repetitions per sign.
- [Paper](https://www.sciencedirect.com/science/article/pii/S0957417420309143)
- Preprocessed data may be available in the original repository or by request.

### Include-50
- 50 signs, larger and more diverse dataset.
- [Download preprocessed Include-50 data](https://drive.google.com/file/d/14SbYpFIbHi_Is1hD9XH9Sg_5eF--xtAw/view?usp=sharing)
- Place the dataset in the `datasets` folder.

### KSL (Korean Sign Language)
- Korean Sign Language dataset.
- [Download preprocessed KSL data](https://drive.google.com/file/d/1-27qX-KtCE3RknzASvXuJ-aVZAQ60tNj/view?usp=sharing)
- Place the dataset in the `datasets` folder.

> **Note:** This repository is primarily set up for MINDS-Libras, but you can adapt the code for other datasets by adjusting file paths and preprocessing as needed.

---

## Directory Structure

- `datasets/` – Place your dataset files here.
- `image_representations/` – Skeleton image representation code.
- `models/` – Model definitions (e.g., ResNet18).
- `results/` – Results and logs will be saved here.
- `model_training.py` – Main training script.
- `train_minds.py` – Example training script for MINDS-Libras.
- `train.sh` – Shell script to run training.

---

## Training

To train the model using the MINDS-Libras dataset, run:

```bash
sh train.sh
```

This will train the model and save results in the `results` folder.

For more details about how to train, check [https://github.com/Dudu197/sign-language-recognition/blob/main/03_model_training/README.md](https://github.com/Dudu197/sign-language-recognition/blob/main/03_model_training/README.md)

---

## Results

Our model achieves strong performance on multiple sign language datasets:

- **MINDS-Libras:**
  - Accuracy: ~0.93
  - +2 percentage points accuracy, +3 F1-Score over previous SOTA

- **Libras-UFOP:**
  - Accuracy: ~0.82
  - +8 percentage points accuracy, +9 F1-Score over previous SOTA

- **Include-50:**
  - Accuracy: ~0.97 (ResNet18 + Skeleton-DML)

- **KSL (Korean Sign Language):**
  - Accuracy: ~0.63 (ResNet18 + Skeleton-DML)

For more results and details, see the [original paper](https://arxiv.org/abs/2404.19148).

---

## Citation

If you use this code for your research, please cite our paper:

> Alves, Carlos Eduardo GR, Francisco de Assis Boldt, and Thiago M. Paixão. "Enhancing Brazilian Sign Language Recognition through Skeleton Image Representation." arXiv preprint arXiv:2404.19148 (2024).

**BibTeX:**
```bibtex
@article{alves2024enhancing,
  title={Enhancing Brazilian Sign Language Recognition through Skeleton Image Representation},
  author={Alves, Carlos Eduardo GR and Boldt, Francisco de Assis and Paix{a}o, Thiago M},
  journal={arXiv preprint arXiv:2404.19148},
  year={2024}
}
```

---

## License

This project is licensed under the terms of the MIT License.
