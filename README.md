---
sdk: docker
app_port: 7860
---

# CardioCheck — Heart Disease Prediction

**Student:** Muhammad Awais  
**Registration No.:** FA24-BSE-076  
**Section:** BSE-A  
**Course:** Machine Learning Fundamentals (AIC354)

## Project files
- `Heart_Disease_Prediction_Awais.ipynb` — notebook covering data loading, preprocessing, EDA, training, evaluation, and predictions.
- `Heart_Disease_Report_Awais.pdf` — PDF export of the notebook.
- `awais_heart_disease.csv` — named Cleveland source dataset from the UCI Heart Disease dataset.
- `awais_heart_model.pkl` — saved fitted pipeline used by the app.
- `app.py` — redesigned Streamlit interface.
- `requirements.txt` — runtime dependencies.
- `Dockerfile` — container setup for hosting without GitHub.

## Four selected model inputs
The model uses `age`, `sex`, `trestbps` (resting blood pressure), and `chol` (serum cholesterol). The target is derived from the source `num` field: `0` means disease absent, and values above `0` mean disease present.

The dataset uses source-derived observations; rows were not randomly altered to make the project look different. The project is distinct through its four selected inputs, model, notebook, student details, and app interface.

## Run locally
Use Python 3.11 or 3.12 in a virtual environment:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Keep `app.py`, `awais_heart_model.pkl`, and `requirements.txt` in the same folder.

## Deploy without GitHub using Hugging Face Spaces
1. Create/sign in to a Hugging Face account and open the Spaces section.
2. Select **Create new Space** and choose **Docker** as the SDK.
3. Create the Space, then open its **Files** area and upload `app.py`, `awais_heart_model.pkl`, `requirements.txt`, and `Dockerfile`. Keep the README's Docker Space metadata at the top.
4. Wait for the Space to build. Review build logs if it fails.
5. Open the running Space and test both prediction outcomes. Copy its public URL.
6. Replace the deployment placeholder in the first cell of the notebook with that real URL, execute the notebook again, and regenerate the PDF so the notebook and PDF both contain the actual URL.
7. Submit the notebook, dataset CSV, model file, PDF, and deployment URL as required by your instructor.

Hosting platforms can change their interfaces and limits. The actual public URL cannot be filled in until the Space is created under your account. This is an educational demonstration, not a medical diagnostic tool.
