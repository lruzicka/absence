#!/usr/bin/python

import csv

print('Třídič propadlíků')

CJ = []
AJ = []
NJ = []
M = []
ON = []
TV = []
BIO = []
CH = []
HYD = []
GEO = []
OZP = []
PP = []
VT = []
EKO = []
SAZ = []
OVO = []
OAO = []
PRX = []

OZ = []
ICT = []
EKP = []
MV = []
PRO = []
CHZ = []
OTK = []
OK = []
SUS = []
AGR = []
PRX = []

uCJ = []
uAJ = []
uNJ = []
uM = []
uON = []
uTV = []
uBIO = []
uCH = []
uHYD = []
uGEO = []
uOZP = []
uPP = []
uVT = []
uEKO = []
uSAZ = []
uOVO = []
uOAO = []
uPRX = []

uOZ = []
uICT = []
uEKP = []
uMV = []
uPRO = []
uCHZ = []
uOTK = []
uOK = []
uSUS = []
uAGR = []
uPRX = []

ordFail = {}
ordUnc = {}
wFail = {}
wUnc = {}

run = input('Kde je soubor?: ')
deli = input('Jakým znakem jsou data oddělena?: ')
fileLines = csv.reader(open(run,mode='r'),delimiter=deli)

recs = []
for line in fileLines:
    recs.append(line)


for item in recs:
    name,fail,unclass = item
    fail = fail.split(',')
    unclass = unclass.split(',')
    cFail = len(fail)
    cUnc = len(unclass)

    ordFail[name] = cFail
    ordUnc[name] = cUnc

    wFail[name] = fail
    wUnc[name] = unclass

    if 'cj' in fail:
        CJ.append(name)
    if 'aj' in fail:
        AJ.append(name)
    if 'nj' in fail:
        NJ.append(name)
    if 'm' in fail:
        M.append(name)
    if 'on' in fail:
        ON.append(name)
    if 'tv' in fail:
        TV.append(name)
    if 'bio' in fail:
        BIO.append(name)
    if 'ch' in fail:
        CH.append(name)
    if 'hyd' in fail:
        HYD.append(name)
    if 'geo' in fail:
        GEO.append(name)
    if 'ozp' in fail:
        OZP.append(name)
    if 'pp' in fail:
        PP.append(name)
    if 'vt' in fail:
        VT.append(name)
    if 'eko' in fail:
        EKO.append(name)
    if 'saz' in fail:
        SAZ.append(name)
    if 'ovo' in fail:
        OVO.append(name)
    if 'oao' in fail:
        OAO.append(name)
    if 'prx' in fail:
        PRX.append(name)
    if 'oz' in fail:
        OZ.append(name)
    if 'ict' in fail:
        ICT.append(name)
    if 'ekp' in fail:
        EKP.append(name)
    if 'mv' in fail:
        MV.append(name)
    if 'pro' in fail:
        PRO.append(name)
    if 'chz' in fail:
        CHZ.append(name)
    if 'otk' in fail:
        OTK.append(name)
    if 'ok' in fail:
        OK.append(name)
    if 'sus' in fail:
        SUS.append(name)
    if 'agr' in fail:
        AGR.append(name)


    if 'cj' in unclass:
        uCJ.append(name)
    if 'aj' in unclass:
        uAJ.append(name)
    if 'nj' in unclass:
        uNJ.append(name)
    if 'm' in unclass:
        uM.append(name)
    if 'on' in unclass:
        uON.append(name)
    if 'tv' in unclass:
        uTV.append(name)
    if 'bio' in unclass:
        uBIO.append(name)
    if 'ch' in unclass:
        uCH.append(name)
    if 'hyd' in unclass:
        uHYD.append(name)
    if 'geo' in unclass:
        uGEO.append(name)
    if 'ozp' in unclass:
        uOZP.append(name)
    if 'pp' in unclass:
        uPP.append(name)
    if 'vt' in unclass:
        uVT.append(name)
    if 'eko' in unclass:
        uEKO.append(name)
    if 'saz' in unclass:
        uSAZ.append(name)
    if 'ovo' in unclass:
        uOVO.append(name)
    if 'oao' in unclass:
        uOAO.append(name)
    if 'prx' in unclass:
        uPRX.append(name)
    if 'oz' in unclass:
        uOZ.append(name)
    if 'ict' in unclass:
        uICT.append(name)
    if 'ekp' in unclass:
        uEKP.append(name)
    if 'mv' in unclass:
        uMV.append(name)
    if 'pro' in unclass:
        uPRO.append(name)
    if 'chz' in unclass:
        uCHZ.append(name)
    if 'otk' in unclass:
        uOTK.append(name)
    if 'ok' in unclass:
        uOK.append(name)
    if 'sus' in unclass:
        uSUS.append(name)
    if 'agr' in unclass:
        uAGR.append(name)
    
print('Propadli:')
print('Český jazyk: ')
for name in CJ:
    print(name)
print(' ')

print('Anglický jazyk: ')
for name in AJ:
    print(name)
print(' ')

print('Německý jazyk: ')
for name in NJ:
    print(name)
print(' ')

