# Pneumonia Detection from Chest X-rays

Overview

This project demonstrates a supervised learning pipeline (CNN) to detect pneumonia from chest X-ray images. It's built for SDG 3 (Good Health and Well-being).

Contents

- `pneumonia_detection_notebook.ipynb`: Jupyter notebook with the end-to-end workflow.
- `requirements.txt`: Python dependencies.

Setup

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv venv; .\venv\Scripts\Activate.ps1
```

2.Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3.Dataset: Download the 'Chest X-Ray Images (Pneumonia)' dataset. Options:

- Kaggle: `paultimothymooney/chest-xray-pneumonia` (requires Kaggle API and `kaggle.json`).
- Public mirror: search for 'chest_xray' dataset and extract into the project root so the notebook finds `chest_xray/train`, `chest_xray/val`, `chest_xray/test`.

Usage

- Open `pneumonia_detection_notebook.ipynb` in Jupyter and run cells sequentially. The notebook contains guidance on training and stretch goals.

Notes

- The notebook is intentionally small for demo purposes. For production, use transfer learning, larger image sizes, class weighting, and more epochs.
