#!/usr/bin/python

################################################################################
# माहेश्वराणि सूत्राणि

mAheshvara_sUtra = [
    ['अ', 'इ', 'उ', 'ण्'],
    ['ऋ', 'ऌ', 'क्'],
    ['ए', 'ओ', 'ङ्'],
    ['ऐ', 'औ', 'च्'],
    ['ह', 'य', 'व', 'र', 'ट्'],
    ['ल', 'ण्'],
    ['ञ', 'म', 'ङ', 'ण', 'न', 'म्'],
    ['झ', 'भ', 'ञ्'],
    ['घ', 'ढ', 'ध', 'ष्'],
    ['ज', 'ब', 'ग', 'ड', 'द', 'श्'],
    ['ख', 'फ', 'छ', 'ठ', 'थ', 'च', 'ट', 'त', 'व्'],
    ['क', 'प', 'य्'],
    ['श', 'ष', 'स', 'र्'],
    ['ह', 'ल्']]

################################################################################
# १ हलन्त्यम्[ १.३.३ ]

def get_it_varNa():
    it = []
    for msUtra in mAheshvara_sUtra:
        it.append(msUtra[-1])
    return it

# Print all इत् varNa
# print(get_it_varNa())

################################################################################
# ४ आदिरन्त्येन सहेता [१.१.७१ ]

import unicodedata
def get_split_cluster(s):
    """Generate the grapheme clusters for the string s. (Not the full
    Unicode text segmentation algorithm, but probably good enough for
    Devanagari.)

    """
    virama = u'\N{DEVANAGARI SIGN VIRAMA}'
    cluster = u''
    last = None
    for c in s:
        cat = unicodedata.category(c)[0]
        if cat == 'M' or cat == 'L' and last == virama:
            cluster += c
        else:
            if cluster:
                yield cluster
            cluster = c
        last = c
    if cluster:
        yield cluster

def get_pratyAhAra_varNa(pratyAhAra, occurrence_index = 0):
    split_cluster = list(get_split_cluster(pratyAhAra))
    start_flag = False
    pratyAhAra_varNa = []
    oindex = 0

    for msUtra in mAheshvara_sUtra:
        for varNa in msUtra:
            if start_flag == False:                
                if varNa == split_cluster[0]:
                    start_flag = True
                    pratyAhAra_varNa.append(varNa)
            else:
                if varNa != msUtra[-1]:
                    if varNa not in pratyAhAra_varNa:
                        pratyAhAra_varNa.append(varNa)
                if varNa == split_cluster[1]:
                    if oindex == occurrence_index:
                        start_flag = False
                        break
                    else:
                        oindex += 1
        else:
            continue
        break
    return pratyAhAra_varNa

svara_varNa = get_pratyAhAra_varNa('अच्')
vyañjana_varNa = get_pratyAhAra_varNa('हल्')
antaHstha_varNa = get_pratyAhAra_varNa('यण्')
pañchama_varga_varNa = get_pratyAhAra_varNa('ञम्')
chaturtha_varga_varNa = get_pratyAhAra_varNa('झष्')
tRRitIya_varga_varNa = get_pratyAhAra_varNa('जश्')

dvitIyaprathama_varga_varNa = get_pratyAhAra_varNa('खय्')
dvitIyaprathama_varga_varNa_hlen = len(dvitIyaprathama_varga_varNa)//2
dvitIya_varga_varNa = dvitIyaprathama_varga_varNa[:dvitIyaprathama_varga_varNa_hlen]
prathama_varga_varNa = dvitIyaprathama_varga_varNa[dvitIyaprathama_varga_varNa_hlen:]
uShmANa_varNa = get_pratyAhAra_varNa('शल्')
mRRiduvyañjana_varNa = get_pratyAhAra_varNa('हश्')
karkashavyañjana_varNa = get_pratyAhAra_varNa('खर्')

vyañjana_varga_varNa = pañchama_varga_varNa + chaturtha_varga_varNa + tRRitIya_varga_varNa + dvitIya_varga_varNa + prathama_varga_varNa

