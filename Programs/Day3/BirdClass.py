from abc import abstractmethod


class Bird:
    fly = True

    def noise(self):
        print("Birdnoise")

    babies = 0

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False


class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        print("peckpeck")


class Dodo(Bird):
    fly = False
    extinct = True

    def eat(self):
        print("nom nom")

    def reproduce(self):
        if self.extinct == False:
            self.babies += 1
        else:
            print("No more Dodo's")


owly = Owl()
doduo = Dodo()

owly.eat()
owly.noise()
owly.reproduce()
print(owly.babies)

doduo.eat()
doduo.reproduce()

