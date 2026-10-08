# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

        Name: PulseScore
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

        This recommender generates songs based on the features of genre and mood, human readable tags, and numerical audio metrics, scaled from 0 to 1, such as: energy, valence, danceability, acousticness, and tempo_bmp. It makes assumptions about the user's prefernces in each of these categories based off of their past listening history. This is for classroom experience, so user preferences are manually entered instead of taken fro real data. 
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

    The UserProfile stores the listener's preferred audio targets, for example a preferred energy of 0.8, a valence of 0.75, and a tempo_bpm of 120. Also, it stores the listener's favorite categories, like a favorite genre of pop and mood of happy. 

    The Recommender computes the score for each song individually by evaluating it agianst the user's personal profile. For numerical features, it uses a distance formula: 1 - |x - y|, where x is the number for the numerical feature of the song and y is the number for the numerical feature of the user's preferrence. It rewards song close to the user's preferrence and penalizes those far away from it. Also, it checks wether or not the song matchs the favorite mood and/or genre of the lsietner and give bonus points if it match one or both. Both of these computations are combined to give the individual song a score that is between 0 - 1.

    Choosing which songs to recommend is done by taking all of the scored songs and sorting, filtering, and applying rules regarding diversity and flow to them. This ensures that songs are ranked on how likely it is for the listener to like them, song that are consistently skipped are removed, and that there is variety in the songs suggested. 
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

        There are 18 songs in the catalog, all which have varying genre and mood, human readable tags, and numerical audio metrics, scaled from 0 to 1. Originally, there were only 10 songs in the catalog, but 8 were added during the development of the program. Although there was an attmept to make the acatalog of songs as representative as possible, I'm sure there are parts of musical tastes missing or underepresented.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

        The program does a good job at handling the edge cases and stark differences in the preferences, which is something I specifically tested for. There were cases in which the recommendations matched my intuition, like in the test for a Mismatched profile, the program favors categorical bias over the mathematical alignment of the formula used.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

        There is a flaw in my tempo_bpm scale where there is an accidental hard filer. The numerical similarity fourmula that my program uses (1 - |x - y|) works only for features normalized between 0.0 and 1.0, but it breaks down for tempo_bpm because it ranges from around 60 to 160. Due to this, if the listener has a target tempo of 118 and the song in question has a tempo of 120, the formula used would be 1 - |120 - 118| = -1, which is normalized to 0.0. This means that any song that deviates by even 1 bpm is heavily penalized, unfairly punishing the song. 
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

        I tested an Oxymoron profile (which had a high energy target and a melancholic mood), a Mismatch profile (which had a high energy and acoustic target, but a low danceability, and a dramatic mood), and a Bourndary profile (which used missing or extreme values for targets across all preferences). When running these tests, I looked for how the program handled the edge cases and stark differences in the preferences. I wanted the program to be able to suggest songs and not uphold something like a strict mood tag. Something that suprised me about the reults from the Mismatch profile was that there is a tradeoff present in the recommender where the engine will favor categorical bias over the mathematical alignment of the formula used. I tested each of these profiles manually by exchanging them for one another under user_prefs in main().
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

        In the furture, this program can be improved in the area of diversity among top results by adding a plethora of songs to the catalog so that most or all differing music tastes are represnted and availiable for more user profiles. Also, the program can handle more complex user tastes in the future by gathering real data from a large population's user preferences and using that to further imporve the program's generating capabilities.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

        The biggest learning moment I had during this project was during the testing phase. When I tested the different user preferences against my program, it revealed a lot about how flexible my current code was and, as stated, before surprised me by exposing that in certain cases the program will favor categorical bias over the mathematical alignment of the formula used. 

        I used Gemini AI to aid me in generating extar songs to add to the catalog and completing code snippets. Double-checking these suggestions was needed everytime I planned to use what was generated. This was mainly manually, by looking through the songs and ther categorical values to make sure evrything was sound, and also testing the code it gave me in the terminal. 

        I was surpised that such a simple formula (1 - |x - y|) can mirror human taste in a pretty sound way. Also, that the prefereces within each category can be numerically evaluated.

        If I extnded this program, I would, as stated before, improve the area of diversity among top results by adding a plethora of songs to the catalog and make sure the program can handle more complex user tastes in the future by gathering real data from a large population's user preferences. Also, the UI component of this program and making it appealing to the eye. 