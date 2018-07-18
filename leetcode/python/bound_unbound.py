IND = 'ON'


class Kls(object):
    def __init__(self, data):
        self.data = data

    def checkind():
        return IND == 'ON'

    def do_reset(self):
        if self.checkind():
            print('Reset done for: %s' % self.data)

    def set_db(self):
        if self.checkind():
            print('DB connection made for: %s' % self.data)


print(Kls.checkind())
# ik1 = Kls(24)
# print(ik1.checkind())