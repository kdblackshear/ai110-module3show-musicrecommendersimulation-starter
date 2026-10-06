from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    songs = []

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"])
            }
            songs.append(song)
            
    print(f"Successfully loaded {len(songs)} songs.")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    score = 0.0
    reasons = []

    # 1. Categorical Match: Genre (+2.0 points)
    if "genre" in user_prefs and song.get("genre", "").lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append(f"genre match ({song['genre']}) (+2.0)")

    # 2. Categorical Match: Mood (+1.0 point)
    if "mood" in user_prefs and song.get("mood", "").lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append(f"mood match ({song['mood']}) (+1.0)")

    # 3. Numerical Audio Features (e.g., energy, valence, etc.)
    # Uses the distance formula: 1 - |x - y| and scales it into points
    numerical_features = ["energy", "valence", "danceability", "acousticness", "tempo_bpm"]
    
    for feature in numerical_features:
        if feature in user_prefs:
            x = song.get(feature, 0.0)
            y = user_prefs[feature]
            
            # Distance formula calculation (bounded between 0 and 1)
            similarity = 1.0 - abs(x - y)
            similarity = max(0.0, min(1.0, similarity))
            
            # Weight numerical feature contribution (e.g., max 2.0 points)
            feature_points = similarity * 2.0
            score += feature_points
            
            reasons.append(f"{feature} similarity (target: {y}, song: {x}) (+{feature_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored_songs = []
    
    # 1. The Scoring Loop: Judge every song in the catalog
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        # Create a clean, human-readable explanation string from the reasons list
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))
        
    # 2. Sorting: Rank songs from highest to lowest score using Python's built-in sorted()
    # We sort by the score element (index 1 of our tuple) in descending order (reverse=True)
    sorted_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    
    # 3. Slice to return the top k results
    return sorted_songs[:k]
