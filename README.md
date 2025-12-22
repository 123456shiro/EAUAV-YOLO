# EAUAV-YOLO
An Efficiency and Accuracy Enhanced Lightweight Detector for Small Objects in Aerial Images

# EAUAV-YOLO: Efficiency and Accuracy Enhanced Lightweight Detector for Small Objects in Aerial Images

## Overview

This repository contains the implementation of EAUAV-YOLO, a lightweight object detection framework specifically designed for unmanned aerial vehicle (UAV) applications. The framework addresses the challenges of detecting small objects in aerial imagery while maintaining computational efficiency suitable for deployment on resource-constrained UAV platforms.

## Key Features

- **Depth-augmented Spatial Convolution (3DSConv)**: Preserves fine-scale structural cues during downsampling to prevent small object features from being overwhelmed by background responses
- **Multi-path Feature Fusion Pyramid Network (MFFPN)**: Enhances cross-scale representation through high-resolution reconstruction and multi-path interactions
- **Lightweight Shared Detail-Enhanced Detection Head (LSDECD)**: Improves edge-level feature discrimination while reducing parameter count
- **Scale-aware Regression Loss (Wise-EIoU)**: Increases localization robustness for small and distant targets by emphasizing reliable geometric cues

## Architecture Components

### 1. 3D Spatial Convolution Module (3DSConv)
Preserves fine-scale spatial information during early downsampling by embedding position-aware weighting into the downsampling process. Uses average pooling followed by depth-aware convolution to estimate spatial attention weights.

### 2. Multi-path Feature Fusion Pyramid Network (MFFPN)
Balances utilization of low-level high-resolution features and high-level semantic features through:
- Triple Feature Concat (TFConcat): Aligns features from three adjacent scales
- Multiple Scale Fuse (MSFuse): Emphasizes fine-grained cues by upsampling to highest resolution

### 3. Lightweight Shared Detail-Enhanced Detection Head (LSDECD)
Employs re-parameterizable detail-enhanced convolution (DEConv) with differential operators to accentuate intensity transitions and structural irregularities, making small objects more distinguishable.

### 4. Wise-EIoU Loss Function
A scale-aware loss function that builds upon EIoU with dynamic focusing principles to improve regression stability for small objects.

## Performance

EAUAV-YOLO achieves state-of-the-art performance on UAV-oriented datasets with ultra-lightweight complexity:

### VisDrone2019 Results
- **mAP@50**: 0.413
- **mAP@50:95**: 0.247
- **Parameters**: 2.4M

### TinyPerson Results
- **mAP@50**: 0.222
- **mAP@50:95**: 0.0812
- **Parameters**: 2.4M

Compared to YOLOv11n baseline (0.334 mAP@50, 0.195 mAP@50:95 with 2.6M parameters), EAUAV-YOLO achieves 24% and 27% improvements respectively while reducing parameter count.

## Experimental Setup

- **Hardware**: Hygon C86 7390 32-core CPU, NVIDIA A40 48GB GPU
- **Training**: 300 epochs, SGD optimizer (momentum=0.937, weight_decay=0.0005)
- **Batch Size**: 8
- **Input Resolution**: 640×640
- **Learning Rate**: 0.01

## Datasets

- **VisDrone2019**: Benchmark for UAV object detection with densely distributed small objects
- **TinyPerson**: Dataset focused on extremely small human instances in aerial environments

## Applications

EAUAV-YOLO is particularly well-suited for UAV applications including:
- Search and rescue operations
- Precision agriculture monitoring
- Power line inspection
- Real-time surveillance in resource-constrained environments

## Installation

```bash
# Installation instructions would go here
```

## Usage

```bash
# Usage examples would go here
```

## Citation

If you use this work in your research, please cite our paper:

```bibtex
@article{EAUAV-YOLO,
  title={EAUAV-YOLO: An Efficiency and Accuracy Enhanced Lightweight Detector for Small Objects in Aerial Images},
  journal={Computer Vision and Image Understanding}
}
```

## Acknowledgements

This work was supported by [funding information would go here]. We thank all contributors and the computer vision community for their valuable resources and insights.

---

*Note: This README is based on the paper content. Actual implementation details may vary depending on the specific code release.*

---
