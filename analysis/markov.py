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
   


# data
df = pd.read_excel('state_defnew.xlsx')


class Markov:
    def __init__(self, df_data_list):
        self.group = df_data_list['state']
        self.probability_of_transition = {}
        self.excell_data = []

    def control(self, current_data):
        if current_data in self.probability_of_transition:
            return True
        else:
            return False

    def control_transition_data(self, current_data, next_data):
        if next_data in self.probability_of_transition[current_data]['transition']:
            return True
        else:
            return False

    def transition(self, current_data, next_data):
        if (self.control_transition_data(current_data, next_data)):
            self.probability_of_transition[current_data]['transition'][next_data]['amount'] += 1
            self.probability_of_transition[current_data]['transition'][next_data]['probability'] = \
            self.probability_of_transition[current_data]['transition'][next_data]['amount'] / \
            self.probability_of_transition[current_data]['amount']
        else:
            self.probability_of_transition[current_data]['transition'][next_data] = {'amount': 1, 'probability': 1 /
                                                                                                                 self.probability_of_transition[
                                                                                                                     current_data][
                                                                                                                     'amount']}

    def analysis(self):
        for i in list(range(0, len(self.group))):
            if (i == len(self.group) - 1):
                break
            current_data = self.group[i]
            next_data = self.group[i + 1]
            control_result = self.control(current_data)
            if (control_result):
                self.probability_of_transition[current_data]['amount'] += 1
            else:
                self.probability_of_transition[current_data] = {'amount': 1, 'transition': {}}
            self.transition(current_data, next_data)

    def add_to_excel(self, file_name):
        self.df_output = pd.DataFrame(self.excell_data, columns=['from_state', 'amount', 'to_state', 'amount', 'probability'], )
        self.df_output.to_excel(file_name, index=False)

    def run(self):
        self.analysis()
        for i in self.probability_of_transition:
            key = i
            amount = self.probability_of_transition[i]['amount']
            print(key)
            print('amount', amount)
            print('Transitions')
            for j in self.probability_of_transition[i]['transition']:
                key_2 = j
                amount_2 = self.probability_of_transition[i]['transition'][j]['amount']
                probability = amount_2 / amount
                print(key)
                print('amount', self.probability_of_transition[i]['transition'][j]['amount'])
                print('Probability', self.probability_of_transition[i]['transition'][j]['probability'])
                print('------------------------------------------------')
                arr = [key, amount, key_2, amount_2, probability]
                self.excell_data.append(arr)


markov_program = Markov(df)

# start markov program
markov_program.run()

markov_program.add_to_excel('transition_probability2.xlsx')