print('Matematika: ')
for name in M:
    print(name)
print(' ')

print('Občanská nauka: ')
for name in ON:
    print(name)
print(' ')

print('Tělocvik: ')
for name in TV:
    print(name)
print(' ')

print('Biologie: ')
for name in BIO:
    print(name)
print(' ')

print('Chemie: ')
for name in CH:
    print(name)
print(' ')

print('Hydrologie: ')
for name in HYD:
    print(name)
print(' ')

print('Geologie: ')
for name in GEO:
    print(name)
print(' ')

print('Ochrana životního prostředí: ')
for name in OZP:
    print(name)
print(' ')

print('Právní příprava: ')
for name in PP:
    print(name)
print(' ')

print('Výpočetní technika: ')
for name in VT:
    print(name)
print(' ')

print('Ekonomika: ')
for name in EKO:
    print(name)
print(' ')

print('Stroje a zařízení: ')
for name in SAZ:
    print(name)
print(' ')

print('Ochrana vody: ')
for name in OVO:
    print(name)
print(' ')

print('Odpady a ovzduší: ')
for name in OAO:
    print(name)
print(' ')

print('Praxe: ')
for name in PRX:
    print(name)
print(' ')

print('Občanský základ: ')
for name in OZ:
    print(name)
print(' ')

print('Informatika: ')
for name in ICT:
    print(name)
print(' ')

print('Ekonomie podnikání: ')
for name in EKP:
    print(name)
print(' ')

print('Motorová vozidla: ')
for name in MV:
    print(name)
print(' ')

print('Pěstování rostlin: ')
for name in PRO:
    print(name)
print(' ')

print('Chov zvířat: ')
for name in CHZ:
    print(name)
print(' ')

print('Ochrana a tvorba krajiny: ')
for name in OTK:
    print(name)
print(' ')

print('Obchodní korespondence: ')
for name in OK:
    print(name)
print(' ')

print('Stravovací a ubytovací služby: ')
for name in SUS:
    print(name)
print(' ')

print('Agropodnikání: ')
for name in AGR:
    print(name)


print('Neklasifikováni:')
print('Český jazyk: ')
for name in uCJ:
    print(name)
print(' ')

print('Anglický jazyk: ')
for name in uAJ:
    print(name)
print(' ')

print('Německý jazyk: ')
for name in uNJ:
    print(name)
print(' ')

print('Matematika: ')
for name in uM:
    print(name)
print(' ')

print('Občanská nauka: ')
for name in uON:
    print(name)
print(' ')

print('Tělocvik: ')
for name in uTV:
    print(name)
print(' ')

print('Biologie: ')
for name in uBIO:
    print(name)
print(' ')

print('Chemie: ')
for name in uCH:
    print(name)
print(' ')

print('Hydrologie: ')
for name in uHYD:
    print(name)
print(' ')

print('Geologie: ')
for name in uGEO:
    print(name)
print(' ')

print('Ochrana životního prostředí: ')
for name in uOZP:
    print(name)
print(' ')

print('Právní příprava: ')
for name in uPP:
    print(name)
print(' ')

print('Výpočetní technika: ')
for name in uVT:
    print(name)
print(' ')

print('Ekonomika: ')
for name in uEKO:
    print(name)
print(' ')

print('Stroje a zařízení: ')
for name in uSAZ:
    print(name)
print(' ')

print('Ochrana vody: ')
for name in uOVO:
    print(name)
print(' ')

print('Odpady a ovzduší: ')
for name in uOAO:
    print(name)
print(' ')

print('Praxe: ')
for name in uPRX:
    print(name)
print(' ')

print('Občanský základ: ')
for name in uOZ:
    print(name)
print(' ')

print('Informatika: ')
for name in uICT:
    print(name)
print(' ')

print('Ekonomie podnikání: ')
for name in uEKP:
    print(name)
print(' ')

print('Motorová vozidla: ')
for name in uMV:
    print(name)
print(' ')

print('Pěstování rostlin: ')
for name in uPRO:
    print(name)
print(' ')

print('Chov zvířat: ')
for name in uCHZ:
    print(name)
print(' ')

print('Ochrana a tvorba krajiny: ')
for name in uOTK:
    print(name)
print(' ')

print('Obchodní korespondence: ')
for name in uOK:
    print(name)
print(' ')

print('Stravovací a ubytovací služby: ')
for name in uSUS:
    print(name)
print(' ')

print('Agropodnikání: ')
for name in uAGR:
    print(name)

print(' ')
print('Celkový počet nedostatečných (dle žáků)\n')
failedList = []
for item in ordFail.items():
    name,numb = item
    what = wFail[name]
    rec = [numb,name,what]
    failedList.append(rec)

failedList.sort(reverse=True)
for i in failedList:
    numb,name,what = i
    print(name,numb,what)

print(' ')
print('Celkový počet neklasifikací (dle žáků)\n')
failedList = []
for item in ordUnc.items():
    name,numb = item
    what = wUnc[name]
    rec = [numb,name,what]
    failedList.append(rec)

failedList.sort(reverse=True)
for i in failedList:
    numb,name,what = i
    print(name,numb,what)

print('Konec')
