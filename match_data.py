import csv
from pyjarowinkler import distance
from jaccard_index.jaccard import jaccard_index
# Step 1
'''
keywords = [

            # 4 terms: 0 abbre
            ' IBM Technical disclosure Bulletin', 'IBM TECHNICAL DISCLOSURE BULLETIN', 'TECHNICAL DISCLOSURE BULLETIN',
            'IBM\'s Technical Disclosure Bulletin', 'IBM\'s Technology Disclosure Bulletin',
            'IBM Technical Disclosure Bulletin', 'IBM Technology Disclosure Bulletin',
            'IBM Technical disclosure Bulletin', 'IBM Technical Discosure Bulletin',
            'IBM TechnicaL Disclosure Bulletin', 'IBM TECHNICAL DISCLOSURE BULLETIN',
            'IBM Technical Dislosure Bulletin', 'IBM Tehcnical Disclosure Bulletin',
            'IBM Technical Enclosure Bulletin', 'IBM Tecnical Disclosure Bulletin',
            'IBM _Technical Disclosure Bulletin', 'Technical Disclosure Bulletin IBM',
            'IBM Research Disclosure Bull', 'IBM Tehnical Disclosure Bulletin',
            'IBM Burlington Technical Bulletin',

            # 4 terms: 1 abbre.
            'IBM Techn Disclosure Bulletin',
            'IBM Tech Disclosure Bulletin', 'IBM Tec Disclosure Bulletin',
            'IBM Tech disclosure bulletin', 'IBM Tec disclosure bulletin',
            'IBM Technology Discl Bulletin', 'IBM Technology Disc Bulletin',
            'IBM Teccal Disclosure Bulletin',
            'IBM Technical Discl Bulletin', 'IBM Technical Disc Bulletin',
            'IBM Technical Disclosure Bull', 'IBM Technology Disclosure Bull',
            'IBM Technical Dis Bulletin', 'IBM Technology Dis Bulletin',
            'IBM chnical Disclosure Bulletin',

            # 4 terms: 2 abbre.
            'IBM Teca Discl Bulletin', 'IBM Teca Disc Bulletin', 'IBM Teca Dis Bulletin',
            'IBM Techn Discl Bulletin', 'IBM Techn Disc Bulletin', 'IBM Techn Dis Bulletin',
            'IBM Tech Discl Bulletin', 'IBM Tech Disc Bulletin', 'IBM Tech Dis Bulletin',
            'IBM Tec Discl Bulletin', 'IBM Tec Disc Bulletin', 'IBM Tec Dis Bulletin',
            'IBM Tech Disclosure Bull', 'IBM Tec Disclosure Bull',
            'IBM Tech Disclosure Bul', 'IBM Tec Disclosure Bul',
            'IBM Technology Discl Bull', 'IBM Technology Disc Bull',
            'IBM Technology Discl Bul', 'IBM Technology Disc Bul',
            'IBM Technical Discl Bull', 'IBM Technical Disc Bull',
            'IBM Technical Discl Bul', 'IBM Technical Disc Bul',
            'IBM Tech Div Bulletin',
            'IBM _Tech Disc Bulletin',

            # 4 terms: 3 abbre.
            'IBM Techn Discl Bull', ' IBM Techn Discl Bul',
            'IBM Techn Disc Bull', ' IBM Techn Disc Bul',
            'IBM Tech Dicls Bull', 'IBM Tech Dicls Bul',
            'IBM Tech Discl Bull', 'IBM Tech Discl Bul',
            'IBM Tech Disc Bull', 'IBM Tech Disc Bul',
            'IBM Tech Dis Bull', 'IBM Tech Dis Bul',
            'IBM Tech Dicl Bull', 'IBM Tech Dicl Bul',
            'IBM Tec Disc Bull', 'IBM Tec Disc Bul',
            'IBM ch Disclosure Bull', 'IBM ch Disclosure Bul',
            'IBM ch Disc Bull', 'IBM ch Disc Bul',
            'IBM ch Dis Bull', 'IBM ch Dis Bul',
            'IBM Tech D B', 'IBM T D Bulletin', 'IBM T D B',
            'IBM _Tech Discl Bull',



            # 3 terms
            'IBM disclosure Bulletin',
            'IBM Disclosure Bulletin', 'IBM Disclosure Bulletin',
            'IBM Technical Disclosure', 'IBM Technology Disclosure',
            'IBM Technical Bulletin', 'IBM Technology Bulletin',
            'IBM Disclosure Bulletin', 'IBM disclosure Bulletin',
            'IBM Disclosure Bull', 'IBM Disclosure Bul',
            'IBM Technical Bull', 'IBM Technical Bul',
            'IBM Disc Bulletin', 'IBM Dis Bulletin',
            'nical Disclossure Bulliten', 'nical Disclosure BUlletin', 'nical Disclosre Bullein',


            'IBM tech Bulletin', 'IBM tec Bulletin', 'IBM ch Dis',
            'IBM Disclosure Bulletin',
            'IBM Tech Bull', 'IBM Tech Bul',
            'IBM Tech Discl', 'IBM Tech Disc', 'IBM Tech Dis',
            'IBM Discl Bull', 'IBM Discl Bul',
            'IBM Disc Bull', 'IBM Disc Bul',
            'IBM Dis Bull', 'IBM Dis Bul',
            'Technical Disclosure Bulletin', 'Tech Disc Bull', 'IBM Tec Dis', 'IBM Teccal', 'IBM T D',


            # 2 terms
            'IBM Bulletin',
            'IBM Bulletin', 'IBM Disclosure', 'IBM Tech', 'IBM TDB', 'IBM TDM', 'IBM bulletin', 'IBM  Disc',
            'Disclosure Bulletin', 'Disclosure Bull', 'disclosure Bulletin', 'Disc Bulletin',
            'Disclos Bull', 'Discl Bul', 'Disc Bulletin', 'Disc Bull', 'Disc Bul',
            'Dis Bull', 'Discl Bul', 'osure Bulletin', 'osure Bul',
            'cl Bulletin', 'c Bulletin', 'c Bull', 'c Bul', 'c Bultn', 'cl Bulle', 'cl Bull', 'l bull', 'Dsclre Bulltn',
            'nical etin', 'IBM Tec', 'IBM discl', 'Tech disclosue', 'tech discl', 'Tech disclosue',


            # 1 term
            'IBMTDB', ' Bull ', 'Bullentin', 'Bulln', ' Bul ', 'Bulletin', 'Bullet', 'Bult', 'bulletin', 'Buletin',
            'Buletin', 'Disclosure', 'nical', 'IBM', 'disclosure', 'Disclletin', 'Disclre', 'Disclose', 'Disclitia',
            'Discloser', 'Disclosvol', 'Discl', 'DIscl', 'disclisure', 'discl', 'TDB',
            ]
with open('../matching_data/step_1.csv', 'w+') as csvfile_step_1:
    spamwriter = csv.writer(csvfile_step_1, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    with open('../matching_data/matchpart2.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            nplref = row[1]
            for keyword in keywords:
                if keyword in nplref:
                    nplref = nplref.replace(keyword, '')
            spamwriter.writerow([row[0], nplref, row[2]])
'''

