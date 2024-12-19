
# Movie Recommendation System

This project is a Movie Recommendation System built using Machine Learning techniques. The system aims to suggest movies to users based on their preferences and viewing history.

## Features

- **User-based Collaborative Filtering**: Recommends movies based on the preferences of similar users.
- **Item-based Collaborative Filtering**: Recommends movies similar to those the user has liked in the past.
- **Content-based Filtering**: Recommends movies based on the content and attributes of the movies.
- **Hybrid Filtering**: Combines multiple recommendation strategies to improve accuracy.

## Machine Learning Algorithms Used

- **K-Nearest Neighbors (KNN)**: Used for user-based and item-based collaborative filtering.
- **Matrix Factorization (SVD)**: Used for collaborative filtering to decompose the user-item interaction matrix.
- **Cosine Similarity**: Used for measuring similarity between items or users in collaborative filtering.
- **TF-IDF Vectorization**: Used for content-based filtering to analyze movie descriptions and attributes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-recommendation-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd movie-recommendation-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare the dataset:
    - Ensure you have a dataset of movies and user ratings.

2. Train the model:
    - Open the Jupyter notebook `movie-recommender-system.ipynb` and run all cells to train the recommendation model.

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Dataset

The dataset should contain information about movies and user ratings.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

