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

def get_yaNsandhi_joined(inputword1, inputword2):

    ik_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('इक्')
    ik_varNa_lol = [saMjñAprakaraNam.get_all_svara(x) for x in ik_varNa] # list of lists

    yaN_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('यण्')

    ach_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('अच्')
    ach_varNa_all = [x for y in ach_varNa for x in saMjñAprakaraNam.get_all_svara(y)]

    split_varNa = get_split_varNa(inputword1) + get_split_varNa(inputword2)

    for i in range(len(split_varNa)-1):

        for ik_index, ik_sublist in enumerate(ik_varNa_lol):
            if split_varNa[i] in ik_sublist and split_varNa[i+1] in ach_varNa_all:
                split_varNa[i] = yaN_varNa[ik_index]
                break

    return get_joined_varNa(split_varNa)

# सन्धिं योजयत
# test_words = [
#     ["प्रति", "अयः"], ["बहुषु", "एकः"], ["भ्रातृ", "उक्तिः"], ["गमॢ", "इति"], 
#     ["वधू", "ऐश्वर्यम्"], ["जननी", "आह"]]
# for word in test_words:
#     print(word, end=' ')
#     print(get_yaNsandhi_joined(word[0], word[1]), end=' ')
#     print()

def get_yaNsandhi_split(inputword):

    ik_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('इक्')

    yaN_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('यण्')

    ach_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('अच्')
    ach_varNa_all = [x for y in ach_varNa for x in saMjñAprakaraNam.get_all_svara(y)]

    split_varNa = get_split_varNa(inputword)

    outputwords = []
    outputindex = 0

    for i in range(len(split_varNa)-1):

        if split_varNa[i] in yaN_varNa and split_varNa[i+1] in ach_varNa_all:

            split_varNa[i] = ik_varNa[yaN_varNa.index(split_varNa[i])]
            outputwords.append(get_joined_varNa(split_varNa[outputindex:i+1]))
            outputindex = i+1
            # break # Remove break to find more sandhi

    outputwords.append(get_joined_varNa(split_varNa[outputindex:]))

    return outputwords

# सन्धिं विभजत
# test_words = ["देव्युवाच", "घस्लादेशः", "गुर्वष्टकम्", "मात्रौदार्यम्", "धेन्वागमनम्", "दध्योदनः"]
# for word in test_words:
#     print(word, end=' ')
#     print(get_yaNsandhi_split(word), end=' ')
#     print()

################################################################################
# १८ अनचि च [८.४.४७ ]

def get_anachi_joined(inputword):

    yar_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('यर्')

    ach_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('अच्')
    ach_varNa_all = [x for y in ach_varNa for x in saMjñAprakaraNam.get_all_svara(y)]

    split_varNa = get_split_varNa(inputword)
    split_varNa_output = []

    ach_found = False
    for i in range(len(split_varNa)):

        split_varNa_output.append(split_varNa[i])

        if split_varNa[i] in ach_varNa_all:
            ach_found = True
        else:
            if split_varNa[i] in yar_varNa:
                if ach_found == True:
                    if (i+1 < len(split_varNa)):
                        if (split_varNa[i+1] not in ach_varNa_all):
                            split_varNa_output.append(split_varNa[i])
                    else:
                        split_varNa_output.append(split_varNa[i])
            ach_found = False

    return get_joined_varNa(split_varNa_output)

# test_words = ["कृष्णः", "रामात्", "मत्यत्र", "कृष्णस्य"]
# for word in test_words:
#     print(word, end=' ')
#     print(get_anachi_joined(word), end=' ')
#     print()

################################################################################
# १९ झलां जश् झशि [८.४.५३ ]

