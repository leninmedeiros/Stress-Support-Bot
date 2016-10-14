RELATIONSHIP = ["relationship", "girlfriend", "boyfriend", "wife",
                "husband", "marriage", "divorce", "broke up",
                "my ex", "brokes up", "break up", "crush",
                "fiancé", "broke my heart", "romance", "state",
                "anaclisis", "love affair", "affair", "sexual relationship",
                "human relationship", "partnership", "relation", "marital",
                "married", "hubby", "better half", "benedict", "spouse",
                "househusband", "benedick", "uxoricide", "viscountess",
                "missus", "sheikha", "matron", "wedding", "marry",
                "lady of the house", "marchioness", "housewife", "housewifery",
                "old lady", "uxor", "battle-ax", "vicereine", "woman", "missis",
                "ux.", "widow", "widower", "homemaker", "first lady", "mayoness",
                "signora", "battle-axe", "crown princess", "sheika", "love",
                "lover", "beau", "swain", "spousal", "wedlock", "matrimony",
                "nuptials", "honeymoon"]

WORK = ["work", "working", "boss", "work load", "job", "task",
        "project", "company", "production", "nightwork", "jobs", "duty",
        "mission", "wash", "substituting", "ironing", "operation", "labour",
        "shining", "tending", "social service", "heavy lifting", "service",
        "loose end", "labor", "polishing", "housework", "investigation",
        "timework", "make-work", "lavation", "welfare work", "paperwork",
        "toil", "attention", "spadework", "unfinished business", "action",
        "investigating", "washing", "subbing", "care", "missionary work",
        "logging", "housekeeping", "housewifery", "undertaking", "coursework",
        "activity", "busywork", "aid", "procedure", "old man", "employer",
        "hirer", "guvnor", "foreman", "gaffer", "supervisor", "baas",
        "assistant foreman", "chief", "honcho", "ganger", "straw boss", "leader",
        "executive", "administrator", "general manager", "manager", "colleague",
        "employee", "fired", "hired", "hiring", "firing", "deadline", "business"]

DEATH = ["death", "died", "passed away", "loss", "passed out", "decease",
         "expiry", "passing away", "passing out", "dying"]

FINANCIAL = ["financial", "salary", "paycheck", "money", "debt", "debts",
             "business", "fiscal", "monetary", "fund", "currency", "cash",
             "pound", "pounds", "dollar", "dollars", "bank", "investment",
             "investments", "bill", "bills", "euro", "euros", "$", "€", "£",
             "wealth", "bundle", "pile", "sterling", "currency", "atm", "account",
             "insurance", "price", "rent"]

HEALTH = ["disease", "illness", "ill", "surgery", "tumor",
           "cancer", "hospital", "doctor", "aids", "hiv", "virus",
           "treatment", "pain", "headache", "injury", "injuried", "health",
           "doctors", "healthy", "unhealthy", "sick", "nauseated", "bacteria",
           "allergy", "cough", "cold", "blood", "urine", "smoking", "smoke"]

EXAMS = ["exams", "exam", "school", "college", "course",
         "university", "test", "grade", "teacher", "examination", "question sheet",
         "phd", "my master", "thesis", "dissertation", "paper", "article", "journal",
         "conference", "experiment", "data analysis"]

DICTIONARIES = [RELATIONSHIP, WORK, DEATH, FINANCIAL, HEALTH, EXAMS]


def get_dictionaries():
    return DICTIONARIES
