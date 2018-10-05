import random
import matplotlib.pyplot as plt
import numpy as np


#=====
#possible positive matches - on the right: actual vocalic pattern (A = stressed front vowel, U = stressed back vowel),
#on the left: possible transcription patterns in group writing according to my system (W = presence of w, Ꜣ/0 = absence of w)

#possible matches for 2-consonants words
#note 1: separator = tab ( = '\t' )
#note 2: preconsonatal r and n have been ignored, counted as 1 with the following consonant

matches_string_2 = \
'cAc	cꜢ/0c\n\
ccA	ccꜢ/0\n\
cA/Uc	cꜢ/0c\n\
ccA/U	ccꜢ/0\n\
cUc	cWc\n\
cUc	ccW\n\
cUc cWcW\n\
ccU	ccW\n\
cA/Uc	cWc\n\
cA/Uc	ccW\n\
cA/Uc cWcW\n\
ccA/U	ccW'

#possible matches for 3-consonants words
#note 1: separator = tab ( = '\t' )
#note 2: preconsonatal r and n have been ignored, counted as 1 with the following consonant

matches_string_3 = \
'cAcc	cꜢ/0cc\n\
ccAc	ccꜢ/0c\n\
cccA	cccꜢ/0\n\
cA/Ucc	cꜢ/0cc\n\
ccA/Uc	ccꜢ/0c\n\
cccA/U	cccꜢ/0\n\
cUcc	cWcc\n\
cUcc	ccWc\n\
cUcc	cWcWc\n\
ccUc	ccWc\n\
ccUc	cccW\n\
ccUc	ccWcW\n\
cccU	cccW\n\
cA/Ucc	cWcc\n\
cA/Ucc	ccWc\n\
cA/Ucc	cWcWc\n\
ccA/Uc	ccWc\n\
ccA/Uc	cccW\n\
ccA/Uc	ccWcW\n\
cccA/U	cccW'

#data extracted from the corpus.
#In each line:
# 1) reconstructed vocalisation (A = stressed front vowel, U = stressed back vowel),
# 2) transcription of the group writing spelling (W = presence of w, Ꜣ/0 = absence of w)
# 3) nr of consonats
# 4) period of the attestation
#
#note 1: separator = tab ( = '\t' )
#note 2: preconsonatal r and n have been ignored, counted as 1 with the following consonant

