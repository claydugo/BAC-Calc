from datetime import datetime

class Session:
    def __init__(self, sex, weight):
        self.sex = sex
        self.weight = lbs2kg(weight)
        self.startTime = datetime.now()
        self.gramsofAlc = 0
        print(f'Session started with {self.sex} gender and {self.weight:.0f} kg weight')

    def getSessionLength(self):
        diff = datetime.now() - self.startTime
        return diff.seconds / (60*60)

    def bac(self):
        if self.sex == 'female':
            tbw = 0.49
        elif self.sex == 'male':
            tbw = 0.58
        else:
            tbw = (0.49+0.58)/2

        # Average B60 from NHTSA (1994)
        b60 = 0.017
        return (self.gramsofAlc*0.806)/(self.weight*tbw*1000) * 100-(b60*self.getSessionLength())
    
    #https://sites.duke.edu/apep/files/2016/02/activity1a_teacher.pdf
    def drink(self, amount, ounces, percent):
        grams = amount * ounces * percent * 29.6 * 0.79
        self.gramsofAlc += grams
       
def lbs2kg(lbs):
    return lbs/2.205

if __name__ == "__main__":
    hmmst = Session('male', 190)
    hmmst.drink(2, 1.5, 0.40)
    print('Took 2 shots')
    hmmst.drink(1, 12, 0.05)
    print('Drank 1 beer')
    hmmst.drink(1, 16, 0.08)
    print('Drank 1 DIPA')
    print(f'Estimated BAC: {hmmst.bac():.4f}%')
