def load_data(file_path):
	''' Converts data from:
	word \t label \n word \t label \n \n word \t label
	to: sentence, {entities : [(start, end, label), (stard, end, label)]}
	'''
	file = open(file_path, 'r')
	training_data, entities, sentence, unique_labels = [], [], [], []
	current_annotation = None
	start =0
	end = 0 # initialize counter to keep track of start and end characters
	for line in file:
		line = line.strip("\n").split("\t")
		# lines with len > 1 are words
		if len(line) > 1:
			label = line[1]
			if(label != 'O'):
				label = line[1]+"_MED"	 # the .txt is formatted: label \t word, label[0:2] = label_type
			#label_type = line[0][0] # beginning of annotations - "B", intermediate - "I"
			word = line[0]
			sentence.append(word)
			start = end
			end += (len(word) + 1)  # length of the word + trailing space

			if label == 'I_MED' :  # if at the end of an annotation
				entities.append(( start,end-1, label))  # append the annotation
							  
			if label == 'B_MED':						 # if beginning new annotation
				entities.append(( start,end-1, label))# start annotation at beginning of word
				
		   
		   
			if label != 'O' and label not in unique_labels:
				unique_labels.append(label)
 
		# lines with len == 1 are breaks between sentences
		if len(line) == 1:
			if(len(entities) > 0):
				sentence = " ".join(sentence)
				training_data.append([sentence, {'entities' : entities}])
			# reset the counters and temporary lists
			end = 0 
			start = 0
			entities, sentence = [], []
			
	file.close()
	return training_data, unique_labels



train_filenames = ['data/Disease/BC2GM/train.tsv', 'data/Disease/BC4CHEMD/train.tsv', 'data/Disease/BC5CDR-chem/train.tsv', 'data/Disease/BC5CDR-disease/train.tsv', 'data/Disease/JNLPBA/train.tsv', 'data/Disease/linnaeus/train.tsv', 'data/Disease/NCBI-disease/train.tsv', 'data/Disease/s800/train.tsv'] 
test_filenames = ['data/Disease/BC2GM/test.tsv', 'data/Disease/BC4CHEMD/test.tsv', 'data/Disease/BC5CDR-chem/test.tsv', 'data/Disease/BC5CDR-disease/test.tsv', 'data/Disease/JNLPBA/test.tsv', 'data/Disease/linnaeus/test.tsv', 'data/Disease/NCBI-disease/test.tsv', 'data/Disease/s800/test.tsv'] 
val_filenames = ['data/Disease/BC2GM/train_dev.tsv', 'data/Disease/BC4CHEMD/train_dev.tsv', 'data/Disease/BC5CDR-chem/train_dev.tsv', 'data/Disease/BC5CDR-disease/train_dev.tsv', 'data/Disease/JNLPBA/train_dev.tsv', 'data/Disease/linnaeus/train_dev.tsv', 'data/Disease/NCBI-disease/train_dev.tsv', 'data/Disease/s800/train_dev.tsv'] 
# Open file3 in write mode 
with open('data/Disease/disease_dataset_combined/train_combined.txt', 'w') as outfile: 

	# Iterate through list 
	for names in train_filenames: 
  
		# Open each file in read mode 
		with open(names) as infile:
			outfile.write(infile.read()) 
  
		# Add '\n' to enter data of file2 
		# from next line 
		outfile.write("\n")
		outfile.write("\n")
	#outfile.close

with open('data/Disease/disease_dataset_combined/test_combined.txt', 'w') as outfile: 

	# Iterate through list 
	for names in test_filenames: 
  
		# Open each file in read mode 
		with open(names) as infile:
			outfile.write(infile.read()) 
  
		# Add '\n' to enter data of file2 
		# from next line 
		outfile.write("\n")
		outfile.write("\n")
	#outfile.close

with open('data/Disease/disease_dataset_combined/val_combined.txt', 'w') as outfile: 
  
	# Iterate through list 
	for names in val_filenames: 
  
		# Open each file in read mode 
		with open(names) as infile:
			outfile.write(infile.read()) 
  
		# Add '\n' to enter data of file2 
		# from next line 
		outfile.write("\n")
		outfile.write("\n")
	#outfile.close

TRAIN_DATA, LABELS = load_data("data/Disease/disease_dataset_combined/train_combined.txt")
print(len(TRAIN_DATA))
TEST_DATA, _ = load_data("data/Disease/disease_dataset_combined/test_combined.txt")
print(len(TEST_DATA))
VALID_DATA, _ = load_data("data/Disease/disease_dataset_combined/val_combined.txt")
print(len(VALID_DATA))





# ADD _DISEASE tags
file = open('data/Disease/disease_dataset_combined/train_combined.txt', 'r')
combined_list = []
for line in file:
	line = line.strip("\n").split("\t")
	if len(line) > 1:
		label = line[1]
		if(label != 'O'):
			label = line[1]+"-MED"
			result_combination = line[0] + '\t' + label
			combined_list.append(result_combination)
		else:
			result_combination = line[0] + '\t' + line[1]
			combined_list.append(result_combination)
	if len(line) == 1:
		combined_list.append("")

with open('data/Disease/train.txt', 'w') as outfile:  
	for names in combined_list: 
		outfile.write(names) 
		outfile.write("\n")


file = open('data/Disease/disease_dataset_combined/test_combined.txt', 'r')
combined_list = []
for line in file:
	line = line.strip("\n").split("\t")
	if len(line) > 1:
		label = line[1]
		if(label != 'O'):
			label = line[1]+"-MED"
			result_combination = line[0] + '\t' + label
			combined_list.append(result_combination)
		else:
			result_combination = line[0] + '\t' + line[1]
			combined_list.append(result_combination)
	if len(line) == 1:
		combined_list.append("")

with open('data/Disease/test.txt', 'w') as outfile:  
	for names in combined_list: 
		outfile.write(names) 
		outfile.write("\n")

file = open('data/Disease/disease_dataset_combined/val_combined.txt', 'r')
combined_list = []
for line in file:
	line = line.strip("\n").split("\t")
	if len(line) > 1:
		label = line[1]
		if(label != 'O'):
			label = line[1]+"-MED"
			result_combination = line[0] + '\t' + label
			combined_list.append(result_combination)
		else:
			result_combination = line[0] + '\t' + line[1]
			combined_list.append(result_combination)
	if len(line) == 1:
		combined_list.append("")

with open('data/Disease/valid.txt', 'w') as outfile:  
	for names in combined_list: 
		outfile.write(names) 
		outfile.write("\n")

