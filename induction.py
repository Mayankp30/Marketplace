# Script Name	: induction.py
# Author		: Mayank Purohit
# Created		: 22 Oct 2016
# Last Modified	: 
# Version		: 1.0

from jsonmerge import merge
import json
import glob
import itertools as itt


# reads all the files globally inside a folder 

read_files = glob.glob('/Users/Mayank/IdeaProjects/Vettery/past/*.json')

output_list = []

# appends data from all files to one single json file

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

		# iterating over list of data to get individual fields
		for i in range (0,len(all_week_list)):
			interview_c_ = [all_week_list[i]['User']['interview_count'], all_week_list[i]['Tag']] # stores interview count
			all_skill.append(all_week_list[i]['Tag'])  # stores all skills inside a tag
			info_list.append(interview_c_)

		_skills = list(itt.chain.from_iterable(all_skill))
		
		
		unique_skill_set = list(set(_skills))  # set - gets unique values 
		output_dict = dict()

		# iterating over all skills and creating dictionary where key - skill, value - (total interview count for a skill)/(total students that posses the skill)
		
		for i in range (0,len(unique_skill_set)):
			student_count=0
			total_interview_count=0
			for j in range(0,len(info_list)):
				stat=iter(info_list[j])
				k=iter(stat)
				interview_count=int(k.next())
				skills=k.next()
				if unique_skill_set[i] in skills:
					student_count=student_count+1
					total_interview_count=total_interview_count+interview_count
			output_dict[unique_skill_set[i]]=total_interview_count/student_count
		
		maximum = max(output_dict, key=output_dict.get) # key of maximum value i.e. ratio of interview_count/student_count
		minimum = min(output_dict, key=output_dict.get) # key of minimum value 
		
		MAX = (output_dict[maximum]) # maximum ratio of a skill
		MIN = (output_dict[minimum]) # minimum ratio of a skill


		scores_skill=dict()

		score=0

		# storing key - as skill and value - as linear score interpolation 

		# individual skill score =10 + (100 - 10) * (ratio - MIN)
		#------------------------      ---------- 
		#------------------------      (MAX- MIN)

		for key, value in output_dict.iteritems():
			ratio = value
			score = 10 + ((100-10)/(MAX-MIN))*(ratio-MIN)
			scores_skill[key]=score
