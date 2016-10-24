# Script Name   : prediction.py
# Author        : Mayank Purohit
# Created       : 21 Oct 2016
# Last Modified : 
# Version       : 1.0

import induction as ind
import json


historical_scores=ind.scores_skill

with open('/Users/Mayank/IdeaProjects/Vettery/present/next_week.json') as json_data:
    next_week_data = json.load(json_data)
    
    candidate_prof=dict()  # dictionary , key - name of candidate , value - (sum of all the scores of skills) / (total number of skills)

    for i in range(0,len(next_week_data)):
    	candidate_skills=next_week_data[i]['Tag']               # gets all the skills of a candidate
    	candidate_fname=next_week_data[i]['User']['first_name'] # gets first name of candidate
    	candidate_lname=next_week_data[i]['User']['last_name']  # gets last name of candidate
    	name=candidate_fname+' '+candidate_lname                # first name + last name of candidate
    	candidate_avg_score= sum([historical_scores[x] for x in candidate_skills])/len(candidate_skills)
    	candidate_prof[name]=candidate_avg_score 
    
    most_requested_candidate= max(candidate_prof, key=candidate_prof.get) # gets key-name of candidate with highest average score 
    
    the_winner = most_requested_candidate

    print 'The candidate with the most interviews should be...' + the_winner + '\n'