data_string = \
"cAc	cꜢ/0c	2	period 1	*y'am	I.2	\n\
cAc	cꜢ/0c	2	period 1	*b'ar(yv)	I.4	\n\
cA/Uc	cꜢ/0c	2	period 1	*b'i:/u:sv	I.5	\n\
cUc	ccW	2	period 1	*murḥv	I.6	\n\
cA/Uc	cꜢ/0c	2	period 1	*h'i/uy	I.10	\n\
cA/Uc	ccW	2	period 1	*h'i/up	I.11	\n\
cUc	ccW	2	period 1	*ḫur(r)v	I.14	\n\
cUc	ccW	2	period 1	*ḫur(rv)	I.15	\n\
cAc	cꜢ/0c	2	period 1	*š'am	I.19	\n\
cA/Uc	cꜢ/0c	2	period 1	*š'i/unfv	I.20	\n\
ccA/Uc	ccWc	3	period 1	*ʔvk'a:/o:nv	I.1	\n\
ccA/Uc	ccꜢ/0c	3	period 1	*bvy'i:/u:ʕ(wv)	I.3	\n\
ccA/Uc	ccWcW	3	period 1	*ḥvr'i:/u:rv	I.12	\n\
ccAc	ccꜢ/0c	3	period 1	*svʕ'artv	I.16	\n\
ccAc	ccꜢ/0c	3	period 1	*svrp'at	I.17	\n\
ccAc	ccꜢ/0c	3	period 1	*švb'adyv / *švb'a:dv	I.18	\n\
ccA/Uc	ccWc	3	period 1	*švḥ'i:/u:qv	I.21	\n\
cAcc	cꜢ/0cc	3	period 1	*qilʕv	I.22	\n\
ccAc	ccꜢ/0c	3	period 1	*kvl'a:lv	I.23	\n\
ccA/Uc	ccWc	3	period 1	*ḏvnr'i:/u:yv	I.25	\n\
ccA/Uc	cccW	3	period 1	*ḏvn'a/i/uḥ	I.26	\n\
ccA/Ucc	cccWc	4	period 1	*mvrk'a/obtv	I.7	\n\
cccAc	cccꜢ/0c	4	period 1	*mvkt'a(:)l(v)	I.9	\n\
ccA/Ucc	ccWcc	4	period 1	*ḥvl'i:/u:lwv	I.13	\n\
ccAcc	ccꜢ/0cWc	4	period 1	*kvl'ak(kvrv)	I.24	\n\
cccAcc	cccꜢ/0cc	5	period 1	*mvḫm'aḫwv	I.8	\n\
ccA	ccꜢ/0	2	period 2	*ʔvp'i:(cv)	II.1	\n\
cAc	cꜢ/0c	2	period 2	*y'am	II.2	\n\
cA/Uc	ccW	2	period 2	*ʕ'i/ur	II.3a	\n\
cA/Uc	cWc	2	period 2	*ʕ'i/ur	II.3b	\n\
cA/Uc	cꜢ/0c	2	period 2	*w'i/ur	II.7	\n\
cA/Uc	cWc	2	period 2	*b'i/unr	II.8	\n\
cA/Uc	cꜢ/0c	2	period 2	*b'i:/u:sv	II.10	\n\
cA/Uc	cꜢ/0c	2	period 2	*b'i:/u:sv	II.11	\n\
cA/Uc	cꜢ/0c	2	period 2	*b'i/ušʔv	II.12	\n\
cUc	cWc	2	period 2	*pu:l	II.13	\n\
cUc	ccW	2	period 2	*murḥv	II.14	\n\
cA/Uc	cꜢ/0c	2	period 2	*h'i/uy	II.22	\n\
cA/Uc	ccW	2	period 2	*h'i/up	II.23	\n\
cA/Uc	ccW	2	period 2	*h'i:/u:mv	II.24	\n\
cAc	cꜢ/0c	2	period 2	*ḫ'anr	II.28	\n\
cUc	ccW	2	period 2	*ḫur(r)v	II.29	\n\
cUc	ccW	2	period 2	*ḫur(rv)	II.30	\n\
cA/Uc	cꜢ/0c	2	period 2	*ḫ'i/ujtv	II.31	\n\
cA/Uc	ccW	2	period 2	*s'i:/u:kv	II.33	\n\
cA/Uc	cWc	2	period 2	*k'a/op	II.40	\n\
cAc	cꜢ/0c	2	period 2	*til(lv)	II.44	\n\
cA/Uc	cWc	2	period 2	*ṯ'i/uṯ	II.46	\n\
cA/Uc	cꜢ/0c	2	period 2	*ḏ'i/unr	II.47	\n\
ccUc	ccWc	3	period 2	*ʕvnr'o:rv	II.4a	\n\
ccUc	cccW	3	period 2	*ʕvnr'o:rv	II.4b	\n\
ccAc	ccꜢ/0c	3	period 2	*ʕvrš'i:/u:nv	II.5	\n\
ccAc	ccꜢ/0c	3	period 2	*ʕvg'altv	II.6	\n\
cAcc	cꜢ/0cc	3	period 2	*b'aryv	II.9	\n\
ccA/Uc	cccW	3	period 2	*mvḫ2'i:/u:rv	II.16	\n\
ccA/Uc	cccW	3	period 2	*mvḫ'i:/u:rv	II.17	\n\
ccUc	ccWc	3	period 2	*rvb'o:y(v)	II.21	\n\
cUcc	cWcc	3	period 2	*ḥumṣv	II.25	\n\
ccA/Uc	ccWc	3	period 2	*ḥvr'i:/u:rv	II.26	\n\
cA/Ucc	ccWc	3	period 2	*ḫ'i:/u:bvsv	II.27	\n\
ccAc	ccꜢ/0c	3	period 2	*ḫasi:nv	II.32	\n\
ccAc	ccꜢ/0c	3	period 2	*švb'ad	II.34a	\n\
ccUc	ccWc	3	period 2	*švb'o:dv	II.34b	\n\
ccUc	ccWc	3	period 2	*švb'o:dv	II.34c	\n\
ccAc	ccꜢ/0c	3	period 2	*švb'adyv	II.34d	\n\
ccA/Uc	ccWc	3	period 2	*švḥ'i:/u:qv	II.35	\n\
cA/Ucc	cꜢ/0cc	3	period 2	*k'i/urmv(t)	II.37	\n\
ccA/Uc	ccꜢ/0c	3	period 2	*qvr'i:/u:rv	II.38	\n\
cA/Ucc	cꜢ/0cc	3	period 2	*q'i/ultv	II.39	\n\
ccAc	ccꜢ/0c	3	period 2	*kvr'ak	II.41	\n\
cAcc	cꜢ/0cc	3	period 2	*k'awnv	II.42	\n\
ccUc	ccWc	3	period 2	*gvs'o:rv	II.43	\n\
ccUc	ccWcW	3	period 2	*tv(n)nu:r(v)	II.45	\n\
ccA/Uc	ccꜢ/0c	3	period 2	*ḏvnr'i:/u:yv	II.48	\n\
ccA/Uc	ccWc	3	period 2	*ṣvluḥi:t / *ṣvlloḫtv	II.49	\n\
ccA/Ucc	cccWc	4	period 2	*mvrk'a/obtv	II.15	\n\
cccUc	cccWcW	4	period 2	*mvsvs'o:bv	II.18	\n\
cccUc	cccWcW	4	period 2	*mvšd'o:dv	II.19	\n\
cccAc	cccꜢ/0c	4	period 2	*mvkt'ar	II.20	\n\
ccA/Ucc	ccꜢ/0cc	4	period 2	*švk'i:/u:rvʕv	II.36	\n\
cUc	cWc	2	period 3	*y'om	III.2	\n\
cAc	cꜢ/0c	2	period 3	*ʕ'enr	III.3	\n\
cAc	cꜢ/0c	2	period 3	*b'eʔšv	III.6	\n\
cAc	cꜢ/0c	2	period 3	*h'ey	III.10	\n\
cUc	ccW	2	period 3	*ḫur(r)v	III.14	\n\
cUc	ccW	2	period 3	*ḫ2'ord(v)	III.15	\n\
cAc	cꜢ/0c	2	period 3	*q'i:ḏv	III.19	\n\
cUc	ccW	2	period 3	*k'op	III.20	\n\
cUc	cWc	2	period 3	*g'onsv	III.21	\n\
cAc	cꜢ/0c	2	period 3	*ṯ'eṯ	III.22	\n\
ccUc	ccWc	3	period 3	*ʔvy'o:rv	III.1	\n\
ccAc	ccꜢ/0c	3	period 3	*ʕvrš'i:nv	III.4	\n\
cUcc	ccWc	3	period 3	*b'oryv	III.5	\n\
cAcc	cꜢ/0cc	3	period 3	*m'ekḥv	III.8	\n\
cUcc	cWcc	3	period 3	*ḥumṣv	III.11	\n\
ccA/Uc	ccWcW	3	period 3	*ḥvr'i:/u:rv	III.12	\n\
ccAc	ccꜢ/0c	3	period 3	*ḫab'er	III.13	\n\
ccUc	ccWc	3	period 3	*svrp'ot(v)	III.16	\n\
ccUc	cccW	3	period 3	*švb'odyv	III.17	\n\
ccAc	ccꜢ/0c	3	period 3	*qvr'i:rv	III.18	\n\
ccAc	ccꜢ/0c	3	period 3	*dəb'i:r	III.23	\n\
ccUcc	ccWcc	4	period 3	*mvrk'obtv	III.7	\n\
cccUc   cccWc	4	period 3	*mvkd'ol	III.9	\
"



