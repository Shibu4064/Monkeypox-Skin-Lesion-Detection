# Monkeypox Skin Lesion Detection
<!--
README generated for:
Deep Learning Architectures for Real-Time Monkeypox Detection:
A Comparative Study of CNNs, Transformers, and Siamese Networks
-->

<div align="center">

# 🧬 Deep Learning Architectures for Real-Time Monkeypox Detection  
### A Comparative Study of CNNs, Vision Transformers, and Siamese Networks

[![Paper](https://img.shields.io/badge/Paper-ICCIT%202025-blue)](#citation)
[![Task](https://img.shields.io/badge/Task-Medical%20Image%20Classification-brightgreen)](#overview)
[![Models](https://img.shields.io/badge/Models-CNN%20%7C%20ViT%20%7C%20Siamese-orange)](#models)
[![Framework](https://img.shields.io/badge/Framework-PyTorch%20%7C%20TensorFlow-lightgrey)](#quick-start)
[![Status](https://img.shields.io/badge/Status-Research%20Prototype-purple)](#clinical-and-ethical-note)

**Real-time AI-assisted screening of Mpox skin lesions using deep learning, transfer learning,  
Vision Transformers, and similarity-based Siamese representation learning.**

</div>

---

## 📌 Overview

This repository supports the paper:

> **Deep Learning Architectures for Real-Time Monkeypox Detection:  
> A Comparative Study of CNNs, Transformers, and Siamese Networks**

The study investigates automated **Mpox / monkeypox skin-lesion detection** using modern computer vision architectures. It compares the strengths of **Convolutional Neural Networks**, **Vision Transformers**, and **Siamese Neural Networks** across both:

- **Binary classification:** Mpox vs. Non-Mpox  
- **Multi-class classification:** Mpox, Chickenpox, Measles, Cowpox, HFMD, and Healthy skin

The motivation is simple: **PCR testing is reliable but can be expensive, slower, and less accessible in resource-limited settings**. AI-based visual screening can act as a supportive tool for rapid triage, early awareness, and healthcare decision support.

> ⚠️ This work is a **research prototype** and is not intended to replace professional clinical diagnosis.

---

## ✨ Key Highlights

- ✅ Comparative evaluation of **CNNs, ViTs, and Siamese Networks**
- ✅ Supports both **binary** and **six-class** lesion classification
- ✅ Uses augmented and balanced skin-lesion datasets
- ✅ Includes high-performing architectures such as **ConvNeXt, ResNet50, Swin Transformer, Base ViT, and Siamese-ResNet**
- ✅ Reports standard metrics: **Accuracy, Macro-F1, ROC-AUC, confusion matrix, training/validation curves**
- ✅ Discusses clinical deployment potential for **fast, scalable, and accessible Mpox screening**
- ✅ Identifies future directions including **Edge AI deployment**, clinical metadata integration, and robustness enhancement

---

## 🧠 Research Problem

Mpox skin lesions can visually resemble other diseases such as chickenpox, measles, cowpox, and hand-foot-and-mouth disease. This makes early visual diagnosis challenging, especially where access to laboratory testing or expert dermatological review is limited.

This study asks:

> **Can modern deep learning architectures provide accurate, fast, and scalable visual screening for Mpox from skin-lesion images?**

---

<a id="models"></a>

## 🏗️ Proposed Comparative Framework

The paper evaluates three complementary model families:

| Architecture Family | Purpose | Strength |
|---|---|---|
| **CNNs** | Local lesion feature extraction | Fast, reliable, strong baseline performance |
| **Vision Transformers** | Global visual dependency modelling | Captures long-range spatial relationships |
| **Siamese Networks** | Similarity-based lesion matching | Useful for visually subtle and limited-data cases |

### Model Families Studied

#### 🔹 Convolutional Neural Networks
- ResNet50  
- ConvNeXt  
- InceptionV3  
- Xception  
- VGG19  
- Sequential CNN  

#### 🔹 Vision Transformer Models
- Base ViT  
- Swin Transformer  
- iBOT  

#### 🔹 Siamese Network
- Hybrid **Siamese-ResNet** architecture with shared-weight branches  
- Trained using image pairs to learn class similarity and dissimilarity  

---

## 🗂️ Dataset Summary

### Binary Classification Dataset

| Class | Number of Images |
|---|---:|
| Mpox | 1,530 |
| Non-Mpox | 1,890 |
| **Total** | **3,420** |

### Multi-Class Classification Dataset

| Class | Number of Images |
|---|---:|
| Mpox | 15,490 |
| Chickenpox | 3,973 |
| Measles | 2,893 |
| Cowpox | 3,550 |
| HFMD | 8,687 |
| Healthy | 6,226 |
| **Total** | **40,819** |

### Preprocessing and Augmentation

The image pipeline applies common augmentation strategies to improve generalisation:

- Rotation  
- Translation  
- Reflection / flipping  
- Shear  
- Brightness adjustment  
- Contrast adjustment  
- Hue and saturation variation  
- Scaling and zooming  

---

## 📊 Main Results

### Performance Comparison

| Model Type | Model | Binary Accuracy | Binary Macro-F1 | Multi-Class Accuracy | Multi-Class Macro-F1 |
|---|---|---:|---:|---:|---:|
| CNN | InceptionV3 | 91% | 0.91 | 89% | 0.88 |
| CNN | ResNet50 | 100% | 1.00 | 97% | 0.96 |
| CNN | Xception | 95% | 0.95 | 96% | 0.96 |
| CNN | VGG19 | 92% | 0.92 | 97% | 0.96 |
| CNN | **ConvNeXt** | **99%** | **0.99** | **99%** | **0.99** |
| CNN | Sequential CNN | 92% | 0.93 | 89% | 0.89 |
| ViT | Base ViT | 98% | 0.98 | 96% | 0.95 |
| ViT | Swin Transformer | 95% | 0.95 | 98% | 0.96 |
| ViT | iBOT | 83% | 0.84 | 84% | 0.81 |
| Siamese | **SNN** | **99%** | **0.97** | **98%** | **0.96** |

### Best Performing Models

| Category | Strongest Model(s) | Observation |
|---|---|---|
| Best CNN | **ConvNeXt** | Highly consistent across binary and multi-class tasks |
| Best binary classifier | **ResNet50 / ConvNeXt / SNN** | Near-perfect binary screening performance |
| Best transformer model | **Swin Transformer / Base ViT** | Strong global feature modelling |
| Best similarity-based model | **Siamese Neural Network** | Robust lesion similarity representation |
| Most balanced overall | **ConvNeXt** | Strong accuracy and Macro-F1 across both tasks |

---

## 🔍 Interpretability and Model Understanding

The study uses multiple analysis tools to better understand model decisions:

- Confusion matrices for binary and multi-class classification  
- Correct vs. incorrect prediction visualisation  
- Confidence-score inspection  
- Class-wise accuracy comparison  
- Training and validation accuracy/loss curves  

These analyses help identify not only **which model performs best**, but also **where and why errors occur**.

---

## 🚀 Why This Work Matters

Automated Mpox screening can support:

- Faster preliminary assessment of suspected skin lesions  
- Decision support in regions with limited PCR testing access  
- Reduced diagnostic delay during outbreaks  
- Scalable web or mobile-based screening tools  
- Future Edge AI deployment for remote or low-resource settings  

The study does **not** claim to replace clinicians. Instead, it shows how deep learning can support faster and more accessible medical image screening workflows.

---

---

## ⚙️ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mpox-detection-deep-learning.git
cd mpox-detection-deep-learning
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train a CNN Model

```bash
python src/train_cnn.py \
  --model convnext \
  --task multiclass \
  --data_dir data/multiclass \
  --epochs 30 \
  --batch_size 32
```

### 5. Train a Vision Transformer

```bash
python src/train_vit.py \
  --model swin \
  --task multiclass \
  --data_dir data/multiclass \
  --epochs 30
```

### 6. Train the Siamese Network

```bash
python src/train_siamese.py \
  --data_dir data/multiclass \
  --epochs 30 \
  --pair_strategy balanced
```

### 7. Evaluate a Saved Model

```bash
python src/evaluate.py \
  --checkpoint models/saved_checkpoints/best_model.pth \
  --task multiclass \
  --data_dir data/multiclass
```

---

## 📦 Example Requirements

```txt
python>=3.9
torch
torchvision
tensorflow
keras
scikit-learn
opencv-python
numpy
pandas
matplotlib
seaborn
tqdm
Pillow
```

---

## 📈 Expected Outputs

After training and evaluation, the repository can generate:

- Classification reports  
- Confusion matrices  
- Accuracy/loss curves  
- ROC-AUC summaries  
- Macro-F1 comparison tables  
- Correct/incorrect prediction examples  
- Saved model checkpoints  

---

## 🧪 Reproducibility Checklist

- [ ] Dataset source documented  
- [ ] Preprocessing pipeline fixed  
- [ ] Train/validation/test split saved  
- [ ] Random seed specified  
- [ ] Model checkpoints versioned  
- [ ] Evaluation scripts included  
- [ ] Confusion matrices and metrics exported  
- [ ] Hardware and software environment documented  

---

## 🧩 Limitations

This research identifies several important limitations:

- Publicly available Mpox datasets remain limited  
- Some lesion classes are visually similar, making classification difficult  
- Image-only models do not use important clinical metadata  
- Real-world deployment requires validation across skin tones, age groups, devices, lighting conditions, and geographical settings  
- Clinical testing is required before practical medical use  

---

## 🔮 Future Work

Future development can extend this work through:

- Larger and more diverse clinical datasets  
- Integration of age, skin tone, demographics, symptoms, and lesion progression metadata  
- Explainable AI methods such as Grad-CAM or attention-based lesion localisation  
- Edge AI deployment on mobile and low-resource devices  
- Federated learning for privacy-preserving medical AI  
- Web-based diagnostic assistance with clinician-in-the-loop validation  

---

## 🩺 Clinical and Ethical Note

This repository is intended for **academic and research purposes only**.  
The models described here should not be used for self-diagnosis or as a substitute for professional medical advice, laboratory testing, or clinical consultation.

Any real-world use of this system should involve:

- Clinical validation  
- Ethical approval  
- Privacy protection  
- Bias and fairness assessment  
- Human medical supervision  

---

## 👥 Authors

- **Sakib Azmain Sahil**  
- **Badhan Rani Das**  
- **Hrithik Majumdar Shibu**  
- **Aisha Hayder Chowdhury**

---

## 📚 Citation

If this work helps your research, please cite:

```bibtex
@inproceedings{sahil2025mpox_detection,
  title={Deep Learning Architectures for Real-Time Monkeypox Detection: A Comparative Study of CNNs, Transformers, and Siamese Networks},
  author={Sahil, Sakib Azmain and Das, Badhan Rani and Shibu, Hrithik Majumdar and Chowdhury, Aisha Hayder},
  booktitle={2025 28th International Conference on Computer and Information Technology (ICCIT)},
  pages={1368--1373},
  year={2025},
  publisher={IEEE},
  doi={10.1109/ICCIT68739.2025.11491487}
}
```

---

## 🌟 Repository Message

> This project demonstrates how carefully designed deep learning systems can support rapid, scalable, and accessible medical image screening.  
> By comparing CNNs, Vision Transformers, and Siamese Networks, the study provides a practical foundation for future Mpox detection systems, especially in resource-limited healthcare settings.

<div align="center">

### ⭐ If you find this work useful, consider starring the repository.

</div>

