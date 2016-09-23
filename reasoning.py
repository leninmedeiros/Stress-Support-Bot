import text_mining

# Change it afterwards
THERE_IS_NO_STRESSFUL_SITUATION_RESPONSE = "No stressful situation."

strategies = ["general_emotional_support", "cognitive_change",
              "attentional_deployment", "situation_selection",
              "situation_modification"]


def get_strategies():
    return strategies


def process_incoming_message(message):
    if is_there_any_stressful_situation(message):
        situation = text_mining.classify_the_stressful_situation(message)
        individual = text_mining.classify_the_most_affected_individual(message)
        strategy = select_strategy(situation)
        response = construct_response(situation, individual, strategy)
    else:
        response = THERE_IS_NO_STRESSFUL_SITUATION_RESPONSE
    return response


def select_strategy(situation):
    strategy = get_strategies()[0]
    # TO DO
    return strategy


def construct_response(situation, individual, strategy):
    response = select_template(strategy)
    response = set_template_for_situation(situation, response)
    response = set_template_for_individual(situation, individual)
    return response


def select_template(strategy):
    # TO DO
    template = "template: "
    if strategy == get_strategies()[1]:
        template += get_strategies()[1]
    elif strategy == get_strategies()[2]:
        template += get_strategies()[2]
    elif strategy == get_strategies()[3]:
        template += get_strategies()[3]
    elif strategy == get_strategies()[4]:
        template += get_strategies()[4]
    else:
        template += get_strategies()[0]
    return template + " "


def set_template_for_situation(situation, response):
    # TO DO
    template = "template: "
    if situation == text_mining.get_situations()[0]:
        template += text_mining.get_situations()[0]
    elif situation == text_mining.get_situations()[1]:
        template += text_mining.get_situations()[1]
    elif situation == text_mining.get_situations()[2]:
        template += text_mining.get_situations()[2]
    elif situation == text_mining.get_situations()[3]:
        template += text_mining.get_situations()[3]
    elif situation == text_mining.get_situations()[4]:
        template += text_mining.get_situations()[4]
    elif situation == text_mining.get_situations()[5]:
        template += text_mining.get_situations()[5]
    else:
        template += text_mining.get_situations()[6]
    return template + " "


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
