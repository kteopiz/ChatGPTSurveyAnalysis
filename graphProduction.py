# Names: Kyle Teopiz, Alan Pangnathip, Joseph Carvalho, Hameez Iqbal
# Date: Wednesday, March 1, 2023
import csv
import matplotlib.pyplot as plt
import numpy as np

rows = []
# Simple Printer without formatting
with open('chatGPT_ethics_survey_responses.csv', newline='') as f:
    reader = csv.reader(f)

    # Slice occurs at [1:] to remove the first unneeded row which contains the survey questions
    survey_response_rows = (list(reader)[1:])

# Filters out the Time Stamps from each row of responses as it is uneeded data
for i in range(len(survey_response_rows)):
    survey_response_rows[i] = survey_response_rows[i][1:]


