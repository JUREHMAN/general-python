#information about basic particles

#charge of leptons
electric_charge =''
electric_charge_of_input_particle = ''
charged_leptons = ['electron', 'muon', 'tau']
charged_anti_leptons = ['positron', 'anti-muon', 'anti-tau']
neutral_leptons = ['electron-neutrino', 'electron-anti-neutrino', 'muon-neutrino', 'muon-anti-neutrino', 'tau-neutrino', 'tau-anti-neutrino']

#charge of baryons
charged_baryons = ['proton', 'sigma-plus']
charged_anti_baryons = ['anti-proton', 'anti-sigma-plus']

#charge of Mesons
#to be added
#to be added


# for particle in charged_leptons:
#     electric_charge == -1
# for particle in charged_anti_leptons:
#     electric_charge == 1
# for particle in neutral_leptons:
#     electric_charge == 0


input_particle = input("Please Enter the name of your initial particle:\n")
no_of_output_particles =int(input("Please Enter the number of final particles:\n"))
if no_of_output_particles == 2:
    p1 = input("Please Enter the name of your first final particle:\n")
    p2 = input("Please Enter the name of your second final particle:\n")
    #electric charge
    electric_charge_of_p1 = ''
    electric_charge_of_p2 = ''
    if input_particle == 'electron' or 'muon' or 'tau':
        electric_charge_of_input_particle == -1
    if input_particle =='positron' or 'anti-muon' or 'anti-tau':
        electric_charge_of_input_particle == +1
    if p1 == 'proton' or 'sigma' or 'pi-plus' or 'k-plus':
        electric_charge_of_p1 == +1
    if p2 == 'anti-proton' or 'sigma-minus' or 'k-minus':
        electric_charge_of_p2 == -1
    if electric_charge_of_input_particle == electric_charge_of_p1 + electric_charge_of_p2:
        print("Electric charge is conserved in your decay/cross section:\n")
    else:
        print("Their may be some electric charge conservation issue or some of limitation of this program\nplease stay connected for updats")




    #baryon number
    #lepton number

if no_of_output_particles == 3:
    pp1 = input("Please Enter the name of your first final particle:\n")
    pp2 = input("Please Enter the name of your second final particle:\n")
    pp3 = input("Please Enter the name of your third final particle:\n")
    #electric charge
    #baryon number
    #lepton number

if no_of_output_particles == 4:
    ppp1 = input("Please Enter the name of your first final particle:\n")
    ppp2 = input("Please Enter the name of your second final particle:\n")
    ppp3 = input("Please Enter the name of your third final particle:\n")
    ppp4 = input("Please Enter the name of your fourth final particle:\n")
    #electric charge
    #baryon number
    #lepton number

else:
    print("We are working to include other cases..\nplease be patient:")