# Step 2
'''
patent_nplref_year = {}
with open('../matching_data/step_1.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i in range(30049):
        next(spamreader)
    for row in spamreader:
        patent_nplref_year[(row[0], row[1])] = row[2]

code_reference_year = {}
with open('../matching_data/matchpart1.csv', 'r', encoding='unicode_escape') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|',)
    next(spamreader)
    for row in spamreader:
        code_reference_year[(row[1], row[2])] = row[0]

with open('../matching_data/step_2.csv', 'a+') as csvfile_step_2:
    spamwriter = csv.writer(csvfile_step_2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow(['patent', 'nplref', '1st code', '1st reference', 'similarity', '2nd code', '2nd reference', 'similarity',
                        # '3rd code', '3rd reference', 'similarity'])
    for (patent, nplref) in patent_nplref_year:
        if nplref != '':
            comparing_result = {}
            for (code, reference) in code_reference_year:
                if (reference != '') and \
                   (patent_nplref_year[(patent, nplref)] == code_reference_year[(code, reference)]):
                    comparing_result[(code, reference)] = distance.get_jaro_distance(nplref,
                                                                        reference,
                                                                        winkler=True,
                                                                        scaling=0.1)
            sorted_comparing_result = dict(sorted(comparing_result.items(), key=lambda x: x[-1], reverse=True))
            top_3_comparing_result = list(sorted_comparing_result.items())[:3]
            spamwriter.writerow([patent, nplref,
                                 top_3_comparing_result[0][0][0], top_3_comparing_result[0][0][1],
                                 top_3_comparing_result[0][1],
                                 top_3_comparing_result[1][0][0], top_3_comparing_result[1][0][1],
                                 top_3_comparing_result[1][1],
                                 top_3_comparing_result[2][0][0], top_3_comparing_result[2][0][1],
                                 top_3_comparing_result[2][1],
                                 ])
            print(top_3_comparing_result[0][0])
'''

# Step 3
'''
patent_nplref_year = {}
with open('../matching_data/step_1.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i in range(1):
        next(spamreader)
    for row in spamreader:
        patent_nplref_year[(row[0], row[1])] = row[2]

with open('../matching_data/step_3.csv', 'w+') as csvfile_step_2:
    spamwriter = csv.writer(csvfile_step_2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['patent', 'nplref', 'year', 'code', 'reference', 'distance score', 'rank'])
    with open('../matching_data/step_2.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for row in spamreader:
            patent = row[0]
            nplref = row[1]
            year = patent_nplref_year[(patent, nplref)]
            for i in range (3):
                code = row[2 + 3 * i]
                reference = row[3 + 3 * i]
                distance_score = row[4 + 3 * i]
                rank = i + 1
                #print(patent, nplref, year, code, reference, distance_score, rank)
                spamwriter.writerow([patent, nplref, year, code, reference, distance_score, rank])
'''

# Compute jaccard distance
with open('../matching_data/step_3_jaccard.csv', 'w+') as csvfile_step_3:
    spamwriter = csv.writer(csvfile_step_3, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['patent', 'nplref', 'year', 'code', 'reference', 'Jaro-Winkler distance', 'rank',
                         'Jaccard distance'])
    with open('../matching_data/step_3.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(spamreader)
        for row in spamreader:
            jaccard_distance = round(jaccard_index(row[1], row[4]), 2)
            spamwriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], jaccard_distance])






