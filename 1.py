def vytvor_soubor_zamestnanci(slovnik, nazev_souboru):
    with open(nazev_souboru, 'w') as soubor:
        for zamestnanec_id, zamestnanec_info in slovnik.items():
            soubor.write(f'ID zaměstnance: {zamestnanec_id}\n')
            soubor.write(f'Jméno: {zamestnanec_info["jmeno"]}\n')
            soubor.write(f'Příjmení: {zamestnanec_info["prijmeni"]}\n')
            soubor.write(f'Pozice: {zamestnanec_info["pozice"]}\n')
            soubor.write(f'Email: {zamestnanec_info["email"]}\n')
            soubor.write(f'Kancelář: {zamestnanec_info["kancelar"]}\n')
            soubor.write('-' * 30 + '\n')

zamestnanci = {
    1: {
        'jmeno': 'Alexandr',
        'prijmeni': 'Dulovec',
        'pozice': 'borec',
        'email': 'alexandr.dulovec@student.ossp.cz',
        'kancelar': 'A101'
    },
    2: {
        'jmeno': 'Filip',
        'prijmeni': 'Zatáčka',
        'pozice': 'Řidič',
        'email': 'filip.zatacka@gmail.com',
        'kancelar': 'A101'
    },
    3: {
        'jmeno': 'Milan',
        'prijmeni': 'Švanda',
        'pozice': 'Bezdomovec',
        'email': 'milan.svanda@gmail.com',
        'kancelar': 'B202'
    }
}

vytvor_soubor_zamestnanci(zamestnanci, 'zamestnanci.txt')
