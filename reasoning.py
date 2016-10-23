import text_mining
import numpy
import templates

# Change it afterwards
THERE_IS_NO_STRESSFUL_SITUATION_RESPONSE = "No stressful situation."

strategies = ["general_emotional_support", "cognitive_change",
              "attentional_deployment", "situation_selection",
              "situation_modification"]

# Based on the first survey made via CrowdFlower:
ABSOLUTE_RESULTS = [
    [8, 6, 5, 4, 5, 28],
    [3, 8, 3, 0, 4, 18],
    [8, 4, 0, 0, 3, 15],
    [2, 2, 0, 0, 1, 5],
    [1, 5, 2, 0, 1, 9],
    [0, 1, 0, 0, 3, 4],
    [5, 2, 0, 1, 1, 9]
    ]

PROBABILITIES = [[0.2857, 0.2143, 0.1786, 0.1428, 0.1786],
                 [0.1667, 0.4444, 0.1667, 0, 0.2222],
                 [0.5333, 0.2667, 0, 0, 0.2],
                 [0.4, 0.4, 0, 0, 0.2],
                 [0.1111, 0.5556, 0.2222, 0, 0.1111],
                 [0, 0.25, 0, 0, 0.75],
                 [0.5556, 0.2222, 0, 0.1111, 0.1111]]


def get_probabilities():
    return PROBABILITIES


def get_strategies():
    return strategies


def process_incoming_message(message, user):
    if is_there_any_stressful_situation(message):
        situation = text_mining.classify_the_stressful_situation(message)
        # To perform the below afterwards:
        # individual = text_mining.classify_the_most_affected_individual(
        #     message
        # )
        strategy = select_strategy(situation)
        # To use like the below afterwards:
        # response = construct_response(situation, user, individual, strategy)
        response = construct_response(situation, user, strategy)
        print("The identified situation concerns to: "+situation)
        print("The selected strategy is: "+strategy)
    else:
        response = THERE_IS_NO_STRESSFUL_SITUATION_RESPONSE
    return {'situation': situation, 'strategy': strategy, 'response': response}


def select_strategy(situation):
    index_s = text_mining.stressful_situations.index(situation)
    prob = PROBABILITIES[index_s]

    # Bots 1 & 2: with probabilities.
    sel_index = numpy.random.choice(5, 1, p=prob)
    # Bots 3 & 4: without probabilities (completely random choice).
    # sel_index = numpy.random.choice(5, 1)

    strategy = strategies[sel_index]
    return strategy


# To put individual as a parameter as well afterwards.
def construct_response(situation, user, strategy):
    response = select_template(strategy)
    response = set_template_for_situation(situation, response)
    # To use something similar to the below afterwards:
    # response = set_template_for_individual(situation, individual)
    personalised_response = response.replace("<user>", user)
    return personalised_response


def select_template(strategy):
    index = get_strategies().index(strategy)
    return templates.get_templates()[index]


def set_template_for_situation(situation, response):
    # Bots 1 & 3: telling the name of the situation
    # Bots 2 & 4: without telling the name of the situation

    # This if-else is useless for Bots 2 & 4. Use the below instead:
    # templates = response[0]
    if situation == "loss":
        templates = response[1]
    else:
        templates = response[0]

    a = numpy.arange(len(templates))
    index = numpy.random.choice(a, 1)
    raw_response = templates[index]
    # This if-else is useless for Bots 2 & 4. Use the below instead:
    # response = raw_response.replace("<situation>", "")
    if situation == "other":
        response = raw_response.replace("<situation>", "")
    else:
        response = raw_response.replace("<situation>", situation + " ")

    return response


def set_template_for_individual(individual, response):
    # TO DO
    template = "template: "
    if individual == text_mining.get_individuals()[1]:
        template += text_mining.get_individuals()[1]
    elif individual == text_mining.get_individuals()[2]:
        template += text_mining.get_individuals()[2]
    else:
        template += text_mining.get_individuals()[0]
    return template + " "


def is_there_any_stressful_situation(message):
    # TO DO
    message_contains_a_stressful_situation = True
    return message_contains_a_stressful_situation
