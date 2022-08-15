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

# Generate grapheme clusters for string s
import unicodedata
def get_split_cluster(s):
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

# print(list(get_split_cluster("ऋग्वेदसंहितायां प्रथमं मण्डलम्")))

def get_pratyAhAra_varNa(pratyAhAra, occurrence_index = 0):
    split_cluster = list(get_split_cluster(pratyAhAra))
    start_flag = False
    pratyAhAra_varNa = []
    oindex = 0

    for i, msUtra in enumerate(mAheshvara_sUtra):
        for varNa in msUtra:
            if start_flag == False:                
                if varNa == split_cluster[0]:
                    start_flag = True
                    v = varNa
                    if (i > 3):
                        v += chr(0x094d)
                    pratyAhAra_varNa.append(v)
            else:
                if varNa != msUtra[-1]:
                    v = varNa
                    if (i > 3):
                        v += chr(0x094d)
                    if v not in pratyAhAra_varNa:
                        pratyAhAra_varNa.append(v)
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
# print(svara_varNa)
# print(vyañjana_varNa)
# print(antaHstha_varNa)
# print(pañchama_varga_varNa)
# print(chaturtha_varga_varNa)
# print(tRRitIya_varga_varNa)
# print(dvitIya_varga_varNa)
# print(prathama_varga_varNa)
# print(uShmANa_varNa)
# print(mRRiduvyañjana_varNa)
# print(karkashavyañjana_varNa)

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
pluta_svara_varNa = [i for i in list(hrasva_svara_varNa[:5]) + list(dIrgha_svara_varNa[5:])] 

# print(hrasva_svara_varNa)
# print(dIrgha_svara_varNa)
# print(pluta_svara_varNa)

unique_svara_varNa = [x for y in zip(hrasva_svara_varNa, dIrgha_svara_varNa) for x in y if x]
mAtrA_svara_varNa = [
    None, chr(0x093E), chr(0x093F), chr(0x0940), chr(0x0941), chr(0x0942), 
    chr(0x0943), chr(0x0944), chr(0x0962), chr(0x0947), chr(0x0948), 
    chr(0x094B), chr(0x094C)] 

def get_svara_from_mAtrA(mAtrA):
    svara = None
    if mAtrA in mAtrA_svara_varNa:
        mindex = mAtrA_svara_varNa.index(mAtrA)
        svara = unique_svara_varNa[mindex]
    return svara

def get_mAtrA_from_svara(svara):
    mAtrA = None
    if svara in unique_svara_varNa:
        sindex = unique_svara_varNa.index(svara)
        mAtrA = mAtrA_svara_varNa[sindex]
    return mAtrA

anudAtta_rekhA = chr(0x0952)
svarita_rekhA = chr(0x0951)
anunAsika_chandrabindu = chr(0x0901)
virAma_chinha = chr(0x094d)

# print(anudAtta_rekhA)
# print(svarita_rekhA)
# print(anunAsika_chandrabindu)

