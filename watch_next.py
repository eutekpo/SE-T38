import spacy

nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    with open("movies.txt", "r") as f:
        movie_descriptions = [line.strip() for line in f.readlines()]
    movie_titles = [line.split(":")[0] for line in movie_descriptions]
    model_description = nlp(description)
    similarities = [model_description.similarity(nlp(desc)) for desc in movie_descriptions]
    max_index = similarities.index(max(similarities))
    return movie_titles[max_index]

planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print("You should watch:", find_similar_movie(planet_hulk_description))