# Test प्रत्याहार formation
# print(f"इच् are: {get_pratyAhAra_varNa('इच्')}") # अकारं विना अन्ये स्वराः
# print(f"वल् are: {get_pratyAhAra_varNa('वल्')}") # यकारं विना अन्यानि व्यञ्जनानि
# print(f"यम् are: {get_pratyAhAra_varNa('यम्')}") # अन्तःस्थाः, अनुनासिक-व्यञ्जनानि च
# print(f"झश् are: {get_pratyAhAra_varNa('झश्')}") # वर्गाणां तृतीय-चतुर्थवर्णाः
# print(f"यय् are: {get_pratyAhAra_varNa('यय्')}") # ऊष्मवर्णान् विहाय अन्यानि व्यञ्जनानि
# print(f"झय् are: {get_pratyAhAra_varNa('झय्')}") # वर्गाणां प्रथम-द्वितीय-तृतीय-चतुर्थवर्णाः
# print(f"इण् are: {get_pratyAhAra_varNa('इण्', 1)}")
# print(f"अण् are: {get_pratyAhAra_varNa('अण्')}")
# print(f"अण् are: {get_pratyAhAra_varNa('अण्', 1)}")

################################################################################
# ५ ऊकालोऽज्झ्रस्वदीर्घप्लुतः [१.२.२७ ]
# ६ उच्चैरुदात्तः [१.२.२९ ]
# ७ नीचैरनुदात्तः [१.२.३० ]
# ८ समाहारः स्वरितः [१.२.३१ ]

hrasva_svara_varNa = ['अ', 'इ', 'उ', 'ऋ', 'ऌ', None, None, None, None]
dIrgha_svara_varNa = ['आ', 'ई', 'ऊ', 'ॠ', None, 'ए', 'ऐ', 'ओ', 'औ']
# Letter ३ is appended to each pluta svara
pluta_svara_varNa = list(hrasva_svara_varNa[:5]) + list(dIrgha_svara_varNa[5:])

def get_hrasvadIrghapluta_bheda(varNa):
    bheda = []
    if (varNa[0] in pluta_svara_varNa) and (varNa[-1] == '३'):
        bheda.append("प्लुत")
    elif (varNa[0] in hrasva_svara_varNa):
        bheda.append("ह्रस्व")
    elif (varNa[0] in dIrgha_svara_varNa):
        bheda.append("दीर्घ")
    return bheda

anudAtta_rekhA = (b'\xe0\xa5\x92').decode("utf-8")
svarita_rekhA = (b'\xe0\xa5\x91').decode("utf-8")

def get_udAttaanudAttasvarita_bheda(varNa):
    bheda = []
    if (varNa[0] in hrasva_svara_varNa or varNa[0] in dIrgha_svara_varNa or varNa[0] in pluta_svara_varNa):
        if (len(varNa) > 1) and (varNa[1] == anudAtta_rekhA):
            bheda.append("अनुदात्त")
        elif (len(varNa) > 2) and (varNa[2] == anudAtta_rekhA):
            bheda.append("अनुदात्त")
        elif (len(varNa) > 1) and (varNa[1] == svarita_rekhA):
            bheda.append("स्वरित")
        elif (len(varNa) > 2) and (varNa[2] == svarita_rekhA):
            bheda.append("स्वरित")
        else:
            bheda.append("उदात्त")
    return bheda

anunAsika_chandrabindu = (b'\xe0\xa4\x81').decode("utf-8")

def get_anunAsikaniranunAsika_bheda(varNa):
    bheda = []
    if (varNa[0] in hrasva_svara_varNa or varNa[0] in dIrgha_svara_varNa or varNa[0] in pluta_svara_varNa or varNa[0] in ['य', 'व', 'ल']):
        if (len(varNa) > 1) and (varNa[1] == anunAsika_chandrabindu):
            bheda.append("अनुनासिक")
        else:    
            bheda.append("निरनुनासिक")
    return bheda

