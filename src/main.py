"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    '''
    # Starter example profile
    user_prefs = {
        "genre": "metal", 
        "mood": "melancholic", 
        "energy": 0.95, 
        "valence": 0.2
    }

    
    user_prefs = {
        "genre": "classical", 
        "mood": "happy", 
        "energy": 0.95, 
        "danceability": 0.90
    }
    '''
    user_prefs = {
        "genre": "unknown_genre", 
        "mood": "unknown_mood", 
        "energy": 0.0, 
        "acousticness": 1.0, 
        "danceability": 0.0, 
        "valence": 0.0
    }
    
    
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("=" * 50)
    print("🎵 TOP RECOMMENDATIONS FOR YOU 🎵")
    print("=" * 50)
    
    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        
        # Header for each recommendation
        print(f"\n{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f} / 10.0")
        print(f"   Genre: {song['genre'].title()} | Mood: {song['mood'].title()}")
        print("   --- Match Breakdown ---")
        
        # Split the reasons string back into bullet points for clean readability
        reasons_list = explanation.split(", ")
        for reason in reasons_list:
            print(f"    • {reason}")
            
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
