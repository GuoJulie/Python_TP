import datetime

class Date:

    def __init__(self, string_date):

        if "/" in string_date:
            self.day = int(string_date.split('/')[0])
            self.month = int(string_date.split('/')[1])
            self.year = int(string_date.split('/')[2])

    # surcharge ==
    def __eq__(self,object):
        return self.__dict__ == object.__dict__

    # surcharge <
    def __lt__(self, object):
        if self.year < object.year or (self.year == object.year and self.month < object.month) \
                or (self.year == object.year and self.month == object.month and self.day < object.day):
            return True
        else:
            return False


class Etudiant:

    def __init__(self, prenom, nom, anniversaire):
        self.prenom = prenom
        self.nom = nom
        self.anniversaire = anniversaire

    def adresselec(self):
        adresse = self.prenom.lower() + '.' + self.nom.lower() + '@etu.univ-tours.fr'
        return adresse

    def age(self):
        self.year = self.anniversaire.year
        datestring = datetime.date.today()
        current_year = int(str(datestring).split('-')[0])
        calculer_age = current_year - self.year
        return str(calculer_age)



if __name__ == '__main__':
    date_1 = Date('26/04/1994')
    date_2 = Date('26/04/1996')
    print(date_1.__eq__(date_2))
    print(date_1.__lt__(date_2))

    etudiant_1 = Etudiant('XIAOQING', 'Guo', date_1)
    etudiant_2 = Etudiant('nn', 'MM', date_2)
    print(etudiant_1.adresselec() + ': ' + etudiant_1.age() + ' ans')
    print(etudiant_2.adresselec() + ': ' + etudiant_2.age() + ' ans')

