#!/usr/bin/python

import saMjñAprakaraNam

################################################################################

import viShNusahasranAma

# Print list
# nAma_list = viShNusahasranAma.nAma_list
# print(len(nAma_list))

################################################################################
# Read viShNusahasranAma.csv

import csv
def get_nAma_list():

    nAma_list = []

    with open('../data/viShNusahasranAma.csv', 'r') as read_obj:
    
        csv_reader = csv.reader(read_obj)
        nAma_list = list(csv_reader)

    return nAma_list

# Print list
# nAma_list = get_nAma_list()
# for index in range(len(nAma_list)):
#     print(str(nAma_list[index][1::]) + ',')

################################################################################

import unicodedata
def get_split_varNa(varNa_str):

    split_varNa = []

    cv = None
    sole_vyañjana_found = False

    for v in varNa_str:

        if unicodedata.category(v)[0] == 'L':
            if (cv):
                split_varNa.append(cv)
                if sole_vyañjana_found:
                    sole_vyañjana_found = False
                    split_varNa.append('अ')
            cv = v
            if (v+saMjñAprakaraNam.virAma_chinha in saMjñAprakaraNam.vyañjana_varNa):
                cv += saMjñAprakaraNam.virAma_chinha
                sole_vyañjana_found = True

        elif unicodedata.category(v)[0] == 'M':

            if (v in saMjñAprakaraNam.mAtrA_svara_varNa):
                if (cv):
                    split_varNa.append(cv)
                    if sole_vyañjana_found:
                        sole_vyañjana_found = False
                cv = saMjñAprakaraNam.get_svara_from_mAtrA(v)
            elif (v == saMjñAprakaraNam.virAma_chinha):
                if sole_vyañjana_found:
                    sole_vyañjana_found = False
            elif (
                (v == saMjñAprakaraNam.anudAtta_rekhA) or 
                (v == saMjñAprakaraNam.svarita_rekhA) or 
                (v == saMjñAprakaraNam.anunAsika_chandrabindu)):

                if (cv):
                    if sole_vyañjana_found:
                        sole_vyañjana_found = False
                        split_varNa.append(cv)
                        cv = 'अ'
                cv += v
            else:
                if (cv):
                    split_varNa.append(cv)
                    if sole_vyañjana_found:
                        sole_vyañjana_found = False
                        split_varNa.append('अ')
                cv = v

        elif unicodedata.category(v)[0] == 'Z':
            if (cv):
                split_varNa.append(cv)
                if sole_vyañjana_found:
                    sole_vyañjana_found = False
                    split_varNa.append('अ')
            cv = v

        else:
            pass        

    if (cv):
        split_varNa.append(cv)
        if sole_vyañjana_found:
            split_varNa.append('अ')

    return split_varNa

def get_joined_varNa(split_varNa):

    varNa_str = ''
    sole_vyañjana_found = False

    for v in split_varNa:

        if (v in saMjñAprakaraNam.svara_varNa_all):
            if sole_vyañjana_found == True:
                sole_vyañjana_found = False
                mAtrA = saMjñAprakaraNam.get_mAtrA_from_svara(v[0])
                if mAtrA:
                    varNa_str += mAtrA + v[1:]
                else:
                    varNa_str += v[1:]
            else:
                varNa_str += v

        elif (v in saMjñAprakaraNam.vyañjana_varNa):
            if sole_vyañjana_found == True:
                varNa_str += saMjñAprakaraNam.virAma_chinha
            varNa_str += v[0]
            sole_vyañjana_found = True
            
        else:
            varNa_str += v
 
    if sole_vyañjana_found == True:
        varNa_str += saMjñAprakaraNam.virAma_chinha
        
    return varNa_str

# test_words = [
#     "देव्युवाच", "धेन्वागमनम्", "स॒त्यश्चि॒त्रश्र॑वस्तमः", "सु॑म॒तिरृ॑जूय॒तां", 
#     "स्तुष्टु॒वांस॑स्त॒नूभि॒र्व्य॑शेम", "प॒त॒यन्म॑न्द॒यत्स॑खम्"]
# for word in test_words:
#     print(word, end=' ')
#     split_varNa = get_split_varNa(word)
#     joined_varNa = get_joined_varNa(split_varNa)
#     print(joined_varNa, end=' ')
#     print(word == joined_varNa)

################################################################################

def get_nAma_with_start_varNa(start_varNa):

    nAma_list = viShNusahasranAma.nAma_list

    output_list = [x for x in nAma_list if get_split_varNa(x[0])[0] == start_varNa]

    return output_list

# Print list
# nAma_list = get_nAma_with_start_varNa('क्')
# for index in range(len(nAma_list)):
#     print(nAma_list[index][0])

################################################################################

def get_nAma_with_len(nAma_len):

    nAma_list = viShNusahasranAma.nAma_list

    output_list = [x for x in nAma_list if len(list(saMjñAprakaraNam.get_split_cluster(x[0]))) == nAma_len]
    
    return output_list

# Print list
# nAma_list = get_nAma_with_len(10)
# for index in range(len(nAma_list)):
#     print(nAma_list[index][0])

################################################################################
