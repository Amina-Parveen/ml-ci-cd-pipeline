# <div align="center">ML CI/CD Pipeline – Iris Dataset Prediction</div>

<p align="center">
  ML CI/CD pipeline for training and deploying an Iris dataset model, with automated build and deployment on Render.
</p>

---

## Project Overview
This project demonstrates a **complete Machine Learning CI/CD pipeline** using the Iris dataset. 

The workflow includes:

- **Data Loading & Preprocessing:** Reads the Iris dataset and prepares it for model training.  
- **Model Training:** Trains a RandomForestClassifier to classify iris species.  
- **Flask API:** Provides endpoints for health checks and predictions.  
- **CI/CD Deployment:** Automatically builds and deploys updates to Render whenever changes are pushed to the repository.  
- **Environment Variables:** Configurable paths (like `MODEL_PATH`) for flexibility in deployment.

The main purpose of this project is **prediction**, showcasing how a trained ML model can be integrated into a CI/CD workflow and deployed to the cloud.

---

## Project Structure
```
├── app.py            # Flask API
├── model/            # Saved model files
│   └── iris_model.pkl
|   └── train.py
|   └── evaluate.py
├── test/
|   └── test_model.py
├── data/
|    └── iris.csv      # Dataset (iris.csv)
├── requirements.txt
└── README.md
```

---

## Features
- Train a RandomForest model on the Iris dataset.  
- Flask API with endpoints:  
  - `GET /health` – Check server health.  
  - `POST /predict` – Send feature inputs to get predictions.  
- CI/CD pipeline automatically deploys updates via Render.
- Deployed on Render for live demonstration (prediction endpoint under development).

---

## Installation (Local)
1. Clone the repository:
  ``` bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the Flask app:
```
python app.py
```
4. Test endpoints locally using **Postman** or **cURL**.

---

## Usage
Health Check
```
curl http://localhost:8000/health
```
Predict
Send a JSON POST request to /predict:
```
{
  "input": [5.1, 3.5, 1.4, 0.2]
}
```
Response:
```
{
  "predictions": [0]
}
```

---

## Deployment
- Deployed on Render: [Render Deployment Link](https://ml-ci-cd-pipeline-dkje.onrender.com/)
- Auto-deploys whenever changes are pushed to the main branch.
Note: Prediction through the deployed server is under development.

---

## Tech Stack
- **Python** – Scripting and ML
- **scikit-learn** – ML algorithms
- **Flask** – API server
- **Render** – CI/CD deployment

---

## Resources
**Iris Dataset** – [Original dataset used for training](https://www.kaggle.com/datasets/uciml/iris)  
**scikit-learn Documentation** – [ML library reference](https://scikit-learn.org/stable/)  
**Flask Documentation** – [API framework reference](https://flask.palletsprojects.com/en/stable/)  
**Render Documentation** – [Deployment guide](https://render.com/docs/)  
**CI/CD Concepts** – [Understanding pipelines for ML deployment](https://towardsdatascience.com/ci-cd-for-machine-learning-mlops-pipeline-overview-35c169e41ecf/)  

---

## Future Improvements
- Enable prediction through deployed Render API.
- Add automated testing and logging for CI/CD workflow.
- Expand pipeline to support multiple datasets and models.
- Add frontend interface for easier prediction input.

---

##  Author

 **Amina Parveen**  
**Contact:** [LinkedIn](https://www.linkedin.com/in/amina-parveen-9606182a2)    
**GitHub:** [@Amina-Parveen](https://github.com/Amina-Parveen)  

---

✨ *This project is for learning and academic purposes only.*
