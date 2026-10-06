# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

    For this design, each song is categorized on the features of genre and mood, human readable tags, and numerical audio metrics, scaled from 0 to 1, such as: energy, valence, danceability, acousticness, and tempo_bmp. 

    The UserProfile stores the listener's preferred audio targets, for example a preferred energy of 0.8, a valence of 0.75, and a tempo_bpm of 120. Also, it stores the listener's favorite categories, like a favorite genre of pop and mood of happy. 

    The Recommender computes the score for each song individually by evaluating it agianst the user's personal profile. For numerical features, it uses a distance formula: 1 - |x - y|, where x is the number for the numerical feature of the song and y is the number for the numerical feature of the user's preferrence. It rewards song close to the user's preferrence and penalizes those far away from it. Also, it checks wether or not the song matchs the favorite mood and/or genre of the lsietner and give bonus points if it match one or both. Both of these computations are combined to give the individual song a score that is between 0 - 1.

    Choosing which songs to recommend is done by taking all of the scored songs and sorting, filtering, and applying rules regarding diversity and flow to them. This ensures that songs are ranked on how likely it is for the listener to like them, song that are consistently skipped are removed, and that there is variety in the songs suggested. 

    Algorithm Recipe: 
      1. Inputs: 
          ~ UserProfile - target preferences and numerical audio targets
          ~ Dataset - library of songs with metadata
      
      2. Scoring Loop:
          ~ Numerical Audio Feature Distance - 50% weight, 
          1 - |x - y|
          ~ Categorical Bonus Points - 50% weight, genre match = +2.5, mood match = +1.5 points, total points are normalized (4 pts max) to a 0 to 1 scale.
          ~ Final Aggregated Score - combining both components, Final Score = 0.5 * (Average Audio Distance)
      
      3. Ranking Filtering, and Output:
          ~ Removing songs that are consistently skipped or don't meet basline threshold rules, rank remaining scored songs based on final score, apply rules to ensure variety, and return the top recommendations to listener. 



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Starter Preferrences:
```
Loading songs from data/songs.csv...
Successfully loaded 18 songs.
==================================================
🎵 TOP RECOMMENDATIONS FOR YOU 🎵
==================================================

1. Sunrise City by Neon Echo
   Score: 4.96 / 10.0
   Genre: Pop | Mood: Happy
   --- Match Breakdown ---
    • genre match (pop) (+2.0)
    • mood match (happy) (+1.0)
    • energy similarity (target: 0.8
    • song: 0.82) (+1.96)

2. Gym Hero by Max Pulse
   Score: 3.74 / 10.0
   Genre: Pop | Mood: Intense
   --- Match Breakdown ---
    • genre match (pop) (+2.0)
    • energy similarity (target: 0.8
    • song: 0.93) (+1.74)

3. Rooftop Lights by Indigo Parade
   Score: 2.92 / 10.0
   Genre: Indie Pop | Mood: Happy
   --- Match Breakdown ---
    • mood match (happy) (+1.0)
    • energy similarity (target: 0.8
    • song: 0.76) (+1.92)

4. Velvet Groove by Funk Masters
   Score: 2.00 / 10.0
   Genre: Funk | Mood: Groovy
   --- Match Breakdown ---
    • energy similarity (target: 0.8
    • song: 0.8) (+2.00)

5. Vivaldi Storm by Baroque Ensemble
   Score: 1.90 / 10.0
   Genre: Classical | Mood: Dramatic
   --- Match Breakdown ---
    • energy similarity (target: 0.8
    • song: 0.85) (+1.90)

==================================================
```

Oxymoron Preferrences:
```
Loading songs from data/songs.csv...
Successfully loaded 18 songs.
==================================================
🎵 TOP RECOMMENDATIONS FOR YOU 🎵
==================================================

1. Hollow Crown by Iron Citadel
   Score: 5.90 / 10.0
   Genre: Metal | Mood: Aggressive
   --- Match Breakdown ---
    • genre match (metal) (+2.0)
    • energy similarity (target: 0.95
    • song: 0.98) (+1.94)
    • valence similarity (target: 0.2
    • song: 0.22) (+1.96)

2. Midnight Velvet by Blue Note Trio
   Score: 3.58 / 10.0
   Genre: Blues | Mood: Melancholic
   --- Match Breakdown ---
    • mood match (melancholic) (+1.0)
    • energy similarity (target: 0.95
    • song: 0.32) (+0.74)
    • valence similarity (target: 0.2
    • song: 0.28) (+1.84)

3. Vivaldi Storm by Baroque Ensemble
   Score: 3.50 / 10.0
   Genre: Classical | Mood: Dramatic
   --- Match Breakdown ---
    • energy similarity (target: 0.95
    • song: 0.85) (+1.80)
    • valence similarity (target: 0.2
    • song: 0.35) (+1.70)

4. Cyber Horizon by Neon Runner
   Score: 3.42 / 10.0
   Genre: Cyberpunk | Mood: Gritty
   --- Match Breakdown ---
    • energy similarity (target: 0.95
    • song: 0.88) (+1.86)
    • valence similarity (target: 0.2
    • song: 0.42) (+1.56)

5. Storm Runner by Voltline
   Score: 3.36 / 10.0
   Genre: Rock | Mood: Intense
   --- Match Breakdown ---
    • energy similarity (target: 0.95
    • song: 0.91) (+1.92)
    • valence similarity (target: 0.2
    • song: 0.48) (+1.44)

==================================================
```

