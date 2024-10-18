import pandas as pd
import sys
import os

os.chdir(r'C:\Users\jpark\VisualStudio\Simpsons_BACI\\')

baci_data = r"C:\Users\jpark\Downloads\BACI_HS92_V202401b"

def country_mappings():
  baci_country = pd.read_csv(baci_data + "\country_codes_V202401b.csv", usecols=['country_code', 'country_iso3'])


  ### Make Hong part of China (sorry Hong Kong)
  baci_country[baci_country['country_code'] == 344] = 156
  baci_country[baci_country['country_code'] == 344] = 156

  iso_regions = pd.read_csv(r"baci_preparation\iso_countries_regions.csv", usecols=['name', 'alpha-3', 'region_eu'])
  iso_regions.to_csv("iso")

  iso_regs = baci_country.merge(iso_regions, left_on='country_iso3', right_on='alpha-3', how='left')
  iso_regs.drop(columns=['country_iso3'], inplace=True)

  iso_regs['OECD'] = 'RoW'

  #iso_regs['new'] = np.where(iso_regs['region_eu'] == 'Europe', 'Europe', np.NAN)
  iso_regs.loc[(iso_regs['alpha-3'] == 'JPN', 'OECD')] = 'Japan'
  iso_regs.loc[(iso_regs['alpha-3'] == 'USA', 'OECD')] = 'United States'
  iso_regs.loc[(iso_regs['alpha-3'] == 'CHN', 'OECD')] = 'China, incl. Hong-Kong'
  iso_regs.loc[(iso_regs['alpha-3'] == 'HKG', 'OECD')] = 'China, incl. Hong-Kong'
  iso_regs.loc[(iso_regs['alpha-3'] == 'KOR', 'OECD')] = 'Korea'
  iso_regs.loc[(iso_regs['alpha-3'] == 'TWN', 'OECD')] = 'Chinese Taipei'

  eu = [
    'AUT', 'BEL', 'BGR','HRV', 'CZE', 'DNK', 'EST', 'FIN', 'FRA',
    'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LTU', 'LUX', 'MLT',
    'NLD', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE', 'CYP'
  ]

  iso_regs.loc[(iso_regs['alpha-3'].isin(eu), 'OECD')] = 'European Union'


  iso_regs.rename(columns = {'alpha-3': 'ISO3'}, inplace = True)

  return iso_regs[['country_code', 'ISO3', 'region_eu', 'OECD']]


country_mappings().to_csv("country_mapping.csv")

