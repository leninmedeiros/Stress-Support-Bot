RELATIONSHIP = ["relationship", "relationships", "girlfriends", "boyfriends",
                "wifes", "girlfriend", "boyfriend", "wife",
                "husband", "husbands", "marriage", "divorce", "divorced",
                "broke up", "crushes", "romances", "affairs",
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
                "nuptials", "honeymoon", "cheated on", "cheat on",
                "someone else", "passion", "bad sex"]

WORK = ["work", "worked", "works", "working", "boss", "bosses", "work load",
        "job", "jobs", "task", "tasks", "projects", "companies", "managers"
        "project", "company", "production", "nightwork", "duty",
        "duties", "mission", "wash", "substituting", "ironing", "operation",
        "labour", "shining", "tending", "social service", "heavy lifting",
        "loose end", "labor", "polishing", "housework", "investigation",
        "timework", "make-work", "lavation", "welfare work", "paperwork",
        "toil", "attention", "spadework", "unfinished business", "action",
        "investigating", "washing", "subbing", "care", "missionary work",
        "logging", "housekeeping", "housewifery", "undertaking", "coursework",
        "activity", "busywork", "aid", "procedure", "old man", "employer",
        "hirer", "guvnor", "foreman", "gaffer", "supervisor", "superior", "baas",
        "assistant foreman", "chief", "honcho", "ganger", "straw boss", "leader",
        "executive", "administrator", "general manager", "manager", "colleague",
        "employee", "fired", "hired", "hiring", "firing", "deadline",
        "deadlines", "business", "service", "colleagues", "employed", "full time",
        "home office", "firm", "firms"]

LOSS = ["death", "died", "dead", "passed away", "pass away", "loss",
         "passed out", "decease", "deaths", "deceases", "losses"
         "expiry", "passing away", "passing out", "dying", "bury",
         "buried", "funeral", "killed",
         "deceased", "no more", "rest in piece"]

FINANCIAL = ["financial", "salary", "paycheck", "money", "debt", "debts",
             "business", "fiscal", "monetary", "fund", "currency", "cash",
             "pound", "pounds", "dollar", "dollars", "bank", "investment",
             "investments", "bill", "bills", "euro", "euros", "$", "€", "£",
             "wealth", "bundle", "pile", "sterling", "currency", "atm", "account",
             "insurance", "price", "rent", "cent", "penny", "pound", "broke",
             "lend", "borrow", "loan", "expenses", "expense"]

HEALTH = ["disease", "illness", "ill", "surgery", "tumor", "diagnose",
           "cancer", "hospital", "doctor", "aids", "hiv", "virus", "infection",
           "treatment", "pain", "headache", "injury", "injuried", "injured",
           "doctors", "healthy", "unhealthy", "sick", "sickness", "nauseated",
           "allergy", "cough", "cold", "blood", "urine", "smoking", "smoke",
           "suffer", "suffering", "diagnosis", "infected", "health", "bacteria",
           "condition", "diseases", "bacterias", "doctors", "clinical", "overweight",
           "unprotected sex", "drugs", "tobacco", "alcohol", "diet", "std",
           "sexually transmitted disease", "sexually transmitted diseases"]

EDUCATIONAL = ["exams", "exam", "school", "college", "course", "learn"
         "university", "test", "grade", "teacher", "examination", "question sheet",
         "phd", "my master", "thesis", "dissertation", "paper", "article", "journal",
         "conference", "experiment", "data analysis", "education", "schools",
         "articles", "journals", "master degree", "bachelor"]

DICTIONARIES = [RELATIONSHIP, WORK, LOSS, FINANCIAL, HEALTH, EDUCATIONAL]


def get_dictionaries():
    return DICTIONARIES