# test_varNa = ['इ', 'आ॒', 'एँ३', 'ऊ॑', 'ऋँ॒', 'अँ३', 'ॠ॑', 'ओँ॒', 'ऌ॑३', 'ऐ', 'क', 'व', 'यँ']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_hrasvadIrghapluta_bheda(varNa), end=' ')
#     print(get_udAttaanudAttasvarita_bheda(varNa), end=' ')
#     print(get_anunAsikaniranunAsika_bheda(varNa), end=' ')
#     print()

def get_hrasvadIrghapluta_svara(varNa):
    svara = []
    varNa_index = -1

    if (varNa[0] in hrasva_svara_varNa):
        varNa_index = hrasva_svara_varNa.index(varNa[0])
    elif (varNa[0] in dIrgha_svara_varNa):
        varNa_index = dIrgha_svara_varNa.index(varNa[0])
    elif (varNa[0] in pluta_svara_varNa):
        varNa_index = pluta_svara_varNa.index(varNa[0])
    
    if (varNa_index != -1):
        if (hrasva_svara_varNa[varNa_index]):
            v = hrasva_svara_varNa[varNa_index]
            svara.append(v)
        if (dIrgha_svara_varNa[varNa_index]):
            v = dIrgha_svara_varNa[varNa_index]
            svara.append(v)
        if (pluta_svara_varNa[varNa_index]):
            v = pluta_svara_varNa[varNa_index]
            svara.append(v + '३')
    return svara

def get_all_svara(varNa):
    svara = []
    varNa_index = -1

    # Get index of svara 
    if (varNa[0] in hrasva_svara_varNa):
        varNa_index = hrasva_svara_varNa.index(varNa[0])
    elif (varNa[0] in dIrgha_svara_varNa):
        varNa_index = dIrgha_svara_varNa.index(varNa[0])
    
    if (varNa_index != -1):
        if (hrasva_svara_varNa[varNa_index]):
            v = hrasva_svara_varNa[varNa_index]
            svara.append(v)
            svara.append(v + anunAsika_chandrabindu)
            svara.append(v + anudAtta_rekhA)
            svara.append(v + anunAsika_chandrabindu + anudAtta_rekhA)
            svara.append(v + svarita_rekhA)
            svara.append(v + anunAsika_chandrabindu + svarita_rekhA)
        if (dIrgha_svara_varNa[varNa_index]):
            v = dIrgha_svara_varNa[varNa_index]
            svara.append(v)
            svara.append(v + anunAsika_chandrabindu)
            svara.append(v + anudAtta_rekhA)
            svara.append(v + anunAsika_chandrabindu + anudAtta_rekhA)
            svara.append(v + svarita_rekhA)
            svara.append(v + anunAsika_chandrabindu + svarita_rekhA)
        if (pluta_svara_varNa[varNa_index]):
            v = pluta_svara_varNa[varNa_index]
            svara.append(v + '३')
            svara.append(v + anunAsika_chandrabindu + '३')
            svara.append(v + anudAtta_rekhA + '३')
            svara.append(v + anunAsika_chandrabindu + anudAtta_rekhA + '३')
            svara.append(v + svarita_rekhA + '३')
            svara.append(v + anunAsika_chandrabindu + svarita_rekhA + '३')
    return svara

# test_svara_varNa = ['इ', 'आ॒', 'एँ३', 'ऊ॑', 'ऋँ॒', 'अँ३', 'ॠ॑', 'ओँ॒', 'ऌ॑३', 'ऐ']
# for varNa in test_svara_varNa:
#     print(varNa, end=' ')
#     # print(get_hrasvadIrghapluta_svara(varNa), end=' ')
#     print(get_all_svara(varNa), end=' ')
#     print()

