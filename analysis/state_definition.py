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


program = Program(df.head())

# start program
program.run()

# result
res = program.res()
# save to excel
program.add_data_to_excel('output.xlsx')







