from Elements.Connector import *
from Elements.Tensegrity import *
from vpython import *
import numpy as np


def main():
    r, l = 1., 5.
    th_0 = np.pi * 2. / 3.
    d_th = np.pi * 5. / 6.
    h = np.sqrt(l ** 2 - 2 * r * r * (1 - np.cos(d_th)))

    positions = [[r, 0., -h / 2],  # A
                 [r * np.cos(d_th), r * np.sin(d_th), h / 2],  # A_p
                 [r * np.cos(th_0), r * np.sin(th_0), -h / 2],  # B
                 [r * np.cos(d_th + th_0), r * np.sin(d_th + th_0), h / 2],  # B_p
                 [r * np.cos(-th_0), r * np.sin(-th_0), -h / 2],  # C
                 [r * np.cos(d_th - th_0), r * np.sin(d_th - th_0), h / 2]]  # C_p
    # 0 = no connection, 1 = strut, 2 = tendon
    #               A  Ap B  Bp C  Cp
    connections = [[0, 1, 2, 0, 2, 2],   # A
                   [1, 0, 2, 2, 0, 2],   # Ap
                   [2, 0, 0, 1, 2, 0],   # B
                   [0, 2, 1, 0, 2, 2],   # Bp
                   [2, 0, 2, 2, 0, 1],   # C
                   [2, 2, 0, 2, 1, 0], ] # Cp

    T = Tensegrity([Node(p) for p in positions])
    T.set_connections(connections)
    tense = T.build_vpython_tensegrity()

    # a = Node([0., 0., 0.])
    # b = Node([1., 1., 1.])
    # c = Node([2., 2., 2.])
    # d = Node([3., 3., 3.])
    # strut = Strut(a, b)
    # tendon = Tendon(c, d)
    # strut.get_vpython_element()
    # tendon.get_vpython_element()


if __name__ == "__main__":
    main()
