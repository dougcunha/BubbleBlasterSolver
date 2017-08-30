from board import Board
from show import showSolution
import solution
import random
from evaluators import evaluatorsList


class Ret():
    def __init__(self, func, touchs, score):
        self.touchs = touchs
        self.score = score
        self.func_name = func.func_name

    def __repr__(self):
        """
        Representacao da string.
        """
        return "%s - %s => %d" % (self.func_name, str(self.touchs), self.score)


def test_solution(max_touchs=6, game=None):
    b = Board(game, max_touchs)
    max_iters = 8000
    done = False
    solutions = []
    while max_iters > 0:
        touchs = []
        b.reset()
        f = random.choice(evaluatorsList)
        for i in range(0, max_touchs):
            touch = solution.getTouch(b.clone(), f)
            if not touch:
                continue
            touchs.append(touch)
            score = b.touch(touch, False)
            if score == 0:
                break
                done = True
        max_iters -= 1
        solutions.append(Ret(f, touchs, score))
        if done:
            break

    best = min(solutions, key=lambda x: x.score)
    worst = max(solutions, key=lambda x: x.score)
    print "Best -> " + str(best)
    print "Worst -> " + str(worst)
    showSolution(b, best.touchs)

if __name__ == '__main__':
    game = """
    0 0 3 1 1
    1 4 1 4 2
    3 3 2 3 0
    1 4 4 0 2
    2 4 1 2 2
    3 3 1 3 0
    """
    test_solution(game=game, max_touchs=3)
