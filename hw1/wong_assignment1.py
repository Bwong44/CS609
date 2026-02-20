from Bio import SeqIO #biopython package
import pandas as pd #pandas used to convert lists into an array dataframe
import matplotlib.pyplot as plt
import numpy as np
from hmmlearn import hmm

#Question 1, HMM
#Input CSV File
df = pd.read_csv("assignment1.csv")
drop = df.groupby("Read_ID")["Position"].diff().lt(0) #detects new seq by looking if the postion drops back to 1 so it'll be negative
version = drop.groupby(df["Read_ID"]).cumsum() #counts how many times drop happnes
df["Read_ID"] = df['Read_ID'] + "." + version.astype(str)  #appends to Read_ID with the drop number
xDataFrame = df[["Intensity_A", "Intensity_T","Intensity_G", "Intensity_C"]] #store the intensity columns
xNumpy = xDataFrame.to_numpy() #converts to np array
lengths = df.groupby("Read_ID").size().to_list() #gets lengths of each read for HMM

#Using given params
model = hmm.GaussianHMM(n_components=4, covariance_type="diag", random_state=0, init_params="") 
model.startprob_ = np.array([0.25, 0.25, 0.25, 0.25]) #ATGC equal start probabilities

transProb = np.array([[0.9, 0.033, 0.033, 0.033],
                     [0.033, 0.9, 0.033, 0.033],
                     [0.033, 0.033, 0.9, 0.033],
                     [0.033, 0.033, 0.033, 0.9]])
model.transmat_= transProb / transProb.sum(axis=1, keepdims=True) #normalize transition prob

model.means_ = np.array([[0.9, 0.05, 0.03, 0.02],
                         [0.05, 0.9, 0.03, 0.02],
                         [0.05, 0.05, 0.9, 0.02],
                         [0.05, 0.05, 0.03, 0.9]])

model.covars_ = np.full((4,4), 0.01)

logprob, stateSeq = model.decode(xNumpy, lengths, algorithm="viterbi") #decode the sequence using viterbi algorithm

#Output
map = np.array(["A","T","G","C"]) #map for nuc to state numbers
outputHMM = map[stateSeq] 
read_ids = df["Read_ID"].unique() #get unique read ids
index = 0 #index to track position of the outputHMM
with open("assignment1.fasta", "w") as f: #write to fasta file
    for rid, L in zip(read_ids, lengths):
        f.write(f">{rid}\n")
        f.write(f"".join(outputHMM[index:index+L]) + "\n") #writes out the strand for each, since length is the length of each read
        seqData = xNumpy[index:index+L]
        seqLogprob = model.score(seqData)
        print(f"Read_ID: {rid}\nLength: {L}\nLog Probability: {seqLogprob}\n\n")
        index += L

#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#

#Question 2, fastqc q score
# Read a FASTQ file record by record
rows = [] #List to hold quality score rows from SeqIO parse
for record in SeqIO.parse("assignment1.fastq", "fastq"):
    rows.append(record.letter_annotations['phred_quality'] #From biopython, gets qScore for each position as a list
    )
df = pd.DataFrame(rows) #Converts the list of lists into a dataframe named df

df.to_csv("output.csv", index=False)

with open("qScoresMedian", "w") as outFile: #Writes the median scores of each base to file
    outFile.write("Position,Median\n")
    for position, median in enumerate(df.median(), start=1):
        outFile.write(f"{position},{median}\n")

plt.figure(figsize=(12, 6))
plt.boxplot(df)
plt.xticks(rotation=90, ha="right") #Rotate x-axis labels 90 degrees
plt.tight_layout() #Adjust layout
plt.savefig("QScoreBoxplot.png")
