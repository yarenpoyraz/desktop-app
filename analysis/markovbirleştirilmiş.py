import pandas as pd
import os

# data
df = pd.read_excel('./markov_veri.xlsx')
class Program:
    def __init__(self, data):
        self.df = data
        self.amount_data = len(self.df)
        self.speed = self.df['Speed']
        self.temperature = self.df['Temperature']
        self.irradiance = self.df['Irradiance']
        self.pressure = self.df['Pressure']
        self.speed_array =[[-1 + i,0 + i]for i in range(1,26)]
        self.temperature_array =[[-43.4 + (i * 3.6), -40 + (i * 3.6)] for i in range(1,26)]
        self.irradiance_array =[[-72 + (i * 72), i * 72]for i in range(1,26)]
        self.pressure_array =[[92.72+ (i*0.28),93 + (0.28 * i)]for i in range(1,26)]
        self.group = []
        self.ids = []
        self.init_values()
        self.init_inc()
        self.init_data()
        self.uniq_ids = self.get_uniq_ids()
    def get_uniq_id(self,state):
       uid = self.uniq_ids[state]
       return uid
    def get_uniq_ids(self):
        state_dict={}
        state_number = 0
        for i in range(25):
            for j in range(25):
                for k in range(25):
                    for l in range(25):
                        state = [i, j, k, l]
                        state_dict[str(state)] = state_number
                        state_number+=1
        return state_dict
    def get_speed_state(self,speed):
        state = 0
        index = 0
        for i in self.speed_array:
            if(i[0] <= speed  and speed <= i[1]):
                state = index
                break
            index = index + 1
        return state
    def get_temperature_state(self,temperature):
        state = 0
        index = 0
        for i in self.temperature_array:
            if(i[0] <= temperature  and temperature <= i[1]):
                state = index
            index = index + 1
        return state
    def get_irradiance_state(self,irradiance):
        state = 0
        index = 0
        for i in self.irradiance_array:
            if(i[0] <= irradiance  and irradiance <= i[1]):
                state = index
            index = index + 1
        return state
    def get_pressure_state(self,pressure):
        state = 0
        index = 0
        for i in self.pressure_array:
            if(i[0] <= pressure  and pressure <= i[1]):
                state = index
            index = index + 1
        return state

    def init_values(self):
        self.init_speed = [-1, 0]
        self.init_temperature = [-43.6, -40]
        self.init_irradiance = [-72, 0]
        self.init_pressure=[92.72, 93]

    def init_inc(self):
        self.inc_speed = 1
        self.inc_temp = 3.6
        self.inc_irr = 72
        self.inc_pressure = 0.28

    def init_data(self):
        self.df['group'] = None

    def process(self):
        index =0
        for i in range(0,self.amount_data):
            speed_state = self.get_speed_state(self.speed[i])
            temperature = self.get_temperature_state(self.temperature[i])
            irradiance = self.get_irradiance_state(self.irradiance[i])
            pressure = self.get_pressure_state(self.pressure[i])
            state = [speed_state,temperature,irradiance,pressure]
            self.df.loc[i, 'group'] = str(state)
            self.group.append([state])
            uniq_id_of_state = self.get_uniq_id(str(state))
            self.ids.append(uniq_id_of_state)
            self.df.loc[i, 'state'] = uniq_id_of_state
            print(self.df.loc[i])
            index = index + 1
            print('%{} completed'.format((index / self.amount_data) * 100))
    def run(self):
        print('run funct init')
        self.process()

    def res(self):
        return self.df

    def add_data_to_excel(self, file_name):
        self.df.to_excel(file_name)

    # create program


    




program = Program(df)

# start program
program.run()

# result
res = program.res()
# save to excel
program.add_data_to_excel('state_def.xlsx')

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
