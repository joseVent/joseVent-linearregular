
#he metido este codigo 

#var = ['0-9', '19-Oct', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79','80+', 'White-alone pop', 'Two or more races pop', 'GQ_ESTIMATES_2018','Less than a high school diploma 2014-18','High school diploma only 2014-18','Some college or associate's degree 2014-18','Bachelor's degree or higher 2014-18', 'POVALL_2018',
#'Civilian_labor_force_2018', 'Employed_2018', 'Unemployed_2018','Total nurse practitioners (2019)', 'Total physician assistants (2019)','Total Hospitals (2019)', 'Internal Medicine Primary Care (2019)','Family Medicine/General Practice Primary Care (2019)','Total Specialist Physicians (2019)', 'ICU Beds_x', 'Total Population','Population Aged 60+', 'county_pop2018_18 and older','anycondition_number', 'Obesity_number', 'Heart disease_number','COPD_number', 'diabetes_number', 'CKD_number', 'POP_TOT']

import matplotlib.pyplot as plt


fig, axis = plt.subplots(74, 2, figsize=(60, 20), gridspec_kw={'height_ratios': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
# Crear una figura múltiple con histogramas y diagramas de caja
sns.histplot(ax = axis[0, 0], data = total_data, x = "0-9").set(xlabel = None)
sns.boxplot(ax = axis[0, 1], data = total_data, x = "0-9")
sns.histplot(ax = axis[1, 0], data = total_data, x = "19-Oct").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[1, 1], data = total_data, x = "19_Oct")
sns.histplot(ax = axis[2, 0], data = total_data, x = "20_29").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[2, 1], data = total_data, x = "20_29")
sns.histplot(ax = axis[3, 0], data = total_data, x = "30_39").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[3, 1], data = total_data, x = "30_39")
sns.histplot(ax = axis[4, 0], data = total_data, x = "40-49").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[4, 1], data = total_data, x = "40_49")
sns.histplot(ax = axis[5, 0], data = total_data, x = "50_59").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[5, 1], data = total_data, x = "50-59")
sns.histplot(ax = axis[6, 0], data = total_data, x = "60-69").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[6, 1], data = total_data, x = "60_69")
sns.histplot(ax = axis[7, 0], data = total_data, x = "70_79").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[7, 1], data = total_data, x = "70-79")
sns.histplot(ax = axis[8, 0], data = total_data, x = "80+").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[8, 1], data = total_data, x = "80+")
sns.histplot(ax = axis[9, 0], data = total_data, x = "White-alone pop").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[9, 1], data = total_data, x = "White-alone pop")
sns.histplot(ax = axis[10, 0], data = total_data, x = "Two or more races pop").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[10, 1], data = total_data, x = "Two or more races pop")
sns.histplot(ax = axis[11, 0], data = total_data, x = "GQ_ESTIMATES_2018").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[11, 1], data = total_data, x = "GQ_ESTIMATES_2018")
sns.histplot(ax = axis[12, 0], data = total_data, x = "Less than a high school diploma 2014-18").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[12, 1], data = total_data, x = "Less than a high school diploma 2014-18")
sns.histplot(ax = axis[13, 0], data = total_data, x = "High school diploma only 2014-18").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[13, 1], data = total_data, x = "'High school diploma only 2014-18'")
sns.histplot(ax = axis[14, 0], data = total_data, x = "Some college or associate's degree 2014-18").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[14, 1], data = total_data, x = "Some college or associate's degree 2014-18")
sns.histplot(ax = axis[15, 0], data = total_data, x = "Bachelor's degree or higher 2014-18").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[15, 1], data = total_data, x = "Bachelor's degree or higher 2014-18")
sns.histplot(ax = axis[16, 0], data = total_data, x = "POVALL_2018").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[16, 1], data = total_data, x = "POVALL_2018")
sns.histplot(ax = axis[17, 0], data = total_data, x = "Civilian_labor_force_2018").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[17, 1], data = total_data, x = "Civilian_labor_force_2018")
sns.histplot(ax = axis[18, 0], data = total_data, x = "Employed_2018").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[18, 1], data = total_data, x = "Employed_2018")
sns.histplot(ax = axis[19, 0], data = total_data, x = "Unemployed_2018").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[19, 1], data = total_data, x = "Unemployed_2018")
sns.histplot(ax = axis[20, 0], data = total_data, x = "Total nurse practitioners (2019)").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[20, 1], data = total_data, x = "Total nurse practitioners (2019)")
sns.histplot(ax = axis[21, 0], data = total_data, x = "Total physician assistants (2019)").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[21, 1], data = total_data, x = "Total physician assistants (2019)")
sns.histplot(ax = axis[22, 0], data = total_data, x = "Total Hospitals (2019)").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[22, 1], data = total_data, x = "Total Hospitals (2019)")
sns.histplot(ax = axis[23, 0], data = total_data, x = "Internal Medicine Primary Care (2019)").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[23, 1], data = total_data, x = "Internal Medicine Primary Care (2019)")
sns.histplot(ax = axis[24, 0], data = total_data, x = "Family Medicine/General Practice Primary Care (2019)").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[24, 1], data = total_data, x = "Family Medicine/General Practice Primary Care (2019)")
sns.histplot(ax = axis[25, 0], data = total_data, x = "Total Specialist Physicians (2019)").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[25, 1], data = total_data, x = "Total Specialist Physicians (2019)")
sns.histplot(ax = axis[26, 0], data = total_data, x = "ICU Beds_x").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[26, 1], data = total_data, x = "ICU Beds_x")
sns.histplot(ax = axis[27, 0], data = total_data, x = "Total Population").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[27, 1], data = total_data, x = "Total Population")
sns.histplot(ax = axis[28, 0], data = total_data, x = "Population Aged 60+").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[28, 1], data = total_data, x = "Population Aged 60+")
sns.histplot(ax = axis[29, 0], data = total_data, x = "county_pop2018_18 and older").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[29, 1], data = total_data, x = "county_pop2018_18 and older")
sns.histplot(ax = axis[30, 0], data = total_data, x = "anycondition_number").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[30, 1], data = total_data, x = "anycondition_number")
sns.histplot(ax = axis[31, 0], data = total_data, x = "Obesity_number").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[31, 1], data = total_data, x = "'Obesity_number")
sns.histplot(ax = axis[32, 0], data = total_data, x = "Heart disease_number").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[32, 1], data = total_data, x = "Heart disease_number")
sns.histplot(ax = axis[33, 0], data = total_data, x = "COPD_number").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[33, 1], data = total_data, x = "COPD_number")
sns.histplot(ax = axis[34, 0], data = total_data, x = "diabetes_number").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[34, 1], data = total_data, x = "diabetes_number")
sns.histplot(ax = axis[35, 0], data = total_data, x = "CKD_number").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[35, 1], data = total_data, x = "CKD_number")
sns.histplot(ax = axis[36, 0], data = total_data, x = "POP_TOT").set(xlabel = None, ylabel = None)
sns.boxplot(ax = axis[36, 1], data = total_data, x = "POP_TOT")





