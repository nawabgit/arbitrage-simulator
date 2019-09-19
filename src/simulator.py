class BetSimulator:

    def __init__(self, stake, samples, odds_diff, random=False):
        """
        :param stake: initial stake for strategy
        :param samples: n number of bet attempts
        :param odds_diff: the maximum odds we will take advantages of
                         e.g. 2.1 betfair, 2.2 bookie = odds_diff of 0.1
        :param random: if odd_diff is a static value or a range
        """

        self.stake = stake
        self.samples = samples
        self.odds_diff = odds_diff
        self.random = random

    def simulate(self):
        pass

    def kelly_criterion(self):
        pass

