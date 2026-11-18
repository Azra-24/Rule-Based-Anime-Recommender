# Rule-Based Anime Recommendation System

A Python-based, rule-driven anime recommendation system that suggests anime based on user preferences such as genre and episode length. It uses predefined recommendation rules and interactive inputs to help both beginners and experienced anime viewers discover anime they might enjoy.

## Features

- **Personalized Recommendations:** Suggests anime based on user preferences.
- **11 Anime Genres:** Choose from Shonen, Fantasy, Action, Comedy, Adventure, Super Power, Martial Arts, Psychological, Police/Detective, Thriller, and Supernatural.
- **Duration Selection:** Choose between short and long anime.
- **Anime Information:** Displays additional details, including subgenres and synopses.
- **Beginner-Friendly:** Provides a brief introduction for users who are new to anime.
- **Interactive CLI:** Offers a simple, user-friendly command-line experience.

## Tech Stack

- **Python** – Core programming language.
- **Random** – Selects anime recommendations from predefined lists.
- **Time** – Adds pauses between printed messages.
- **Termcolor** – Adds colored text to the terminal interface.

## Project Structure

```text
Rule-Based-Anime-Recommender/
│
├── anime_recommender.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Rule-Based-Anime-Recommender
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python anime_recommender.py
```

## How It Works

1. The user enters their name and starts the recommendation process.
2. The system asks whether the user is new to anime and provides a brief introduction if needed.
3. The user selects a preferred anime genre from the available options.
4. The user chooses between short and long anime.
5. Based on the selected preferences, predefined rules filter the available recommendations.
6. The system randomly selects an anime from the matching options and displays its details and synopsis.

## Recommendation Approach

This project follows a **rule-based recommendation approach**. It uses predefined genre and duration categories to determine suitable anime recommendations. The Python `random` module is used to select a recommendation from the matching options.

It does not use machine learning or artificial intelligence models.

## Future Improvements

- Provide multiple anime recommendations at once.
- Add a watchlist feature.
- Include anime ratings and release information.
- Introduce mood-based recommendations.
- Add an anime search feature.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
