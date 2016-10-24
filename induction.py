# Script Name	: induction.py
# Author		: Mayank Purohit
# Created		: 22 Oct 2016
# Last Modified	: 
# Version		: 1.0

from jsonmerge import merge
import json
import glob
import itertools as itt


# reads all the files in global scope 

read_files = glob.glob('/Users/Mayank/IdeaProjects/Vettery/past/*.json')

output_list = []

# merge files into single json file

for f in read_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

with open("merged_file.json", "wb") as outfile:
    json.dump(output_list, outfile)


with open('merged_file.json') as json_data:
		all_week_data = json.load(json_data)
		all_week_list = list(itt.chain.from_iterable(all_week_data))
	
		info_list = []
		all_skill = []

		# extracting interview count / tags from candidates info
		for i in range (0,len(all_week_list)):
			interview_c_ = [all_week_list[i]['User']['interview_count'], all_week_list[i]['Tag']] # gets and stores interview count along with set of skills
			all_skill.append(all_week_list[i]['Tag']) 
			info_list.append(interview_c_)

		_skills = list(itt.chain.from_iterable(all_skill))
		
		
		unique_skill_set = list(set(_skills))  # set - gets unique value of skills
		output_dict = dict()

		# assigning ratios of interview count per candidate for each skill set
		
		for i in range (0,len(unique_skill_set)):
			candidate_count=0
			total_interview_count=0
			for j in range(0,len(info_list)):
				stat=iter(info_list[j])
				k=iter(stat)
				interview_count=int(k.next())
				skills=k.next()
				if unique_skill_set[i] in skills:
					candidate_count=candidate_count+1
					total_interview_count=total_interview_count+interview_count
			output_dict[unique_skill_set[i]]=total_interview_count/candidate_count
		
		maximum = max(output_dict, key=output_dict.get) # key of maximum value i.e. ratio of interview_count/student_count
		minimum = min(output_dict, key=output_dict.get) # key of minimum value 
		
		MAX = (output_dict[maximum]) # maximum ratio of a skill
		MIN = (output_dict[minimum]) # minimum ratio of a skill


		scores_skill=dict()

		score=0

		# assigning score to each skill set based on interview count to candidate count ratio

		# individual skill score = 10 + (100 - 10) * (ratio - MIN)
		#------------------------      ---------- 
		#------------------------      (MAX- MIN)

		for key, value in output_dict.iteritems():
			ratio = value
			score = 10 + ((100-10)/(MAX-MIN))*(ratio-MIN)
			scores_skill[key]=score
