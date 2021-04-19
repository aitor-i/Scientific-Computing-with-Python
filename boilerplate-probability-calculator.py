import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for key, val in kwargs.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, number_balls):
        self.balls = list()
        if number_balls >= len(self.contents):
            self.balls = self.contents

        else:
            for i in range(number_balls):
                balls_in_hat = len(self.contents)
                ball_to_draw = random.randint(0, balls_in_hat - 1)
                self.balls.append(self.contents[ball_to_draw])
                del self.contents[ball_to_draw]

        return self.balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = int(num_experiments)
    M = 0

    for i in range(N):

        print('This is the {} try'.format(i))

        copy_hat = copy.deepcopy(hat)
        draw_balls = copy_hat.draw(num_balls_drawn)
        print(draw_balls)
        check_list = []

        for colour, num in expected_balls.items():
            x = [ball for ball in draw_balls if colour in ball]
            if len(x) >= num:
                check_list.append(True)
            else:
                check_list.append(False)
        if set(check_list) == {True}:
            M = M + 1
            print('ok')

    probability = M / N
    return probability


hat = Hat(red=5, orange=4, black=1, blue=8, pink=2, striped=9)

print(experiment(hat=hat, expected_balls={"red": 2, "blue": 1}, num_balls_drawn=7, num_experiments=10000))
