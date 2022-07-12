from msilib import init_database


class Urban:

    country = "india"

class Rural:

    state = "uttar pradesh"
    point = 0

    def upgradeRate(self):
        self.point = self.point + 1

class New (Urban, Rural):

    name = "shank"

n = New()
print(n.state)
n.upgradeRate()
print(n.point)