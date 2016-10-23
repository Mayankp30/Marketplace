from jsonmerge import merge
import json
import glob
import itertools as itt

read_files = glob.glob('/Users/Mayank/IdeaProjects/Vettery/past/*.json')
output_list = []

for f in read_files:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

with open("merged_file.json", "wb") as outfile:
    json.dump(output_list, outfile)


with open('merged_file.json') as json_data:
		allweekdata = json.load(json_data)
		allweeklist = list(itt.chain.from_iterable(allweekdata))
		
		infolist=[]
		all_skill = []
		for i in range (0,len(allweeklist)):
			interview_skill = [allweeklist[i]['User']['interview_count'], allweeklist[i]['Tag']]
			all_skill.append(allweeklist[i]['Tag'])
			infolist.append(interview_skill)

		_skills = list(itt.chain.from_iterable(all_skill))
		
		
		unique_skill_set = list(set(_skills))
		output_dict = dict()
		for i in range (0,len(unique_skill_set)):
			
			student_count=0
			total_interview_count=0
			for j in range(0,len(infolist)):
				stat=iter(infolist[j])
				k=iter(stat)
				interview_count=int(k.next())
				skills=k.next()
				if unique_skill_set[i] in skills:
					student_count=student_count+1
					total_interview_count=total_interview_count+interview_count
			#print student_count
			#print total_interview_count
			output_dict[unique_skill_set[i]]=total_interview_count/student_count
		print output_dict
		
		maximum = max(output_dict, key=output_dict.get)
		print maximum


		

				
				

								




		the_winner = 'Mayank'
		print 'The candidate with the most interviews should be...' + the_winner + '\n'
