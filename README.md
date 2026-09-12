# Fraud Detection App

A simple Streamlit app that predicts whether a transaction looks fraudulent, based on a model I trained on transaction data.

**Live app:** [link once deployed]

## What it does

You enter transaction details, and the app runs them through a trained ML pipeline to flag whether it looks like fraud or not. Nothing fancy — just a quick, usable interface around the model.

## Running it yourself

## Dataset

```bash
git clone <https://github.com/TheStereo-code/Fraud_prediction.git>
cd Fraud_detection
python -m venv venv
venv\Scripts\activate        # (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
streamlit run main/fraud_detection.py
```
This project uses the [AIML Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download&select=AIML+Dataset.csv) for training. 
Download it and place it inside the `main/` folder as `AIML_Dataset.csv` before running `analysis.ipynb`.

## About the model

I trained this on `AIML_Dataset.csv` (not included here — it's too large/sensitive to commit). The model itself is saved as `fraud_detection_pipeline.pkl` and loaded straight into the app.

If you want to know exactly how it was built — feature choices, comparisons, etc. — check `main/analysis.ipynb`.

## Notes

Still a work in progress. Next things I want to add: better input validation, maybe some explainability around predictions, and a cleaner UI.
