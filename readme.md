
# 🎬 Movie Recommendation System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A sophisticated **Movie Recommendation System** built using Machine Learning techniques and deployed with Streamlit. This system provides intelligent movie suggestions based on content similarity, featuring an interactive web interface with movie posters fetched from The Movie Database (TMDB) API.

## 🎯 Overview

This project implements a **content-based filtering** approach using cosine similarity to recommend movies. Unlike collaborative filtering that requires user behavior data, this system analyzes movie features like genres, keywords, cast, and crew to find similar movies, making it perfect for new users (solving the cold start problem).

## ✨ Features

- **Content-Based Filtering**: Recommends movies based on movie features and attributes
- **Interactive Web Interface**: User-friendly Streamlit dashboard
- **Movie Posters**: Automatically fetches and displays movie posters from TMDB API
- **Real-time Recommendations**: Get 5 similar movies instantly
- **Similarity Scoring**: Advanced cosine similarity algorithm for accurate recommendations
- **Large Dataset**: Trained on TMDB 5000 movie dataset

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Data Processing**: NLTK, Pandas
- **API Integration**: TMDB API for movie posters
- **Model Persistence**: Pickle for saving trained models

## 📁 Project Structure

```
Movie Recommendation System/
│
├── app.py                          # Streamlit web application
├── movie-recommender-system.ipynb  # Jupyter notebook with ML pipeline
├── movie_dict.pkl                  # Preprocessed movie data (pickle file)
├── similarity.pkl                  # Cosine similarity matrix (pickle file)
├── requirement.txt                 # Python dependencies
├── tmdb_5000_credits.csv          # Movie credits dataset
├── tmdb_5000_movies.csv           # Movie details dataset
└── readme.md                      # Project documentation
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Internet connection (for TMDB API)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### Step 2: Install Dependencies
```bash
pip install -r requirement.txt
```

### Step 3: TMDB API Setup (Optional)
The app uses a TMDB API key for fetching movie posters. The current key in the code is for demonstration purposes.

To use your own API key:
1. Sign up at [TMDB](https://www.themoviedb.org/signup)
2. Go to Settings > API and request an API key
3. Replace the API key in `app.py` line 8:
```python
# Replace with your API key
api_key = "your_api_key_here"
```

## 🎯 Usage

### Method 1: Run the Streamlit App (Recommended)
```bash
streamlit run app.py
```
The app will open in your default browser at `http://localhost:8501`

### Method 2: Train the Model from Scratch
1. Open the Jupyter notebook:
```bash
jupyter notebook movie-recommender-system.ipynb
```
2. Run all cells to:
   - Load and preprocess the data
   - Create feature vectors
   - Calculate cosine similarity
   - Save the trained model

## 🎮 How to Use the App

1. **Launch the App**: Run `streamlit run app.py`
2. **Select a Movie**: Use the dropdown to search and select a movie
3. **Get Recommendations**: Click "Recommend" to get 5 similar movies
4. **View Results**: See movie titles with their posters

## 📊 Machine Learning Pipeline

### 1. Data Preprocessing
- Combines movie metadata (genres, keywords, cast, crew)
- Creates feature vectors using text processing
- Handles missing values and data cleaning

### 2. Feature Engineering
- **Text Vectorization**: Converts movie features to numerical vectors
- **Dimensionality Reduction**: Optimizes feature space
- **Normalization**: Ensures consistent feature scaling

### 3. Similarity Calculation
- **Cosine Similarity**: Measures similarity between movie vectors
- **Matrix Computation**: Creates 5000x5000 similarity matrix
- **Efficient Storage**: Saves computed similarity for fast retrieval

### 4. Recommendation Engine
- Finds most similar movies based on cosine similarity scores
- Returns top 5 recommendations excluding the selected movie
- Integrates with TMDB API for visual enhancement

## 📈 Dataset Information

This project uses the **TMDB 5000 Movie Dataset** consisting of:

### Files Included:
- **`tmdb_5000_movies.csv`**: Contains movie details
  - 4,803 movies
  - Features: budget, genres, homepage, id, keywords, original_language, overview, popularity, production_companies, release_date, revenue, runtime, spoken_languages, status, tagline, title, vote_average, vote_count

- **`tmdb_5000_credits.csv`**: Contains movie credits
  - Cast and crew information
  - Features: movie_id, title, cast, crew

### Data Processing:
- Movies with missing critical information are filtered out
- Text features are preprocessed and vectorized
- Similarity matrix is computed and stored for efficient retrieval

## 🔧 Troubleshooting

### Common Issues:

**1. ModuleNotFoundError**
```bash
# Ensure all dependencies are installed
pip install -r requirement.txt
```

**2. API Key Issues**
- Movie posters not loading? Check your internet connection
- The demo API key has rate limits; use your own TMDB API key for better performance

**3. Pickle File Errors**
```bash
# If pickle files are corrupted, retrain the model
jupyter notebook movie-recommender-system.ipynb
# Run all cells to regenerate pickle files
```

**4. Streamlit Issues**
```bash
# Clear Streamlit cache
streamlit cache clear
```

## 🚀 Future Enhancements

- [ ] Add user rating system
- [ ] Implement hybrid recommendation (collaborative + content-based)
- [ ] Add movie reviews sentiment analysis
- [ ] Deploy to cloud platform (Heroku/AWS)
- [ ] Add user authentication and personal watchlists
- [ ] Implement real-time trending movies
- [ ] Add movie trailer integration
- [ ] Multi-language support

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Commit your changes**: `git commit -m 'Add some feature'`
4. **Push to the branch**: `git push origin feature/your-feature-name`
5. **Open a Pull Request**

### Contribution Guidelines:
- Follow PEP 8 Python style guide
- Add comments to your code
- Update documentation if needed
- Test your changes before submitting

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [The Movie Database (TMDB)](https://www.themoviedb.org/) for providing the API and dataset
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools
- The open-source community for various Python libraries used

## 📞 Contact

If you have any questions, feel free to reach out:

- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

---

⭐ **If you found this project helpful, please give it a star!** ⭐

