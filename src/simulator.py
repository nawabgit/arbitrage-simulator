from decimal import Decimal


class BetSimulator:

    def __init__(self, bankroll, samples, odds_diff, random=False):
        """
        :param bankroll: initial stake for strategy
        :param samples: n number of bet attempts
        :param odds_diff: the maximum odds we will take advantages of
                         e.g. 2.1 betfair, 2.2 bookie = odds_diff of 0.1
        :param random: if odd_diff is a static value or a range
        """

        self.bankroll = Decimal(bankroll)
        self.samples = samples
        self.odds_diff = odds_diff
        self.random = random

    def simulate(self):
        pass

    def kelly_criterion(self, b, p, weight=0.5):
        """
        Applies the kelly criterion formula with a modest 1/2 (modifiable) weighting
        :param b the decimal odds proposed by the bookie
        :param p the 'real' odds of match from 0 to 1
        :param weight the 'safeness' multiplier applied to reduce the risk

        :return: the amount that should be staked on the bet
        """

        b = b - 1
        q = 1 - p

        weighted_kc = Decimal(weight) * Decimal(((b * p) - q) / b)

        return round(self.bankroll * weighted_kc, 2)

