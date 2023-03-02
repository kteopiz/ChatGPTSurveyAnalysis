# Names: Kyle Teopiz, Alan Pangnathip, Joseph Carvalho, Hameez Iqbal
# Date: Wednesday, March 1, 2023

import csv
import matplotlib.pyplot as plt
import numpy as np


# Simple Printer without formatting
with open('chatGPT_ethics_survey_responses.csv', newline='') as f:
    reader = csv.reader(f)

    # Slice occurs at [1:] to remove the first unneeded row which contains the survey questions
    survey_response_rows = (list(reader)[1:])

# Filters out the Time Stamps from each row of responses as it is unneeded data
for i in range(len(survey_response_rows)):
    survey_response_rows[i] = survey_response_rows[i][1:]

QUESTION_ACCESSOR = {
    "age_range" : 0,
    "gender" : 1,
    "academia_status": 2,
    "location": 3,
    "political_spectrum": 4,
    "religion": 5,
    "heard_of_chatGPT": 6,
    "have_used_chatGPT": 7,
    "plagiarism_for_essays_prompt": 8,
    "cuse_for_research_prompt": 9,
    "use_in_workplace_prompt": 10,
    "effect_on_student_learning": 11,
    "instructor_use": 12,
    "personal_use": 13
}