Mismatch Preferrences:
```
Loading songs from data/songs.csv...
Successfully loaded 18 songs.
==================================================
🎵 TOP RECOMMENDATIONS FOR YOU 🎵
==================================================

1. Vivaldi Storm by Baroque Ensemble
   Score: 4.90 / 10.0
   Genre: Classical | Mood: Dramatic
   --- Match Breakdown ---
    • genre match (classical) (+2.0)
    • energy similarity (target: 0.95
    • song: 0.85) (+1.80)
    • danceability similarity (target: 0.9
    • song: 0.45) (+1.10)

2. Sunrise City by Neon Echo
   Score: 4.52 / 10.0
   Genre: Pop | Mood: Happy
   --- Match Breakdown ---
    • mood match (happy) (+1.0)
    • energy similarity (target: 0.95
    • song: 0.82) (+1.74)
    • danceability similarity (target: 0.9
    • song: 0.79) (+1.78)

3. Rooftop Lights by Indigo Parade
   Score: 4.46 / 10.0
   Genre: Indie Pop | Mood: Happy
   --- Match Breakdown ---
    • mood match (happy) (+1.0)
    • energy similarity (target: 0.95
    • song: 0.76) (+1.62)
    • danceability similarity (target: 0.9
    • song: 0.82) (+1.84)

4. Electric Pulse by Vortex Club
   Score: 3.98 / 10.0
   Genre: House | Mood: Euphoric
   --- Match Breakdown ---
    • energy similarity (target: 0.95
    • song: 0.95) (+2.00)
    • danceability similarity (target: 0.9
    • song: 0.91) (+1.98)

5. Gym Hero by Max Pulse
   Score: 3.92 / 10.0
   Genre: Pop | Mood: Intense
   --- Match Breakdown ---
    • energy similarity (target: 0.95
    • song: 0.93) (+1.96)
    • danceability similarity (target: 0.9
    • song: 0.88) (+1.96)

==================================================
```

Boundary Preferrences:
```
Loading songs from data/songs.csv...
Successfully loaded 18 songs.
==================================================
🎵 TOP RECOMMENDATIONS FOR YOU 🎵
==================================================

1. Starlight Reverie by Astral Projection
   Score: 5.96 / 10.0
   Genre: Ambient | Mood: Dreamy
   --- Match Breakdown ---
    • energy similarity (target: 0.0
    • song: 0.2) (+1.60)
    • valence similarity (target: 0.0
    • song: 0.5) (+1.00)
    • danceability similarity (target: 0.0
    • song: 0.3) (+1.40)
    • acousticness similarity (target: 1.0
    • song: 0.98) (+1.96)

2. Midnight Velvet by Blue Note Trio
   Score: 5.50 / 10.0
   Genre: Blues | Mood: Melancholic
   --- Match Breakdown ---
    • energy similarity (target: 0.0
    • song: 0.32) (+1.36)
    • valence similarity (target: 0.0
    • song: 0.28) (+1.44)
    • danceability similarity (target: 0.0
    • song: 0.5) (+1.00)
    • acousticness similarity (target: 1.0
    • song: 0.85) (+1.70)

3. Spacewalk Thoughts by Orbit Bloom
   Score: 5.16 / 10.0
   Genre: Ambient | Mood: Chill
   --- Match Breakdown ---
    • energy similarity (target: 0.0
    • song: 0.28) (+1.44)
    • valence similarity (target: 0.0
    • song: 0.65) (+0.70)
    • danceability similarity (target: 0.0
    • song: 0.41) (+1.18)
    • acousticness similarity (target: 1.0
    • song: 0.92) (+1.84)

4. Library Rain by Paper Lanterns
   Score: 4.66 / 10.0
   Genre: Lofi | Mood: Chill
   --- Match Breakdown ---
    • energy similarity (target: 0.0
    • song: 0.35) (+1.30)
    • valence similarity (target: 0.0
    • song: 0.6) (+0.80)
    • danceability similarity (target: 0.0
    • song: 0.58) (+0.84)
    • acousticness similarity (target: 1.0
    • song: 0.86) (+1.72)

5. Vivaldi Storm by Baroque Ensemble
   Score: 4.60 / 10.0
   Genre: Classical | Mood: Dramatic
   --- Match Breakdown ---
    • energy similarity (target: 0.0
    • song: 0.85) (+0.30)
    • valence similarity (target: 0.0
    • song: 0.35) (+1.30)
    • danceability similarity (target: 0.0
    • song: 0.45) (+1.10)
    • acousticness similarity (target: 1.0
    • song: 0.95) (+1.90)

==================================================

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



