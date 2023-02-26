# import pandas, numpy, and matplotlib
import pandas as pd

# load the income gap data
un_income_gap = pd.read_csv("data/un_income_gap.csv")
un_income_gap.set_index('country', inplace=True)
un_income_gap['incomeratio'] = \
  un_income_gap.femaleincomepercapita / \
    un_income_gap.maleincomepercapita
un_income_gap['educratio'] = \
  un_income_gap.femaleyearseducation / \
     un_income_gap.maleyearseducation
un_income_gap['laborforcepartratio'] = \
  un_income_gap.femalelaborforceparticipation / \
     un_income_gap.malelaborforceparticipation
un_income_gap['humandevratio'] = \
  un_income_gap.femalehumandevelopment / \
     un_income_gap.malehumandevelopment
     
num_cols = ['educratio','laborforcepartratio','humandevratio',
  'genderinequality','maternalmortality','incomeratio',
  'adolescentbirthrate', 'femaleperparliament','incomepercapita']

gap = un_income_gap[num_cols]

