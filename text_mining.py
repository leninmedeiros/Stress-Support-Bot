
from dictionaries import get_dictionaries

stressful_situations = ["relationship", "work", "death", "financial",
                        "health", "educational", "other"]
individuals = ["self", "family", "other"]


def get_situations():
    return stressful_situations


def get_individuals():
    return individuals


def classify_the_stressful_situation(message):
    factors = []
    for val in get_dictionaries():
        factors.append(get_term_appearance_factor(
             message, val
        ))
    situation = stressful_situations[factors.index(max(factors))]
    return situation


def classify_the_most_affected_individual(message):
    # TO DO
    individual = individuals[0]
    return individual


def get_term_appearance_factor(message, dictionary):
    factor = 0
    for val in dictionary:
        if val in message.lower():
            factor += 1
    return factor
