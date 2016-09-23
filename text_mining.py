from nltk.tokenize import word_tokenize
from dictionaries import get_dictionaries

stressful_situations = ["relationship", "work", "death", "financial",
                        "disease", "exams", "other"]
individuals = ["self", "family", "other"]


def get_situations():
    return stressful_situations


def get_individuals():
    return individuals


def classify_the_stressful_situation(message):
    bag_of_words = word_tokenize(message)
    factors = []
    for val in get_dictionaries():
        factors.append(get_term_appearance_factor(
             bag_of_words, val
        ))
    situation = stressful_situations[factors.index(max(factors))]
    print(situation)
    return situation


def classify_the_most_affected_individual(message):
    # TO DO
    individual = individuals[0]
    return individual


def contains(small, big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
            else:
                return True
    return False


def get_term_appearance_factor(message, dictionary):
    factor = 0
    for val in dictionary:
        if contains(val, message):
            factor += 1
    return factor
