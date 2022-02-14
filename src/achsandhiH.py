#!/usr/bin/python

import saMjñAprakaraNam

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
 
    return varNa_str

# सन्धिं विभजत
# test_shabda = ["ददादिदीदुदूदृदॄदॢदेदैदोदौदःद्"]
# test_shabda = ["चञ्चुः", "अ॒ग्निमी॑ळे", "घस्लादेशः", "गुर्वष्टकम्", "मात्रौदार्यम्", "धेन्वागमनम्", "दध्योदनः"]
# for shabda in test_shabda:
#     print(shabda, end=' ')
#     print(get_split_varNa(shabda), end=' ')
#     print()

# varNa_str = "आ॒पूर्वे॑भि॒रृषि॑भि॒रीप॒क्ड्यो॒मंप॒मं"
# varNa_str = "वैश्वामित्रः"
# varNa_str = "स॒त्यश्चि॒त्रश्र॑वस्तमः"
varNa_str = "वेद॑सा॒मस॑द्वृ॒धेर॑क्षि॒तापा॒युरद॑ब्धःस्व॒स्त"
print(varNa_str)
split_varNa = get_split_varNa(varNa_str)
print(split_varNa)
joined_str = get_joined_varNa(split_varNa)
print(joined_str)
print(varNa_str == joined_str)

# सन्धिं योजयत
# [["प्रति", "अयः"], ["बहुषु", "एकः"], ["भ्रातृ", "उक्तिः"], ["गमॢ", "इति"], ["वधू", "ऐश्वर्यम्"], ["जननी", "आह"]]

################################################################################