#===================================

#settings

#type of words to be compared, according to the number of consonants
#  options: '2' : compares words with 2 consonants, '3' : compares words with 3 consonants, etc
#  note: the value must be a string, not an integer

consonants = '2'


#words to be compared, according to the period
#  options: 'period 1', 'period 2', 'period 3', 'all'
#  note: 'all' can be used to analyse all words from all periods together

period = 'period 1'

#Number of simulations to run

nr_simulations = 100000

#Path where the results of the simulation and the charts will be saved - leave empty to save in the same folder of the script

path = ''

#====================================

def match_counter(sample_1, sample_2):

    res_match = 0

    for i in range(0,len(sample_1)):
        current_match = 0

        for match in matches_2:
            if sample_1[i] == match[0] and sample_2[i] == match[1]:
                current_match = 1

        for match in matches_3:
            if sample_1[i] == match[0] and sample_2[i] == match[1]:
                current_match = 1

        if (current_match == 1):
            res_match = res_match + 1
    return res_match



#====================================

matches_2 = []
matches_2_lines = matches_string_2.split('\n')

for line in matches_2_lines:
    entry_matches_2 = line.split('\t')
    matches_2.append(entry_matches_2)

matches_3 = []
matches_3_lines = matches_string_3.split('\n')

for line in matches_3_lines:
    entry_matches_3 = line.split('\t')
    matches_3.append(entry_matches_3)

