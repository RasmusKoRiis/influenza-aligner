import pandas as pd
import os

cwd = os.getcwd()
folder = os.path.basename(os.getcwd())


#PRIMER LENGHTS IN DICT - IMPORT INSTEAD? # MANGLER PROBE FOR TRIPLEX
primer_dict ={
    "InfB_MP_BMf_38_Ward" : 23,
    "InfB_MP_BMr_132_antisenseB_Ward" : 23,
    "InfB_MP_BM-probe_69_Ward" : 30,
    "InfA_MP_M52c" : 21,
    "InfA_MP_M149r": 23,
    "InfA_MP_probeM93c" : 23,
    "InfB_HA_BHA_188F" : 21,
    "InfB_HA_BHA270R" : 23,
    "InfB_HA_probe_VIC2" : 27,
    "InfB_HA_probe_VIC2" : 27,
    "InfB_HA_probe_VIC2" : 27,
    "InfB_HA_probe_YAM2" : 27,
    "InfB_HA_probe_YAM2" : 27,
    "InfB_HA_probe_YAM2" : 27,
    "InfB_HA_probe_YAM2" : 27,
    "InfA_MA_InfA_For1" : 25,
    "InfA_MA_InfA_For1" : 25,
    "InfA_MA_InfA_For2" : 25,
    "InfA_MA_InfA_For2" : 25,
    "InfA_MA_InfA_For2" : 25,
    "InfA_MA_InfA_For2" : 25,
    "InfA_MA_InfA_Rev1" : 23,
    "InfA_MA_InfA_Rev1" : 23,
    "InfA_MA_InfA_Rev1" : 23,
    "InfA_MA_InfA_Rev1" : 23,
    "InfA_MA_InfA_Rev1" : 23,
    "InfA_MA_InfA_Rev1" : 23,
    "InfA_MA_InfA_Rev2" : 23,
    "InfB_MA_InfA_For" : 22,
    "InfB_MA_InfA_For" : 22,
    "InfB_MA_InfA_Rev" : 22
}


#IMPORT PRIMER ALIGNMENT
df1 = pd.read_csv('{0}/blastn_{1}_MP.csv'.format(cwd,folder),  sep='\t', names=["Primer", "SequenceID", "Raw_Match(%)", "Alignment_Length", "Mismatches", "Gaps", "Primer_Start", "Primer_End", "Seq_Start", "Seq_End", "Expect", "Score"], index_col=False)


Subtype = folder

#Gene = "MP"

def discard (Subtype):
    if Subtype == "H3" or "H1":
        return "InfB"
    elif Subtype == "Bvic" or "Byam":
        return "InfA"

Discard = []
Discard.append(discard(Subtype))


#DATA MINGELING
#df1 = df1.iloc[:1]
df1 = df1.iloc[:,0:12]
df1['Primer_Length'] = df1['Primer'].map(primer_dict)
df1["Primer_Length/Alignment_length_dif"] = df1["Primer_Length"] - df1["Alignment_Length"]
df1["Primer_Length/Alignment_length_dif"] = df1["Primer_Length/Alignment_length_dif"].abs()
df1["ID"] = df1['Primer'].astype(str) +"_"+ df1["SequenceID"].astype(str)
df1["Length_Para"] = df1["Primer_Length"] - df1["Alignment_Length"]

df1 = df1.sort_values("Score", ascending=False).drop_duplicates('ID').sort_index()
#df1 = df1.sort_values("Primer_Length/Alignment_length_dif", ascending=True).drop_duplicates('ID').sort_index()

df1["Match(%)"] = ((df1["Primer_Length"] - (df1["Mismatches"] + df1["Gaps"] + ((df1["Primer_Length"]) - df1["Alignment_Length"]))) / df1["Primer_Length"])
df1["Total_Mis"] = df1["Mismatches"] + df1["Gaps"] + df1["Primer_Length/Alignment_length_dif"]

df1 = df1[~df1.Primer.str.contains('|'.join(Discard))]

#SAVE FINAL DATAFRAME TO CSV
df1.to_csv('primer_{}_MP.csv'.format(folder), index=False)
#df1.to_csv('/Users/rasmuskopperudriis/Coding/projects/influenza-aligner/python_results.csv')
