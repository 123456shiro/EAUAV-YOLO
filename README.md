# EAUAV-YOLO
An Efficiency and Accuracy Enhanced Lightweight Detector for Small Objects in Aerial Images

以下是一个基于您提供的学术论文内容编写的README文件：

# EAUAV-YOLO: 效率与精度增强的小型无人机图像目标检测器

## 简介

本项目实现了EAUAV-YOLO，一种专为无人机(UAV)平台设计的轻量级目标检测框架，专注于提升小目标检测的准确性和效率。该方法通过集成改进的下采样保真度、跨尺度表示、细节敏感解码和几何感知回归机制，在严格的效率约束下显著提升了小目标的可检测性。

## 主要特性

- **深度增强的空间卷积 (3DSConv)**：在下采样过程中保留小目标特征线索
- **多路径特征融合金字塔网络 (MFFPN)**：增强小目标检测的跨尺度表示能力
- **轻量级共享细节增强检测头 (LSDECD)**：在减少参数的同时强化边缘特征
- **尺度感知回归损失 (Wise-EIoU)**：提高小目标和远距离目标的定位鲁棒性

## 性能表现

在VisDrone2019和TinyPerson数据集上的实验结果表明，EAUAV-YOLO在仅2.4M参数的情况下达到了卓越的性能：
- VisDrone2019: 0.413 mAP@50 和 0.247 mAP@50:95
- TinyPerson: 0.222 mAP@50 和 0.0812 mAP@50:95

相比YOLOv11n，分别提升了24%和27%的性能指标，同时保持了极低的计算复杂度。

## 技术细节

### 核心组件

1. **3D空间卷积模块**
   - 通过空间注意力权重图保留早期下采样过程中的精细尺度结构线索
   - 使用平均池化和深度感知卷积估计空间权重

2. **多路径特征融合金字塔网络**
   - Triple Feature Concat (TFConcat): 对齐三个相邻尺度的特征
   - Multiple Scale Fuse (MSFuse): 强调细粒度线索并保留高分辨率结构

3. **轻量级共享细节增强卷积检测头**
   - 基于DEConv的可重参数化细节增强卷积
   - 使用方向差分滤波器突出强度变化和结构不规则性

4. **Wise-EIoU损失函数**
   - 结合EIoU和动态聚焦原理的尺度感知损失函数
   - 通过指数衰减项调节预测框的贡献

## 实验环境

- CPU: Hygon C86 7390 32-core
- GPU: NVIDIA A40 48GB
- 训练轮数: 300 epochs
- 批次大小: 8
- 输入分辨率: 640×640
- 初始学习率: 0.01

## 数据集支持

- VisDrone2019
- TinyPerson

## 应用场景

该检测器特别适用于资源受限的无人机平台，包括但不限于：
- 搜索救援任务
- 精准农业监测
- 电力线路巡检
- 其他需要实时小目标检测的空中应用场景

## 安装与使用

```bash
# 在此处添加安装说明
```

## 引用

如果您在研究中使用了本项目，请引用我们的论文：

```bibtex
@article{EAUAV-YOLO,
  title={EAUAV-YOLO: An Efficiency and Accuracy Enhanced Lightweight Detector for Small Objects in Aerial Images},
  journal={Computer Vision and Image Understanding}
}
```

## 致谢

感谢所有开源项目的贡献者和支持本研究的机构。

---

*注：此README基于论文内容编写，具体实现细节可能需要参考完整的源代码和训练脚本。*
