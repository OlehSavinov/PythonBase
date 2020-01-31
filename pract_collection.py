# ТЕКСТ ДЛЯ АНАЛИЗА
TEXT = """
The term "data science" has appeared in various contexts over the past thirty years but did not become an established term until recently. In an early usage, it was used as a substitute for computer science by Peter Naur in 1960. Naur later introduced the term "datalogy".[15] In 1974, Naur published Concise Survey of Computer Methods, which freely used the term data science in its survey of the contemporary data processing methods that are used in a wide range of applications.

In 1996, members of the International Federation of Classification Societies (IFCS) met in Kobe for their biennial conference. Here, for the first time, the term data science is included in the title of the conference ("Data Science, classification, and related methods"),[16] after the term was introduced in a roundtable discussion by Chikio Hayashi.[3]

In November 1997, C.F. Jeff Wu gave the inaugural lecture entitled "Statistics = Data Science?"[17] for his appointment to the H. C. Carver Professorship at the University of Michigan.[18] In this lecture, he characterized statistical work as a trilogy of data collection, data modeling and analysis, and decision making. In his conclusion, he initiated the modern, non-computer science, usage of the term "data science" and advocated that statistics be renamed data science and statisticians data scientists.[17] Later, he presented his lecture entitled "Statistics = Data Science?" as the first of his 1998 P.C. Mahalanobis Memorial Lectures.[19] These lectures honor Prasanta Chandra Mahalanobis, an Indian scientist and statistician and founder of the Indian Statistical Institute.

In 2001, William S. Cleveland introduced data science as an independent discipline, extending the field of statistics to incorporate "advances in computing with data" in his article "Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics," which was published in Volume 69, No. 1, of the April 2001 edition of the International Statistical Review / Revue Internationale de Statistique.[20] In his report, Cleveland establishes six technical areas which he believed to encompass the field of data science: multidisciplinary investigations, models and methods for data, computing with data, pedagogy, tool evaluation, and theory.

In April 2002, the International Council for Science (ICSU): Committee on Data for Science and Technology (CODATA)[21] started the Data Science Journal,[22] a publication focused on issues such as the description of data systems, their publication on the internet, applications and legal issues.[23] Shortly thereafter, in January 2003, Columbia University began publishing The Journal of Data Science,[24] which provided a platform for all data workers to present their views and exchange ideas. The journal was largely devoted to the application of statistical methods and quantitative research. In 2005, The National Science Board published "Long-lived Digital Data Collections: Enabling Research and Education in the 21st Century" defining data scientists as "the information and computer scientists, database and software and programmers, disciplinary experts, curators and expert annotators, librarians, archivists, and others, who are crucial to the successful management of a digital data collection" whose primary activity is to "conduct creative inquiry and analysis."[25]

Around 2007,[citation needed] Turing award winner Jim Gray envisioned "data-driven science" as a "fourth paradigm" of science that uses the computational analysis of large data as primary scientific method[4][5] and "to have a world in which all of the science literature is online, all of the science data is online, and they interoperate with each other."[26]

In the 2012 Harvard Business Review article "Data Scientist: The Sexiest Job of the 21st Century",[6] DJ Patil claims to have coined this term in 2008 with Jeff Hammerbacher to define their jobs at LinkedIn and Facebook, respectively. He asserts that a data scientist is "a new breed", and that a "shortage of data scientists is becoming a serious constraint in some sectors", but describes a much more business-oriented role.

In 2013, the IEEE Task Force on Data Science and Advanced Analytics[27] was launched. In 2013, the first "European Conference on Data Analysis (ECDA)" was organised in Luxembourg, establishing the European Association for Data Science (EuADS). The first international conference: IEEE International Conference on Data Science and Advanced Analytics was launched in 2014.[28] In 2014, General Assembly launched student-paid bootcamp and The Data Incubator launched a competitive free data science fellowship.[29] In 2014, the American Statistical Association section on Statistical Learning and Data Mining renamed its journal to "Statistical Analysis and Data Mining: The ASA Data Science Journal" and in 2016 changed its section name to "Statistical Learning and Data Science".[30] In 2015, the International Journal on Data Science and Analytics[31] was launched by Springer to publish original work on data science and big data analytics. In September 2015 the Gesellschaft für Klassifikation (GfKl) added to the name of the Society "Data Science Society" at the third ECDA conference at the University of Essex, Colchester, UK.
"""

lat_lower = 'abcdefghijklmnopqrstuvwxyz'
lat_upper = lat_lower.upper()
lat_total = lat_lower + lat_upper
lower_text = TEXT.lower()

#ex1-------------------------------------
upper = 0
for i in TEXT:
    if i in lat_upper:
        upper += 1

lower = 0
for i in TEXT:
    if i in lat_lower:
        lower += 1

total = upper + lower

res_ex1 = {
    'total': total,
    'upper': upper,
    'lower': lower,
}


#ex2-------------------------------------
res_ex2 = []
for i in lat_lower:
    c = 0
    c += lower_text.count(i)
    res = tuple((i, c))
    res_ex2.append(res)

#ex3-------------------------------------
res_ex3 = list(res_ex2)
res_ex3.sort(key=lambda i: i[1])

#ex4-------------------------------------
ts = TEXT.split()
print(len(ts))
for i in TEXT:
    if not i.isalnum():
        new_text = TEXT.replace(i, '1')
        continue
print(new_text)



#result-----------------------------------------------------
# result = {'1': res_ex1, '2': res_ex2, '3': res_ex3}
# print(result)