hrasva_svara_all = [x for y in hrasva_svara_varNa if y for x in [
    y,
    y+anudAtta_rekhA,
    y+svarita_rekhA,
    y+anunAsika_chandrabindu, 
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
dIrgha_svara_all = [x for y in dIrgha_svara_varNa if y for x in [
    y,
    y+anudAtta_rekhA,
    y+svarita_rekhA,
    y+anunAsika_chandrabindu, 
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
pluta_svara_all = [x+'३' for y in pluta_svara_varNa if y for x in [
    y,
    y+anudAtta_rekhA,
    y+svarita_rekhA,
    y+anunAsika_chandrabindu, 
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]

svara_varNa_all = hrasva_svara_all+dIrgha_svara_all+pluta_svara_all

# print(hrasva_svara_all)
# print(dIrgha_svara_all)
# print(pluta_svara_all)
# print(len(hrasva_svara_all+dIrgha_svara_all+pluta_svara_all))

hrasva_svara_udAtta = [x for y in hrasva_svara_varNa if y for x in [
    y,
    y+anunAsika_chandrabindu, 
    ]]
dIrgha_svara_udAtta = [x for y in dIrgha_svara_varNa if y for x in [
    y,
    y+anunAsika_chandrabindu, 
    ]]
pluta_svara_udAtta = [x+'३' for y in pluta_svara_varNa if y for x in [
    y,
    y+anunAsika_chandrabindu, 
    ]]
udAtta_svara_all = hrasva_svara_udAtta + dIrgha_svara_udAtta + pluta_svara_udAtta

hrasva_svara_anudAtta = [x for y in hrasva_svara_varNa if y for x in [
    y+anudAtta_rekhA,
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    ]]
dIrgha_svara_anudAtta = [x for y in dIrgha_svara_varNa if y for x in [
    y+anudAtta_rekhA,
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    ]]
pluta_svara_anudAtta = [x+'३' for y in pluta_svara_varNa if y for x in [
    y+anudAtta_rekhA,
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    ]]
anudAtta_svara_all = hrasva_svara_anudAtta + dIrgha_svara_anudAtta + pluta_svara_anudAtta

hrasva_svara_svarita = [x for y in hrasva_svara_varNa if y for x in [
    y+svarita_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
dIrgha_svara_svarita = [x for y in dIrgha_svara_varNa if y for x in [
    y+svarita_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
pluta_svara_svarita = [x+'३' for y in pluta_svara_varNa if y for x in [
    y+svarita_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
svarita_svara_all = hrasva_svara_svarita + dIrgha_svara_svarita + pluta_svara_svarita

# print(udAtta_svara_all)
# print(anudAtta_svara_all)
# print(svarita_svara_all)
# print(len(udAtta_svara_all+anudAtta_svara_all+svarita_svara_all))

hrasva_svara_anunAsika = [x for y in hrasva_svara_varNa if y for x in [
    y+anunAsika_chandrabindu, 
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
dIrgha_svara_anunAsika = [x for y in dIrgha_svara_varNa if y for x in [
    y+anunAsika_chandrabindu, 
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
pluta_svara_anunAsika = [x+'३' for y in pluta_svara_varNa if y for x in [
    y+anunAsika_chandrabindu, 
    y+anunAsika_chandrabindu+anudAtta_rekhA,
    y+anunAsika_chandrabindu+svarita_rekhA,
    ]]
anunAsika_svara_all = hrasva_svara_anunAsika + dIrgha_svara_anunAsika + pluta_svara_anunAsika

hrasva_svara_niranunAsika = [x for y in hrasva_svara_varNa if y for x in [
    y,
    y+anudAtta_rekhA,
    y+svarita_rekhA,
    ]]
dIrgha_svara_niranunAsika = [x for y in dIrgha_svara_varNa if y for x in [
    y,
    y+anudAtta_rekhA,
    y+svarita_rekhA,
    ]]
pluta_svara_niranunAsika = [x+'३' for y in pluta_svara_varNa if y for x in [
    y,
    y+anudAtta_rekhA,
    y+svarita_rekhA,
    ]]
niranunAsika_svara_all = hrasva_svara_niranunAsika + dIrgha_svara_niranunAsika + pluta_svara_niranunAsika

# print(anunAsika_svara_all)
# print(niranunAsika_svara_all)
# print(len(anunAsika_svara_all+niranunAsika_svara_all))

def get_hrasvadIrghapluta_bheda(varNa):
    bheda = []

    if (varNa in hrasva_svara_all):
        bheda.append("ह्रस्व")
    elif (varNa in dIrgha_svara_all):
        bheda.append("दीर्घ")
    elif (varNa in pluta_svara_all):
        bheda.append("प्लुत")

    return bheda

def get_udAttaanudAttasvarita_bheda(varNa):
    bheda = []

    if (varNa in udAtta_svara_all):
        bheda.append("उदात्त")
    elif (varNa in anudAtta_svara_all):
        bheda.append("अनुदात्त")
    elif (varNa in svarita_svara_all):
        bheda.append("स्वरित")

    return bheda

def get_anunAsikaniranunAsika_bheda(varNa):
    bheda = []

    if (varNa in anunAsika_svara_all) or (varNa in ['य्ँ', 'व्ँ', 'ल्ँ']):
        bheda.append("अनुनासिक")
    elif (varNa in niranunAsika_svara_all) or (varNa in ['य्', 'व्', 'ल्']):
        bheda.append("निरनुनासिक")

    return bheda

def get_svara_bheda(varNa):
    return get_hrasvadIrghapluta_bheda(varNa) + get_udAttaanudAttasvarita_bheda(varNa) + get_anunAsikaniranunAsika_bheda(varNa)

# test_varNa = ['इ', 'आ॒', 'एँ३', 'ऊ॑', 'ऋँ॒', 'अँ३', 'ॠ॑', 'ओँ॒', 'ऌ॑३', 'ऐ', 'क्', 'व्', 'य्ँ']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_svara_bheda(varNa), end=' ')
#     print()

def get_hrasva_svara(varNa):
    varNa_index = -1

    # Get index of svara 
    if (varNa in hrasva_svara_varNa):
        varNa_index = hrasva_svara_varNa.index(varNa)
    elif (varNa in dIrgha_svara_varNa):
        varNa_index = dIrgha_svara_varNa.index(varNa)

    if varNa_index != -1:
        hrasva_svara = [x for y in [hrasva_svara_varNa[varNa_index]] if y for x in [
            y,
            y+anudAtta_rekhA,
            y+svarita_rekhA,
            y+anunAsika_chandrabindu, 
            y+anunAsika_chandrabindu+anudAtta_rekhA,
            y+anunAsika_chandrabindu+svarita_rekhA,
            ]]
    return hrasva_svara

def get_dIrgha_svara(varNa):
    varNa_index = -1

    # Get index of svara 
    if (varNa in hrasva_svara_varNa):
        varNa_index = hrasva_svara_varNa.index(varNa)
    elif (varNa in dIrgha_svara_varNa):
        varNa_index = dIrgha_svara_varNa.index(varNa)

    if varNa_index != -1:
        dIrgha_svara = [x for y in [dIrgha_svara_varNa[varNa_index]] if y for x in [
            y,
            y+anudAtta_rekhA,
            y+svarita_rekhA,
            y+anunAsika_chandrabindu, 
            y+anunAsika_chandrabindu+anudAtta_rekhA,
            y+anunAsika_chandrabindu+svarita_rekhA,
            ]]
    return dIrgha_svara

def get_pluta_svara(varNa):
    varNa_index = -1

    # Get index of svara 
    if (varNa in hrasva_svara_varNa):
        varNa_index = hrasva_svara_varNa.index(varNa)
    elif (varNa in dIrgha_svara_varNa):
        varNa_index = dIrgha_svara_varNa.index(varNa)

    if varNa_index != -1:
        pluta_svara = [x+'३' for y in [pluta_svara_varNa[varNa_index]] if y for x in [
            y,
            y+anudAtta_rekhA,
            y+svarita_rekhA,
            y+anunAsika_chandrabindu, 
            y+anunAsika_chandrabindu+anudAtta_rekhA,
            y+anunAsika_chandrabindu+svarita_rekhA,
            ]]
    return pluta_svara

def get_all_svara(varNa):
    return get_hrasva_svara(varNa) + get_dIrgha_svara(varNa) + get_pluta_svara(varNa)

def get_all_vyañjana(varNa):

    vyañjana = []

    if varNa in ['य्', 'य्ँ']:
        vyañjana.extend(['य्', 'य्ँ'])
    elif varNa in ['व्', 'व्ँ']:
        vyañjana.extend(['व्', 'व्ँ'])
    elif varNa in ['ल्', 'ल्ँ']:
        vyañjana.extend(['ल्', 'ल्ँ'])
    elif varNa in vyañjana_varNa:
        vyañjana.append(varNa)

    return vyañjana

# test_varNa = ['अ', 'ॠ', 'ऌ', 'ऐ', 'औ']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_all_svara(varNa), end=' ')
#     print()

################################################################################
# १० तुल्यास्यप्रयत्नं सवर्णम् [ १.१.९ ]

ku_varga_varNa = ['क्', 'ख्', 'ग्', 'घ्', 'ङ्']
chu_varga_varNa = ['च्', 'छ्', 'ज्', 'झ्', 'ञ्']
Tu_varga_varNa = ['ट्', 'ठ्', 'ड्', 'ढ्', 'ण्']
tu_varga_varNa = ['त्', 'थ्', 'द्', 'ध्', 'न्']
pu_varga_varNa = ['प्', 'फ्', 'ब्', 'भ्', 'म्']

# कण्ठ्याः - अ (स्वराः - अकारस्य अष्टादश भेदाः) + कु (वर्गीयाः) + ह (उष्माणः) + विसर्गः (अयोगवाहाः)
kaNTha_varNa = get_all_svara('अ') + ku_varga_varNa + ['ह्']
# तालव्याः - इ (स्वराः - इकारस्य अष्टादश भेदाः) + चु (वर्गीयाः) + य (अन्तःस्थाः) + श (उष्माणः)
tAlu_varNa = get_all_svara('इ') + chu_varga_varNa + ['य्', 'श्']
# मूर्धन्याः - ऋ (स्वराः - ऋकारस्य अष्टादश भेदाः) + टु (वर्गीयाः) + र (अन्तःस्थाः) + ष (उष्माणः)
mUrdhA_varNa = get_all_svara('ऋ') + Tu_varga_varNa + ['र्', 'ष्']
# दन्त्याः - ऌ (स्वराः - ऌकारस्य द्वादश भेदाः) + तु (वर्गीयाः) + ल (अन्तःस्थाः) + स (उष्माणः)
danta_varNa = get_all_svara('ऌ') + tu_varga_varNa + ['ल्', 'स्']
# ओष्ठ्याः - उ (स्वराः - उकारस्य अष्टादश भेदाः) + पु (वर्गीयाः) + उपध्मानीयः (≍प≍फ - अयोगवाहाः)
oShTha_varNa = get_all_svara('उ') + pu_varga_varNa
# अनुनासिकाः - ञ म ङ ण न (वर्गीयाः)
anunAsika_varNa = pañchama_varga_varNa
# कण्ठ-तालव्यौ - ए (स्वराः - एकारस्य द्वादशभेदाः), ऐ (स्वराः - ऐकारस्य द्वादशभेदाः)
kaNThatAlu_varNa = get_all_svara('ए') + get_all_svara('ऐ')
# कण्ठ-ओष्ठ्यौ - ओ (स्वराः - ओकारस्य द्वादशभेदाः), औ (स्वराः - औकारस्य द्वादशभेदाः)
kaNThoShTha_varNa = get_all_svara('ओ') + get_all_svara('औ')
# दन्त-ओष्ठ्यः व् (अन्तःस्थाः)
dantoShTha_varNa = ['व्']

def get_uchchAraNasthAna(varNa):
    sthAna = []
    if (varNa in kaNTha_varNa):
        sthAna.append("कण्ठ")
    if (varNa in tAlu_varNa):
        sthAna.append("तालु")
    if (varNa in mUrdhA_varNa):
        sthAna.append("मूर्धा")
    if (varNa in danta_varNa):
        sthAna.append("दन्त")
    if (varNa in oShTha_varNa):
        sthAna.append("ओष्ठ")
    if (varNa in anunAsika_varNa):
        sthAna.append("अनुनासिक")
    if (varNa in kaNThatAlu_varNa):
        sthAna.append("कण्ठतालु")
    if (varNa in kaNThoShTha_varNa):
        sthAna.append("कण्ठोष्ठ")
    if (varNa in dantoShTha_varNa):
        sthAna.append("दन्तोष्ठ")
    return sthAna

# Identify उच्चारणस्थान for given varNa
# test_varNa = ['ड्', 'छ्', 'ऋ', 'ऌ', 'भ्', 'ऐ॑', 'ङ्', 'ह्', 'व्', 'औँ॒', 'ख्', 'ष्', 'म्', 'स्', 'य्']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_uchchAraNasthAna(varNa))

spRRiShTa_varNa = vyañjana_varga_varNa
IShatspRRiShTa_varNa = antaHstha_varNa
IShadvivRRita_varNa = uShmANa_varNa
vivRRita_varNa = svara_varNa_all
saMvRRita_varNa = get_hrasva_svara('अ') 

def get_Abhyantaraprayatna(varNa):
    prayatna = []
    if (varNa in spRRiShTa_varNa):
        prayatna.append("स्पृष्ट")
    if (varNa in IShatspRRiShTa_varNa):
        prayatna.append("ईषत्स्पृष्ट")
    if (varNa in IShadvivRRita_varNa):
        prayatna.append("ईषद्विवृत")
    if (varNa in vivRRita_varNa):
        prayatna.append("विवृत")
    if (varNa in saMvRRita_varNa):
        prayatna.append("संवृत")
    return prayatna

# Identify आभ्यन्तरप्रयत्न for given varNa
# test_varNa = ['ष्', 'झ्', 'ल्', 'ठ्', 'य्', 'ऐ', 'स्', 'ऌ', 'अ॑', 'प्']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_Abhyantaraprayatna(varNa))

vivAra_shvAsa_aghoSha_varNa = get_pratyAhAra_varNa('खर्')
saMvAra_nAda_ghoSha_varNa = get_pratyAhAra_varNa('हश्')
alpaprANa_varNa = prathama_varga_varNa + tRRitIya_varga_varNa + pañchama_varga_varNa + get_pratyAhAra_varNa('यण्')
mahAprANa_varNa = dvitIya_varga_varNa + chaturtha_varga_varNa + get_pratyAhAra_varNa('शल्')

def get_bAhyaprayatna(varNa):
    prayatna = []
    if (varNa in vivAra_shvAsa_aghoSha_varNa):
        prayatna.append("विवार श्वास अघोष")
    if (varNa in saMvAra_nAda_ghoSha_varNa):
        prayatna.append("संवार नाद घोष")
    if (varNa in alpaprANa_varNa):
        prayatna.append("अल्पप्राण")
    if (varNa in mahAprANa_varNa):
        prayatna.append("महाप्राण")
    prayatna.extend(get_udAttaanudAttasvarita_bheda(varNa))
    return prayatna

# Identify बाह्यप्रयत्न for given varNa
# test_varNa = ['ह्', 'स्', 'इ॑', 'ख्', 'ए३', 'ष्', 'ल्', 'ञ्', 'य्', 'ण्']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     print(get_bAhyaprayatna(varNa))

################################################################################
# १० तुल्यास्यप्रयत्नं सवर्णम् [ १.१.९ ]
# ११ अणुदित् सवर्णस्य चाप्रत्ययः [१.१.६९ ]

def get_savarNa_bheda(varNa):
    bheda = []

    # Check for udit varNa - 'कुँ', 'चुँ', 'टुँ', 'तुँ', 'पुँ'
    if (varNa in ku_varga_varNa):
        bheda.append("कुँ")
    elif (varNa in chu_varga_varNa):
        bheda.append("चुँ")
    elif (varNa in Tu_varga_varNa):
        bheda.append("टुँ")
    elif (varNa in tu_varga_varNa):
        bheda.append("तुँ")
    elif (varNa in pu_varga_varNa):
        bheda.append("पुँ")
    else:
        # Check for aN varNa - अ, इ, उ, ऋ, ऌ, ए, ओ, ऐ, औ, ह्, य्, व्, र्, ल् 
        aN_varNa = get_pratyAhAra_varNa('अण्', 1)
        # if it is in अ, इ, उ types
        if (av_list := [av for av in aN_varNa[:3] if varNa in get_all_svara(av)]):
            bheda.extend(av_list)
        # if it is in ऋ, ऌ types
        elif (av_list := [av for av in aN_varNa[3:5] if varNa in get_all_svara(av)]):
            bheda.extend(aN_varNa[3:5])
        # if it is in ए, ओ, ऐ, औ, types
        elif (av_list := [av for av in aN_varNa[5:9] if varNa in get_all_svara(av)]):
            bheda.extend(av_list)
        # if it is in remaining अण् types
        elif (av_list := [av for av in aN_varNa[9:] if varNa in get_all_vyañjana(av)]):
            bheda.extend(av_list)
        # Return same as input    
        else:
            bheda.append(varNa)
    return bheda

# Identify whether letters in following pairs are savarṇas of each other:
# test_varNa = [
#     ['उ', 'ऊँ'], ['ऋ', 'श्'], ['म्', 'प्'], ['ओ', 'औ'], ['अ', 'इ'], 
#     ['ट्', 'ष्'], ['ङ्', 'ञ्'], ['ज्', 'छ्'], ['ॠ', 'ऌ'], ['भ्', 'उ'], 
#     ['ष्', 'ष्ँ'], ['य्', 'य्ँ'], ['ओ', 'ओ॑']]
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
        # Check for aN varNa - अ, इ, उ, ऋ, ऌ, ए, ओ, ऐ, औ, ह्, य्, व्, र्, ल् 
        if (varNa in aN_varNa[:3]): # if it is in अ, इ, उ
            savarNa_varNa.extend(get_all_svara(varNa))
        elif (varNa in aN_varNa[3:5]): # if it is in ऋ, ऌ
            savarNa_varNa.extend(get_all_svara(aN_varNa[3]))
            savarNa_varNa.extend(get_all_svara(aN_varNa[4]))
        elif (varNa in aN_varNa[5:9]): # if it is in ए, ओ, ऐ, औ
            savarNa_varNa.extend(get_all_svara(varNa))
        elif (varNa in aN_varNa[9:]): # if it is in remaining अण्
            savarNa_varNa.extend(get_all_vyañjana(varNa))
        else:
            # Return same as input    
            savarNa_varNa.append(varNa)
    return savarNa_varNa

# Identify which letters are represented by following
# test_varNa = ['चुँ', 'औ', 'य्', 'क्', 'ऌ', 'उ', 'तुँ', 'ठ्', 'अ', 'फ्', 'आ']
# for varNa in test_varNa:
#     print(varNa, end=' ')
#     varNa_list = get_savarNa_varNa(varNa)
#     print(len(varNa_list), end=' ')
#     print(varNa_list)

################################################################################