data = []
data_string = data_string.split('\n')

for line in data_string:
    entry_data = line.split('\t')
    data.append(entry_data)

sample_1 = []
sample_2 = []

for item in data:

    #========== settings: item[2] = nr of consonats,
    if item[2] == consonants and period == 'all':
        sample_1.append(item[0])
        sample_2.append(item[1])

    elif item[2] == consonants and item[3] == period:
        sample_1.append(item[0])
        sample_2.append(item[1])

result_counter = match_counter(sample_1, sample_2)

results_times = [0]

for item in sample_1:
    results_times.append(0)

for times in range(0,nr_simulations):

    random.shuffle(sample_1)
    random.shuffle(sample_2)

    result_counter = match_counter(sample_1, sample_2)

    results_times[result_counter] = results_times[result_counter] + 1

print ('======== Results ========')
print ('')
print ('Nr of Trials : Nr of Matches')
print ('')

string_results = 'Nr of Trials : Nr of Matches\n'

for i in range(0,len(results_times)):
    print (str(i) + ' : ' + str(results_times[i]))
    string_results = string_results + str(i) + ' : ' + str(results_times[i]) + '\n'


#========
#========Draw and print charts


x_pos = [i for i, _ in enumerate(results_times)]

plt.bar(x_pos, results_times, color='silver')

ax = plt.gca()
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)
if len(x_pos) < 30:
    plt.xticks(x_pos, x_pos)
else:
    plt.xticks(np.arange(min(x_pos), max(x_pos) + 1, 5.0))

if period == 'period 1':
    name_period = 'p_1'
elif period == 'period 2':
    name_period = 'p_2'
elif period == 'period 3':
    name_period = 'p_3'
elif period == 'all':
    name_period = 'all'

save_path = path + name_period + "_cons_" + consonants + '.png'
plt.savefig(save_path, dpi=600)

save_path_data = path + name_period + "_cons_" + consonants + '.txt'

f = open(save_path_data, 'w') #, 'a') -> + 'a' -> continues file; + 'w' -> overwrite existing file
f.write(string_results)
f.close()


plt.show()
