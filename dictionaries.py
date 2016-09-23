RELATIONSHIP = [["relationship"], ["girlfriend"], ["boyfriend"], ["wife"],
                ["husband"], ["marriage"], ["divorce"], ["broke up"],
                ["my ex"], ["brokes up"], ["break up"], ["crush"],
                ["fiancé"], ["fight"], ["fought"], ["discussion"],
                ["end of a relationship"],
                ["end of my relationship"],
                ["breaking relationship"]]

WORK = [["work"], ["working"], ["boss"], ["work load"], ["job"], ["task"],
        ["project"], ["company"], ["production"], ["nightwork"], ["jobs"]]

DEATH = [["death"], ["died"], ["passed away"],
         ["loss of a family member"], ["passed out"]]

FINANCIAL = [["financial"], ["salary"], ["paycheck"]]

DISEASE = [["disease"], ["illness"], ["ill"], ["surgery"], ["tumor"],
           ["cancer"], ["hospital"], ["doctor"], ["aids"], ["hiv"], ["virus"],
           ["treatment"]]

EXAMS = [["exams"], ["exam"], ["school"], ["college"], ["course"],
         ["university"], ["test"], ["grade"], ["teacher"]]

DICTIONARIES = [RELATIONSHIP, WORK, DEATH, FINANCIAL, DISEASE, EXAMS]


def get_dictionaries():
    return DICTIONARIES