def get_distinct_svara(varNa):
    svara = []
    varNa_index = -1

    # Get index of svara 
    if (varNa[0] in hrasva_svara_varNa):
        varNa_index = hrasva_svara_varNa.index(varNa[0])
    elif (varNa[0] in dIrgha_svara_varNa):
        varNa_index = dIrgha_svara_varNa.index(varNa[0])
    
    if (varNa_index != -1):
        if (hrasva_svara_varNa[varNa_index]):
            v = hrasva_svara_varNa[varNa_index]
            svara.append(v)
        if (dIrgha_svara_varNa[varNa_index]):
            v = dIrgha_svara_varNa[varNa_index]
            svara.append(v)
    return svara

# test_svara_varNa = ['इ', 'आ॒', 'एँ३', 'ऊ॑', 'ऋँ॒', 'अँ३', 'ॠ॑', 'ओँ॒', 'ऌ॑३', 'ऐ']
# for varNa in test_svara_varNa:
#     print(varNa, end=' ')
#     print(get_distinct_svara(varNa), end=' ')
#     print()

################################################################################
# १० तुल्यास्यप्रयत्नं सवर्णम् [ १.१.९ ]

ku_varga_varNa = ['क', 'ख', 'ग', 'घ', 'ङ']
chu_varga_varNa = ['च', 'छ', 'ज', 'झ', 'ञ']
Tu_varga_varNa = ['ट', 'ठ', 'ड', 'ढ', 'ण']
tu_varga_varNa = ['त', 'थ', 'द', 'ध', 'न']
pu_varga_varNa = ['प', 'फ', 'ब', 'भ', 'म']

# कण्ठ्याः - अ (स्वराः - अकारस्य अष्टादश भेदाः) + कु (वर्गीयाः) + ह (उष्माणः) + विसर्गः (अयोगवाहाः)
kaNTha_varNa = get_distinct_svara('अ') + ku_varga_varNa + ['ह']
# तालव्याः - इ (स्वराः - इकारस्य अष्टादश भेदाः) + चु (वर्गीयाः) + य (अन्तःस्थाः) + श (उष्माणः)
tAlu_varNa = get_distinct_svara('इ') + chu_varga_varNa + ['य', 'श']
# मूर्धन्याः - ऋ (स्वराः - ऋकारस्य अष्टादश भेदाः) + टु (वर्गीयाः) + र (अन्तःस्थाः) + ष (उष्माणः)
mUrdhA_varNa = get_distinct_svara('ऋ') + Tu_varga_varNa + ['र', 'ष']
# दन्त्याः - ऌ (स्वराः - ऌकारस्य द्वादश भेदाः) + तु (वर्गीयाः) + ल (अन्तःस्थाः) + स (उष्माणः)
danta_varNa = get_distinct_svara('ऌ') + tu_varga_varNa + ['ल', 'स']
# ओष्ठ्याः - उ (स्वराः - उकारस्य अष्टादश भेदाः) + पु (वर्गीयाः) + उपध्मानीयः (≍प≍फ - अयोगवाहाः)
oShTha_varNa = get_distinct_svara('उ') + pu_varga_varNa
# अनुनासिकाः - ञ म ङ ण न (वर्गीयाः)
anunAsika_varNa = pañchama_varga_varNa
# कण्ठ-तालव्यौ - ए (स्वराः - एकारस्य द्वादशभेदाः), ऐ (स्वराः - ऐकारस्य द्वादशभेदाः)
kaNThatAlu_varNa = get_distinct_svara('ए') + get_distinct_svara('ऐ')
# कण्ठ-ओष्ठ्यौ - ओ (स्वराः - ओकारस्य द्वादशभेदाः), औ (स्वराः - औकारस्य द्वादशभेदाः)
kaNThoShTha_varNa = get_distinct_svara('ओ') + get_distinct_svara('औ')
# दन्त-ओष्ठ्यः व् (अन्तःस्थाः)
dantoShTha_varNa = ['व']