# Ajustar el layout
plt.tight_layout()

# Mostrar el plot
plt.show()


#me ha respondido: 

alueError                                Traceback (most recent call last)
Cell In[5], line 7
      1 #var = ['0-9', '19-Oct', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79','80+', 'White-alone pop', 'Two or more races pop', 'GQ_ESTIMATES_2018','Less than a high school diploma 2014-18','High school diploma only 2014-18','Some college or associate's degree 2014-18','Bachelor's degree or higher 2014-18', 'POVALL_2018',
      2 #'Civilian_labor_force_2018', 'Employed_2018', 'Unemployed_2018','Total nurse practitioners (2019)', 'Total physician assistants (2019)','Total Hospitals (2019)', 'Internal Medicine Primary Care (2019)','Family Medicine/General Practice Primary Care (2019)','Total Specialist Physicians (2019)', 'ICU Beds_x', 'Total Population','Population Aged 60+', 'county_pop2018_18 and older','anycondition_number', 'Obesity_number', 'Heart disease_number','COPD_number', 'diabetes_number', 'CKD_number', 'POP_TOT']
      4 import matplotlib.pyplot as plt
----> 7 fig, axis = plt.subplots(74, 2, figsize=(60, 20), gridspec_kw={'height_ratios': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]})
      8 # Crear una figura múltiple con histogramas y diagramas de caja
      9 sns.histplot(ax = axis[0, 0], data = total_data, x = "0-9").set(xlabel = None)

File ~/.local/lib/python3.11/site-packages/matplotlib/pyplot.py:1502, in subplots(nrows, ncols, sharex, sharey, squeeze, width_ratios, height_ratios, subplot_kw, gridspec_kw, **fig_kw)
   1358 """
   1359 Create a figure and a set of subplots.
   1360 
   (...)
   1499 
   1500 """
   1501 fig = figure(**fig_kw)
-> 1502 axs = fig.subplots(nrows=nrows, ncols=ncols, sharex=sharex, sharey=sharey,
   1503                    squeeze=squeeze, subplot_kw=subplot_kw,
   1504                    gridspec_kw=gridspec_kw, height_ratios=height_ratios,
   1505                    width_ratios=width_ratios)
   1506 return fig, axs

File ~/.local/lib/python3.11/site-packages/matplotlib/figure.py:916, in FigureBase.subplots(self, nrows, ncols, sharex, sharey, squeeze, width_ratios, height_ratios, subplot_kw, gridspec_kw)
...
--> 133     raise ValueError('Expected the given number of height ratios to '
    134                      'match the number of rows of the grid')
    135 self._row_height_ratios = height_ratios

ValueError: Expected the given number of height ratios to match the number of rows of the grid

puedes arreglarlo?





