from turing import TuringMachine

##########
# Inverter
##########

inverter_gamma = '01#'
inverter_sigma = '01#'
inverter_delta = \
    {('init', '0') : ('init', '1', 'right'), 
     ('init', '1') : ('init', '0', 'right'), 
     ('init', '#') : ('accept', '0', 'left'), 
     }

inverter = TuringMachine(inverter_sigma, 
                         inverter_gamma, 
                         inverter_delta)
