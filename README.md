# EAUAV-YOLO

**EAUAV-YOLO: An Efficiency and Accuracy Enhanced Lightweight Detector for Small Objects in Aerial Images**

---

## Overview

This repository contains the implementation of **EAUAV-YOLO**, a lightweight object detection framework specifically designed for unmanned aerial vehicle (UAV) applications. The framework addresses the challenges of detecting small objects in aerial imagery while maintaining computational efficiency suitable for deployment on resource-constrained UAV platforms.

The project is built upon [Ultralytics YOLOv11](https://github.com/ultralytics/ultralytics) and introduces several novel architectural components and a scale-aware regression loss.

---

## Key Features

- **Depth-augmented Spatial Convolution (3DSConv / DSConv)**: Preserves fine-scale structural cues during downsampling to prevent small object features from being overwhelmed by background responses.
- **Multi-path Feature Fusion Pyramid Network (MFFPN)**: Enhances cross-scale representation through high-resolution reconstruction and multi-path interactions (**TFConcat** + **MSFuse**).
- **Lightweight Shared Detail-Enhanced Detection Head (LSDECD)**: Improves edge-level feature discrimination while reducing parameter count.
- **Scale-aware Regression Loss (Wise-EIoU)**: A dynamic focusing loss built upon EIoU that increases localization robustness for small and distant targets by emphasizing reliable geometric cues.

---

## Repository Structure

```
EAUAV-YOLO-main/
├── train.py                         # Training entry script
├── detect.py                        # Inference / detection entry script
└── ultralytics/
    ├── cfg/
    │   ├── models/EAUAV.yaml        # Model architecture configuration
    │   ├── datasets/VisDrone.yaml   # VisDrone dataset configuration
    │   └── datasets/TinyPerson.yaml # TinyPerson dataset configuration
    ├── nn/
    │   ├── modules/                 # Standard YOLO modules (backbone, neck, head)
    │   ├── extra_modules/           # Custom modules (DSConv, TFConcat, MSFuse, blocks, deconv)
    │   └── tasks.py                 # Model & training task definitions
    └── utils/
        ├── loss.py                  # Loss computation (includes WiseIouLoss + EIoU)
        └── metrics.py               # Metric computation (includes WiseIouLoss class)
```

---

## Architecture Components

### 1. Depth-augmented Spatial Convolution (DSConv)

Preserves fine-scale spatial information during early downsampling by embedding position-aware weighting into the downsampling process. Average pooling is followed by depth-aware convolution to estimate spatial attention weights.

### 2. Multi-path Feature Fusion Pyramid Network (MFFPN)

Balances the utilization of low-level high-resolution features and high-level semantic features through:
- **Triple Feature Concat (TFConcat)**: Aligns features from three adjacent scales.
- **Multiple Scale Fuse (MSFuse)**: Emphasizes fine-grained cues by upsampling to the highest resolution.

### 3. Lightweight Shared Detail-Enhanced Detection Head (LSDECD)

Employs re-parameterizable detail-enhanced convolution (**DEConv**) with differential operators to accentuate intensity transitions and structural irregularities, making small objects more distinguishable.

### 4. Wise-EIoU Loss Function

A scale-aware bounding-box regression loss that builds upon **EIoU** with dynamic focusing principles to improve regression stability for small objects. Implemented in:
- `ultralytics/utils/metrics.py` — the `WiseIouLoss` class (`ltype='EIoU'`).
- `ultralytics/utils/loss.py` — the `BboxLoss` class that enables WiseIoU via `use_wiseiou = True`.

---

## Performance

EAUAV-YOLO achieves state-of-the-art performance on UAV-oriented datasets with an ultra-lightweight complexity budget.

### VisDrone2019 Results

| Metric        | EAUAV-YOLO | YOLOv11n (baseline) |
|---------------|-----------:|---------------------:|
| mAP@50        | **0.413**  | 0.334                |
| mAP@50:95     | **0.247**  | 0.195                |
| Parameters    | **2.4M**   | 2.6M                 |

### TinyPerson Results

| Metric        | EAUAV-YOLO (ours) | YOLOv11n (baseline) |
|---------------|-------------------:|---------------------:|
| mAP@50        | **0.222**          | 0.182                |
| mAP@50:95     | **0.0812**         | 0.0587               |
| Parameters    | **2.4M**           | 2.6M                 |

Compared to the YOLOv11n baseline, EAUAV-YOLO achieves **~24%** and **~27%** improvements on VisDrone (0.413 vs 0.334 mAP@50, 0.247 vs 0.195 mAP@50:95), and **~22%** and **~38%** improvements on TinyPerson (0.222 vs 0.182 mAP@50, 0.0812 vs 0.0587 mAP@50:95), while also reducing the parameter count from 2.6M to 2.4M.

---

## Experimental Setup

- **Hardware**: Hygon C86 7390 32-core CPU, NVIDIA A40 48GB GPU.
- **Training**: 300 epochs, SGD optimizer (momentum = 0.937, weight decay = 0.0005).
- **Batch Size**: 32.
- **Input Resolution**: 640 × 640.
- **Learning Rate**: 0.01.
- **AMP (Mixed Precision)**: Disabled.
- **Optimizer**: SGD.

---

## Datasets

- **VisDrone2019**: A benchmark for UAV object detection with densely distributed small objects.
- **TinyPerson**: A dataset focused on extremely small human instances in aerial environments.

Dataset configuration files are provided in `ultralytics/cfg/datasets/`. Please edit the `path:` field inside each YAML file to point to your local dataset root directory, for example:

```yaml
path: /path/to/visdrone        # dataset root directory
train: VisDrone2019-DET-train/images
val: VisDrone2019-DET-val/images
test: VisDrone2019-DET-test-dev/images
```

---

## Installation

### 1. Prerequisites

- Python ≥ 3.9
- PyTorch ≥ 2.0 with CUDA support (recommended)

### 2. Install Ultralytics

```bash
pip install ultralytics
```

### 3. Clone & Override Custom Files

This repository extends the official `ultralytics` package by replacing / adding the following files:

```
ultralytics/cfg/models/EAUAV.yaml         # Custom model
ultralytics/cfg/datasets/VisDrone.yaml     # Dataset config (edit `path`)
ultralytics/cfg/datasets/TinyPerson.yaml   # Dataset config (edit `path`)
ultralytics/nn/extra_modules/              # Custom modules (DSConv, TFConcat, MSFuse, ...)
ultralytics/nn/tasks.py                    # Modified to register custom modules & losses
ultralytics/utils/loss.py                  # Modified BboxLoss with WiseIoU / EIoU support
ultralytics/utils/metrics.py               # WiseIouLoss class
```

In order to use EAUAV-YOLO's custom modules and losses, you must either:

- **Option A (Recommended)**: Copy the files from this repo into your local `site-packages/ultralytics/` folder, overlaying the original files — or, better yet, place the entire `EAUAV-YOLO-main/ultralytics/` folder **before** the pip-installed one in `sys.path` (see `train.py` usage notes below).
- **Option B**: Install Ultralytics in editable mode and overlay the files directly.

Whichever option you choose, make sure Python resolves `from ultralytics import ...` to this repository's modified `ultralytics/` folder. You can verify by running:

```python
import ultralytics
print(ultralytics.__file__)  # should point to YOUR modified ultralytics folder
```

---

## Usage

### Training

Edit `train.py` to set the correct dataset and model YAML paths, then run:

```bash
python train.py
```

Key arguments used in `train.py`:

```python
model = YOLO('ultralytics/cfg/models/EAUAV.yaml')
model.train(
    data='ultralytics/cfg/datasets/VisDrone.yaml',
    cache=False,
    imgsz=640,
    epochs=300,
    batch=32,
    close_mosaic=0,
    workers=4,
    device='0',
    optimizer='SGD',
    conf=0.02,
    amp=False,
    project='runs/train',
    name='exp',
)
```

### Inference / Detection

Edit `detect.py` to set your own `.pt` weights path and image source, then run:

```bash
python detect.py
```

```python
model = YOLO('/path/to/your/best.pt')
model.predict(
    source='/path/to/image.jpg',
    imgsz=640,
    project='runs/detect',
    name='exp',
    save=True,
)
```

## Citation

If you use this work in your research, please cite our paper:

```bibtex
@article{EAUAV-YOLO,
  title   = {EAUAV-YOLO: An Efficiency and Accuracy Enhanced Lightweight Detector for Small Objects in Aerial Images},
  journal = {Computer Vision and Image Understanding}
}
```


*Note: This README is based on the paper content. Actual implementation details may vary depending on the specific code release.*
