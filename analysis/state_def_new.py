import pandas as pd
import os



df = pd.read_excel('state_def.xlsx')
# add the new columns to the DataFrame
df['Speedmin'] = ''
df['Speedmax'] = ''
df['Temperaturemin'] = ''
df['Temperaturemax'] = ''
df['Irradiancemin'] = ''
df['Irradiancemax'] = ''
df['Pressuremin'] = ''
df['Pressuremax'] = ''

# loop through each row of the DataFrame
for i in range(len(df)):
    group = df.loc[i, 'group']
    Speedmin, Speedmax = '', ''
    Temperaturemin, Temperaturemax = '', ''
    Irradiancemin, Irradiancemax = '', ''
    Pressuremin, Pressuremax = '', ''
    
    # split the values in the group column
    group_values = group.strip('[]').split(',')
    for j, value in enumerate(group_values):
        value = int(value.strip())
        if j == 0:
            Speedmin, Speedmax = value, value+1
        elif j == 1:
            Temperaturemin, Temperaturemax = -40 +(value*3.6), (-36.4 +(value*3.6))
        elif j == 2:
            Irradiancemin, Irradiancemax = 0 + (value*72), (72 + (value*72))
        elif j == 3:
            Pressuremin, Pressuremax = 93 + (value*0.28), (93.28 + (value*0.28))
    
    # assign the values to the corresponding columns
    df.loc[i, 'Speedmin'] = Speedmin
    df.loc[i, 'Speedmax'] = Speedmax
    df.loc[i, 'Temperaturemin'] = Temperaturemin
    df.loc[i, 'Temperaturemax'] = Temperaturemax
    df.loc[i, 'Irradiancemin'] = Irradiancemin
    df.loc[i, 'Irradiancemax'] = Irradiancemax
    df.loc[i, 'Pressuremin'] = Pressuremin
    df.loc[i, 'Pressuremax'] = Pressuremax
    
df.to_excel('state_defnew.xlsx', index=False)
   