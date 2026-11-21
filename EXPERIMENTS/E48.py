import itertools


class BayesianNetwork:
    """
    Network structure:
      Rain -> Sprinkler
      Rain -> WetGrass
      Sprinkler -> WetGrass
    """

    def __init__(self):
        # P(Rain)
        self.p_rain = {False: 0.8, True: 0.2}

        # P(Sprinkler | Rain)
        self.p_sprinkler = {
            False: {False: 0.6, True: 0.4},
            True: {False: 0.99, True: 0.01},
        }

        # P(WetGrass | Rain, Sprinkler)
        self.p_wet_grass = {
            (False, False): {False: 1.0, True: 0.0},
            (False, True): {False: 0.1, True: 0.9},
            (True, False): {False: 0.2, True: 0.8},
            (True, True): {False: 0.01, True: 0.99},
        }

    def joint_prob(self, rain: bool, sprinkler: bool, wet_grass: bool) -> float:
        return (
            self.p_rain[rain]
            * self.p_sprinkler[rain][sprinkler]
            * self.p_wet_grass[(rain, sprinkler)][wet_grass]
        )

    def query_prob(self, target_var: str, target_val: bool, evidence: dict[str, bool]) -> float:
        total_evidence = 0.0
        matching_target = 0.0

        for rain, sprinkler, wet_grass in itertools.product([False, True], repeat=3):
            assignment = {"Rain": rain, "Sprinkler": sprinkler, "WetGrass": wet_grass}
            if all(assignment[k] == v for k, v in evidence.items()):
                jp = self.joint_prob(rain, sprinkler, wet_grass)
                total_evidence += jp
                if assignment[target_var] == target_val:
                    matching_target += jp

        return matching_target / total_evidence if total_evidence > 0 else 0.0


def main():
    bn = BayesianNetwork()
    p_rain_given_wet = bn.query_prob("Rain", True, {"WetGrass": True})
    p_sprinkler_given_wet = bn.query_prob("Sprinkler", True, {"WetGrass": True})
    p_rain_given_wet_and_sprinkler = bn.query_prob(
        "Rain", True, {"WetGrass": True, "Sprinkler": True}
    )

    print(f"P(Rain=True | WetGrass=True) = {p_rain_given_wet:.4f}")
    print(f"P(Sprinkler=True | WetGrass=True) = {p_sprinkler_given_wet:.4f}")
    print(f"P(Rain=True | WetGrass=True, Sprinkler=True) = {p_rain_given_wet_and_sprinkler:.4f}")


if __name__ == "__main__":
    main()