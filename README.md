# 🎬 Movie Recommender System  

This project is a **Movie Recommendation Web Application** built with **Streamlit**.  
It uses a **content-based filtering approach** to suggest movies similar to the one selected by the user.  
The system makes use of a pre-computed similarity matrix and a dataset of movies.  
Once a user selects a movie from the dropdown, the app displays the **top five most similar movies** along with their **posters**, which are fetched dynamically using the **TMDb API**.  

The main objective of this project is to demonstrate how machine learning models can be integrated into an interactive web application that anyone can access through a browser.  
The app is lightweight, simple to use, and visually appealing, making it a great starting point for exploring recommender systems.  

---

# web-page 

<img width="1031" height="687" alt="image" src="https://github.com/user-attachments/assets/2b7b9ab1-a0cd-4caa-909a-5a2c3a676dee" />



## ✨ Features  

The application allows users to select a movie title and instantly see a list of similar movies.  
Each recommendation is displayed with both the movie name and its official poster, which makes the results more engaging and visually informative.  
The app is powered by **Streamlit**, which makes the interface interactive and easy to use without requiring any web development background.  

---

## 🛠️ Technology Stack  

This project is primarily developed in **Python**.  
The user interface is built using **Streamlit**, while **pandas** is used to manage the dataset of movies.  
The similarity calculations are pre-computed using **scikit-learn** and stored in a pickled file for quick retrieval.  
Movie posters are fetched dynamically via the **TMDb API**, and the `requests` library is used for making API calls.  
The trained data and similarity matrix are stored as `.pkl` files to speed up recommendations.  

---

## 📂 Project Structure  

The repository is organized in a simple way to make it easy for others to understand and extend:  

# Movie-Recommender
### (Main Streamlit application)
│── app.py 

### Pickled DataFrame containing movie details
│── movies.pkl  
### Pickled similarity matrix for recommendations
│── similarity.pkl
### List of dependencies
│── requirements.txt 
### Project documentation
│── README.md 




---

# ⚙️ Installation & Setup  

## 1. Clone the repository:  
```bash
git clone https://github.com/your-username/Movie-Recommender.git
cd Movie-Recommender

## 2 create a virtual environment
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows

## 3 Install dependencies
pip install -r requirements.txt

## 4 run:
streamlit run app.py

