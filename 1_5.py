jest_adminem = False
jest_czlonkiem_grupy = True 
zasob_jest_zablokowany = True

if jest_adminem == True or jest_czlonkiem_grupy == True:
    zasob_jest_zablokowany = False
else:
    pass

if zasob_jest_zablokowany == False:
    print("Przyznano dostep do zasobu.")
else:
    print("Odmowa dostepu do zasobu.")
