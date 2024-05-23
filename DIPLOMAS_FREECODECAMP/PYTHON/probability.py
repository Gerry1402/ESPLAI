import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color in balls:
            self.contents += [color]*balls[color]

    def draw(self, number):
        if number > len(self.contents):
            all = self.contents
            self.contents = []
            return all
        drawn_balls = random.sample(self.contents, number)
        for color in drawn_balls:
            self.contents.remove(color)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #print ('Balls: ',', '.join(hat.contents))
    #print ('Expected balls: ', expected_balls)
    #print ('Number: ',num_balls_drawn, '\tExperiments: ', num_experiments)
    matches = 0
    count = 0
    num_balls = len(hat.contents)

    for _ in range(num_experiments):
        new_hat=copy.deepcopy(hat)
        there_are_balls = True
        while there_are_balls:
            balls_drawn = new_hat.draw(num_balls_drawn)
            if balls_drawn == [] or len(balls_drawn) < num_balls_drawn:
                there_are_balls = False
                if num_balls_drawn >= num_balls:
                    return 1
                break
            count += 1
            mem = True
            for color, number in expected_balls.items():
                for col in balls_drawn:
                    if col == color:
                        number -= 1
                        if number == 0:
                            break
                if number != 0:
                    mem = False
                    break
            if mem:
                matches += 1
    #print ('Probability: ',matches / count)
    #print()
    return matches / count

hat = Hat(black = 6, red = 4, green = 3)
probability = experiment(hat = hat,
                  expected_balls = {"red":2,"green":1},
                  num_balls_drawn = 5,
                  num_experiments = 2000)
        

