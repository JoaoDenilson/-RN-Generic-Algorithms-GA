from ga import GA

# Número de indivíduos por geração
POPULATION_SIZE = 100
  
# Genes válidos
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP 
QRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}''' # 88 caracteres
  
# Objetivo
TARGET = "Eu gosto de tecnologia" # 22 caracteres


ga = GA(POPULATION_SIZE, GENES, TARGET)
ga.run()