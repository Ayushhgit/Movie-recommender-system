# Movie Recommendation System

This project is a Movie Recommender System built using machine learning techniques. The system recommends movies based on the user's input by calculating the similarity between movies using a pre-trained similarity matrix.

## Features

- **Movie Recommendation**: Recommends similar movies based on a selected movie.
- **User Interface**: The app provides a simple, interactive user interface built using **Streamlit**.
- **Local Dataset**: Uses a local dataset for movie data, including movie titles, movie IDs, and pre-computed similarity scores.

## Technologies Used

- **Python**: The backend is written in Python.
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation.
- **Numpy**: For numerical computations.
- **Pickle**: For saving and loading pre-trained movie data and similarity matrix.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ayushhgit/Movie-recommender-system.git
pip install -r requirements.txt

pip install streamlit pandas numpy

cd Movie-recommender-system/Movie-recommendation-system

streamlit run app.py

Movie-recommender-system/
│
├── Movie-recommendation-system/
│   ├── app.py                # Main Streamlit app.
│   ├── movie.pkl             # Pickle file containing the movie dataset.
│   ├── similarity.pkl        # Pickle file containing the similarity matrix.
│   ├── requirements.txt      # List of Python packages.
│   └── README.md             # Project documentation.
│
└── .gitignore                # Git ignore file to exclude unwanted files.