def get_jhalAMjashjhashi_joined(inputword):

    jhal_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('झल्')
    jhash_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('झश्')
    jash_varNa = saMjñAprakaraNam.get_pratyAhAra_varNa('जश्')

    split_varNa = get_split_varNa(inputword)

    for i in range(len(split_varNa)-1):
        if split_varNa[i] in jhal_varNa and split_varNa[i+1] in jhash_varNa:

            # क् / ख् / ग् / घ् एतेषां जश्त्वे कृते तेषां स्थाने आन्तरतम्येन गकारः विधीयते।
            if (split_varNa[i] in saMjñAprakaraNam.ku_varga_varNa):
                split_varNa[i] = saMjñAprakaraNam.ku_varga_varNa[2]
            # च् / छ् / ज् / झ् एतेषाम् प्रकृतसूत्रेण जश्त्वम् नैव सम्भवति।
            # elif (split_varNa[i] in saMjñAprakaraNam.chu_varga_varNa):
            #     split_varNa[i] = saMjñAprakaraNam.chu_varga_varNa[2]
            # ट् / ठ् / ड् / ढ् एतेषां जश्त्वे कृते तेषां स्थाने आन्तरतम्येन डकारः विधीयते।
            elif (split_varNa[i] in saMjñAprakaraNam.Tu_varga_varNa):
                split_varNa[i] = saMjñAprakaraNam.Tu_varga_varNa[2]
            # त् / थ् / द् / ध् एतेषां जश्त्वे कृते तेषां स्थाने आन्तरतम्येन दकारः विधीयते।
            elif (split_varNa[i] in saMjñAprakaraNam.tu_varga_varNa):
                split_varNa[i] = saMjñAprakaraNam.tu_varga_varNa[2]
            # प् / फ / ब् / भ् एतेषां जश्त्वे कृते तेषां स्थाने आन्तरतम्येन बकारः विधीयते।
            elif (split_varNa[i] in saMjñAprakaraNam.pu_varga_varNa):
                split_varNa[i] = saMjñAprakaraNam.pu_varga_varNa[2]
            # शकारस्य जश्त्वे कृते तस्य स्थाने उच्चारणस्थानसाधर्म्यम् अनुसृत्य आन्तरतम्येन जकारः विधीयते।
            elif (split_varNa[i] == 'श्'):
                split_varNa[i] = 'ज्'
            # षकारस्य जश्त्वे कृते तस्य स्थाने उच्चारणस्थानसाधर्म्यम् अनुसृत्य आन्तरतम्येन डकारः विधीयते।
            elif (split_varNa[i] == 'ष्'):
                split_varNa[i] = 'ड्'
            # सकारस्य जश्त्वे कृते तस्य स्थाने उच्चारणस्थानसाधर्म्यम् अनुसृत्य आन्तरतम्येन दकारः विधीयते।
            elif (split_varNa[i] == 'स्'):
                split_varNa[i] = 'द्'
            # हकारस्य प्रकृतसूत्रेण जश्त्वम् नैव सम्भवति।

    return get_joined_varNa(split_varNa)

# सन्धिं योजयत
# test_words = [
#     ["तनु", "अङ्गी"], ["विधि", "उद्देशः"], ["नृ", "आत्मजः"], ["लघु", "आकारः"],
#     ["कूपी", "उदकम्"], ["पतॢ", "उपदेशः"], ["विधातृ", "इच्छा"], ["अस्ति", "अनुभवः"],
#     ["अभि", "उपेत्य"], ["वधू", "इयम्"]]
# for word in test_words:
#     print(word, end=' ')
#     yaNsandhi_word = get_yaNsandhi_joined(word[0], word[1])
#     print(yaNsandhi_word, end=' ')
#     anachi_word = get_anachi_joined(yaNsandhi_word)
#     print(anachi_word, end=' ')
#     jhalAMjashjhashi_word = get_jhalAMjashjhashi_joined(anachi_word)
#     print(jhalAMjashjhashi_word, end=' ')
#     print()

# सन्धिं विभजत
test_words = [
    "गुकारस्त्वन्धकारस्तु", "ह्यहं", "कर्मण्यतन्द्रितः", "शास्त्रेष्वकुण्ठिता", "वस्त्वस्ति",
    "पृथिव्यप्तेजोवाय्वाकाशकालदिगात्ममनांसि", "यू", "स्त्र्याख्यौ"]
for word in test_words:
    print(word, end=' ')
    print(get_yaNsandhi_split(word), end=' ')
    print()

################################################################################
