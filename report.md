# SDG 3 — Pneumonia Detection from Chest X-rays

Problem addressed

Pneumonia is a leading cause of mortality, particularly in children and older adults. Timely detection from chest X-rays can help prioritize care and improve outcomes. This project builds a model to assist clinicians by flagging X-rays likely to show pneumonia.

ML approach

Supervised learning using a Convolutional Neural Network (CNN). The model is trained on labeled chest X-ray images (PNEUMONIA vs NORMAL). The notebook demonstrates preprocessing with Keras ImageDataGenerator, a compact CNN architecture, training for a few epochs, and evaluation with accuracy, confusion matrix, and classification report.

Results

This demo uses a small training run (5 epochs) intended for quick experimentation. Expected outcomes: reasonable accuracy on the test set for demonstration, but not production-grade. For improved performance, apply transfer learning (EfficientNet), class balancing, and longer training.

Ethical considerations

- Data bias: public datasets may over-represent certain age groups, demographics, or types of imaging equipment. Models trained on biased data may underperform on underrepresented populations.
- Clinical risk: false negatives could delay treatment. The model should be used as a decision-support tool, not a replacement for clinical judgment.
- Privacy: X-rays are medical data — ensure de-identification and follow local regulations.

Deliverables

- `pneumonia_detection_notebook.ipynb`: Notebook with code and notes.
- `README.md` and `requirements.txt` for setup.