def get_uchchAraNasthAna(varNa):
    sthAna = []
    if (varNa[0] in kaNTha_varNa):
        sthAna.append("कण्ठ")
    if (varNa[0] in tAlu_varNa):
        sthAna.append("तालु")
    if (varNa[0] in mUrdhA_varNa):
        sthAna.append("मूर्धा")
    if (varNa[0] in danta_varNa):
        sthAna.append("दन्त")
    if (varNa[0] in oShTha_varNa):
        sthAna.append("ओष्ठ")
    if (varNa[0] in anunAsika_varNa):
        sthAna.append("अनुनासिक")
    if (varNa[0] in kaNThatAlu_varNa):
        sthAna.append("कण्ठतालु")
    if (varNa[0] in kaNThoShTha_varNa):
        sthAna.append("कण्ठोष्ठ")
    if (varNa[0] in dantoShTha_varNa):
        sthAna.append("दन्तोष्ठ")
    return sthAna

# Identify उच्चारणस्थान for given varNa
# test_varNa = ['ड्', 'छ्', 'ऋ', 'ऌ', 'भ्', 'ऐ', 'ङ्', 'ह्', 'व्', 'औ', 'ख्', 'ष्', 'म्', 'स्', 'य्']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_uchchAraNasthAna(varNa))

spRRiShTa_varNa = vyañjana_varga_varNa
IShatspRRiShTa_varNa = antaHstha_varNa
IShadvivRRita_varNa = uShmANa_varNa
vivRRita_varNa = svara_varNa
saMvRRita_varNa = ['अ'] 

def get_Abhyantaraprayatna(varNa):
    prayatna = []
    if (varNa[0] in spRRiShTa_varNa):
        prayatna.append("स्पृष्ट")
    if (varNa[0] in IShatspRRiShTa_varNa):
        prayatna.append("ईषत्स्पृष्ट")
    if (varNa[0] in IShadvivRRita_varNa):
        prayatna.append("ईषद्विवृत")
    if (varNa[0] in vivRRita_varNa):
        prayatna.append("विवृत")
    if (varNa[0] in saMvRRita_varNa):
        prayatna.append("संवृत")
    return prayatna

# Identify आभ्यन्तरप्रयत्न for given varNa
# test_varNa = ['ष्', 'झ्', 'ल्', 'ठ्', 'य्', 'ऐ', 'स्', 'ऌ', 'अ', 'प्']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_Abhyantaraprayatna(varNa))

vivAra_shvAsa_aghoSha_varNa = get_pratyAhAra_varNa('खर्')
saMvAra_nAda_ghoSha_varNa = get_pratyAhAra_varNa('हश्')
alpaprANa_varNa = prathama_varga_varNa + tRRitIya_varga_varNa + pañchama_varga_varNa + get_pratyAhAra_varNa('यण्')
mahAprANa_varNa = dvitIya_varga_varNa + chaturtha_varga_varNa + get_pratyAhAra_varNa('शल्')

def get_bAhyaprayatna(varNa):
    prayatna = []
    if (varNa[0] in vivAra_shvAsa_aghoSha_varNa):
        prayatna.append("विवार श्वास अघोष")
    if (varNa[0] in saMvAra_nAda_ghoSha_varNa):
        prayatna.append("संवार नाद घोष")
    if (varNa[0] in alpaprANa_varNa):
        prayatna.append("अल्पप्राण")
    if (varNa[0] in mahAprANa_varNa):
        prayatna.append("महाप्राण")
    prayatna.extend(get_udAttaanudAttasvarita_bheda(varNa))
    return prayatna

# Identify बाह्यप्रयत्न for given varNa
# test_varNa = ['ह्', 'स्', 'इ॑', 'ख्', 'ए', 'ष्', 'ल्', 'ञ्', 'य्', 'ण्']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_bAhyaprayatna(varNa))

################################################################################
# ११ अणुदित् सवर्णस्य चाप्रत्ययः [१.१.६९ ]

