# Enhancing Bitcoin Price Prediction with Deep Learning: Integrating Social Media Sentiment and Historical Data 
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/iamhlasoe/btc-price-prediction)
![GitHub repo size](https://img.shields.io/github/repo-size/iamhlasoe/btc-price-prediction)
![Paper Published](https://img.shields.io/badge/Published-Yes-brightgreen)

## 📄 Overview

This repository contains the code and resources for my Master's degree machine learning project, **"Enhancing Bitcoin Price Prediction with Deep Learning: Integrating Social Media Sentiment and Historical Data"**, which has been **published in MDPI Applied Sciences Journal, 2025**.  
The study addresses the challenge of Bitcoin's extreme volatility by combining **historical price data** with **social media sentiment and tweet volume data** in a **multivariate deep learning framework**.

## 📰 Publication
- **Title:** Enhancing Bitcoin Price Prediction with Deep Learning: Integrating Social Media Sentiment and Historical Data
- **Journal:** MDPI Applied Sciences 
- **DOI / Link:** https://doi.org/10.3390/app15031554  

## 🎯 Objectives
- Enhance Bitcoin price prediction accuracy by integrating **Twitter sentiment analysis** with historical market data.  
- Compare univariate and multivariate LSTM-based models.  
- Demonstrate the value of incorporating sentiment in decision-making for cryptocurrency investments.  

## 🛠️ Technologies & Tools
- **Language:** Python 3.x  
- **Libraries:** NumPy, Pandas, Scikit-learn, TensorFlow/PyTorch, Matplotlib, etc.  
- **Platform:** Google Colab  
- **Other Tools:** Jupyter Notebook, Git  

## 📊 Dataset
- **Source:** Exploreai; Data and Sons. Bitcoin Tweets and Price Dataset. Available online: https://www.dataandsons.com/categories/markets/bitcoin-tweets-dataset-2017-to-2019
- **Data Collected:**  Bitcoin OHLCV data, sentiment scores, and tweet volumes.   
- **Preprocessing:** Data cleaning, normalization, and time series alignment.  

## 📈 Results

Among the five LSTM-based models developed:
-Multi-LSTM-Sentiment achieved the best performance:
--MAE: 0.00196
--RMSE: 0.00304
-Results demonstrate the importance of social media sentiment in enhancing cryptocurrency forecasting models.

## 🏆 Key Contributions

-Introduced a multivariate LSTM framework that integrates Twitter sentiment and volume data with historical prices.
-Demonstrated significant improvement over a univariate LSTM baseline.
-Provided an open-source pipeline for cryptocurrency sentiment analysis and price prediction.



## 📂 Repository Structure
```plaintext
.
├── data/                # Sample dataset or data description
├── models/              # Trained Models 
├── notebooks/           # Jupyter notebooks for experiments
├── scripts/             # Source code
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
