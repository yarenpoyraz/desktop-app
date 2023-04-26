from analysis.algorithm import a
from analysis.state_definition import Program

filePath = 'markov_veri.xlsx'

program = Program(df)

# start program
program.run()

# result
res = program.res()
# save to excel
program.add_data_to_excel('state_def.xlsx')