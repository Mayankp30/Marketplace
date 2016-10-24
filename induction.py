import prediction as pd
import json


historical_scores=pd.scores_skill

with open('/Users/Mayank/IdeaProjects/Vettery/present/next_week.json') as json_data:
    nextweekdata = json.load(json_data)
    
    candidate_prof={}

    for i in range(0,len(nextweekdata)):
    	candidate_skills=nextweekdata[i]['Tag']
    	candidate_fname=nextweekdata[i]['User']['first_name']
    	candidate_lname=nextweekdata[i]['User']['last_name']
    	name=candidate_fname+candidate_lname
    	print name
    	candidate_avg_score= sum([historical_scores[x] for x in candidate_skills])/len(candidate_skills)
    	candidate_prof[name]=candidate_avg_score 
    
    most_requested= max(candidate_prof, key=candidate_prof.get)
  

    the_winner = most_requested
    print 'The candidate with the most interviews should be...' + the_winner + '\n'

