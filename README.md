# FinSight — AI-Powered Banking Fraud Detection Platform



![Python](https://img.shields.io/badge/Python-3.11-blue)




![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-orange)




![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-green)




![AWS](https://img.shields.io/badge/AWS-S3-yellow)




![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)



## Live Links
- **Live Fraud Detection App:** [shawaiz-finsight.streamlit.app](https://shawaiz-finsight.streamlit.app)
- **Interactive Dashboard:** [shawaiz05.github.io/FinSight-Banking-Analytics](https://shawaiz05.github.io/FinSight-Banking-Analytics)

## Project Overview
FinSight is an end-to-end AI-powered banking fraud detection platform built on 215,945 real credit card transactions. The system detects fraudulent transactions using a Random Forest classifier, stores data on PostgreSQL and AWS S3, and deploys predictions through a live Streamlit web app and interactive dashboard.

## Key Results
- ROC AUC Score: 0.9819 — industry-grade fraud detection accuracy
- Precision: 94% on fraud classification
- 215,945 transactions analysed and stored in PostgreSQL
- 401 fraud cases detected out of 215,945 (0.19% fraud rate)
- Live Streamlit app deployed and accessible publicly

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Data Cleaning | Python, Pandas, NumPy |
| Machine Learning | scikit-learn, Random Forest, SMOTE |
| Database | PostgreSQL (Supabase) |
| Cloud Storage | AWS S3 |
| Deployment | Streamlit Community Cloud |
| Dashboard | HTML, CSS, Chart.js |
| Project Management | Jira (Scrum) |
| Version Control | Git, GitHub |

## Project Structure
FinSight-Banking-Analytics/
├── app.py
├── index.html
├── FinSight_Data_Cleaning.ipynb
├── fraud_detection_model.pkl
├── finsight_queries.sql
├── confusion_matrix.png
└── feature_importance.png
## Dataset
- Source: Credit Card Fraud Detection — Kaggle (mlg-ulb)
- Size: 215,945 transactions after cleaning
- Fraud Rate: 0.19% (401 fraud cases) — matches real banking data
- Features: 28 PCA components + Amount + Class

## ML Pipeline
1. Data Cleaning — dropped nulls, scaled Amount with StandardScaler
2. Class Balancing — applied SMOTE to handle 0.19% fraud imbalance
3. Model Training — Random Forest (100 estimators, stratified split)
4. Evaluation — ROC AUC 0.9819, Precision 94%, Recall 84%

## SQL Analysis
Five PostgreSQL queries analysing:
- Total transactions and fraud count
- Average amount by fraud vs normal
- Top 10 highest fraud transactions
- Fraud distribution by amount range
- Fraud rate summary statistics

## Author
**Mohammed Shawaiz Hussain**
- Email: mdshawaiz05@gmail.com
- LinkedIn: https://www.linkedin.com/in/mohammed-shawaiz-hussain-4a12a32aa
- GitHub: https://github.com/Shawaiz05

Final-year MCA candidate | Data Analyst and ML Engineer | Open to relocation
