# ~/EJOR_2024_Tool/src/Algorithms/Enums/enum_algorithms.py

import enum


class EnumAlgorithms(enum.Enum):
    """
    This Enum shall contain and be updated with all the algorithms that we require
    """
    DP_MsC_T = 0
    S_CLUB = 1


if __name__ == "__main__":
    algo0 = EnumAlgorithms.DP_MsC_T
    algo1 = EnumAlgorithms.S_CLUB

    print(algo0)
    print(algo1)
    print("Equals" if algo0 == algo1 else "Different")