def get_savarNa_bheda(varNa):
    bheda = []

    # Check for udit varNa - 'कुँ', 'चुँ', 'टुँ', 'तुँ', 'पुँ'
    if (varNa[0] in ku_varga_varNa):
        bheda.append("कुँ")
    elif (varNa[0] in chu_varga_varNa):
        bheda.append("चुँ")
    elif (varNa[0] in Tu_varga_varNa):
        bheda.append("टुँ")
    elif (varNa[0] in tu_varga_varNa):
        bheda.append("तुँ")
    elif (varNa[0] in pu_varga_varNa):
        bheda.append("पुँ")
    else:
        # Check for aN varNa - अ, इ, उ, ऋ, ऌ, ए, ओ, ऐ, औ, ह, य, व, र, ल 
        aN_varNa = get_pratyAhAra_varNa('अण्', 1)
        # if it is in अ, इ, उ types
        if (av_list := [av for av in aN_varNa[:3] if varNa[0] in get_distinct_svara(av)]):
            bheda.extend(av_list)
        # if it is in ऋ, ऌ types
        elif (av_list := [av for av in aN_varNa[3:5] if varNa[0] in get_distinct_svara(av)]):
            bheda.extend(aN_varNa[3:5])
        # if it is in remaining अण् types
        elif (varNa[0] in aN_varNa[5:]):
            bheda.append(varNa[0])
        # Return same as input    
        else:
            bheda.append(varNa)
    return bheda

# Identify whether letters in following pairs are savarṇas of each other:
# test_varNa = [
#     ['उ', 'ऊँ'], ['ऋ', 'श्'], ['म्', 'प्'], ['ओ', 'औ'], ['अ', 'इ'], 
#     ['ट्', 'ष्'], ['ङ्', 'ञ्'], ['ज्', 'छ्'], ['ॠ', 'ऌ'], ['भ्', 'उ'], 
#     ['ष', 'षँ'], ['य', 'यँ']]
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     if (get_savarNa_bheda(varNa[0]) == get_savarNa_bheda(varNa[1])):
#         print('आम्')
#     else:
#         print('न')

def get_savarNa_varNa(varNa):
    savarNa_varNa = []
    # Check for udit varNa - 'कुँ', 'चुँ', 'टुँ', 'तुँ', 'पुँ'
    if (varNa == 'कुँ'):
        savarNa_varNa.extend(ku_varga_varNa)
    elif (varNa == 'चुँ'):
        savarNa_varNa.extend(chu_varga_varNa)
    elif (varNa == 'टुँ'):
        savarNa_varNa.extend(Tu_varga_varNa)
    elif (varNa == 'तुँ'):
        savarNa_varNa.extend(tu_varga_varNa)
    elif (varNa == 'पुँ'):
        savarNa_varNa.extend(pu_varga_varNa)
    else:
        aN_varNa = get_pratyAhAra_varNa('अण्', 1)
        # Check for aN varNa - अ, इ, उ, ऋ, ऌ, ए, ओ, ऐ, औ, ह, य, व, र, ल 
        if (varNa in aN_varNa[:3]): # if it is in अ, इ, उ
            savarNa_varNa.extend(get_distinct_svara(varNa))
        elif (varNa in aN_varNa[3:5]): # if it is in ऋ, ऌ
            savarNa_varNa.extend(get_distinct_svara(aN_varNa[3]))
            savarNa_varNa.extend(get_distinct_svara(aN_varNa[4]))
        elif (varNa in aN_varNa[5:]): # if it is in remaining अण्
            if (varNa == 'य') or (varNa == 'व') or (varNa == 'ल'):
                savarNa_varNa.extend([varNa, varNa + anunAsika_chandrabindu])
            else:
                savarNa_varNa.extend([varNa])
        else:
            # Return same as input    
            savarNa_varNa.append(varNa)
    return savarNa_varNa

# Identify which letters are represented by following
# test_varNa = ['चुँ', 'औ', 'य', 'क', 'ऌ', 'उ', 'तुँ', 'ठ', 'अ', 'फ', 'आ']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_savarNa_varNa(varNa))

################################################################################
