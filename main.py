import numpy as np
from vpython import *


def ptc(r, t, z):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return [x, y, z]


def t_prism(r=1., l=5., d_th=np.pi * 5. / 6.):
    # r = radius of base triangle
    # l = length of strut
    # d_th = rotational difference between top and bottom triangle bases
    th_0 = np.pi * 2. / 3.
    h = np.sqrt(l ** 2 - 2 * r * r * (1 - np.cos(d_th)))
    A, A_p = vector(r, 0, -h / 2), vector(r * np.cos(d_th), r * np.sin(d_th), h / 2)
    B, B_p = vector(r * np.cos(th_0), r * np.sin(th_0), -h / 2), vector(r * np.cos(d_th + th_0),
                                                                        r * np.sin(d_th + th_0), h / 2)
    C, C_p = vector(r * np.cos(-th_0), r * np.sin(-th_0), -h / 2), vector(r * np.cos(d_th - th_0),
                                                                          r * np.sin(d_th - th_0), h / 2)

    # Struts
    tensegrity = compound([
        cylinder(pos=A, axis=A_p - A, radius=0.1),
        cylinder(pos=B, axis=B_p - B, radius=0.1),
        cylinder(pos=C, axis=C_p - C, radius=0.1),

        # bottom/top tendons
        cylinder(pos=A, axis=B - A, radius=0.02, color=color.red),
        cylinder(pos=B, axis=C - B, radius=0.02, color=color.red),
        cylinder(pos=C, axis=A - C, radius=0.02, color=color.red),

        cylinder(pos=A_p, axis=B_p - A_p, radius=0.02, color=color.green),
        cylinder(pos=B_p, axis=C_p - B_p, radius=0.02, color=color.green),
        cylinder(pos=C_p, axis=A_p - C_p, radius=0.02, color=color.green),

        # side tendons
        cylinder(pos=A, axis=C_p - A, radius=0.02, color=color.blue),
        cylinder(pos=B, axis=A_p - B, radius=0.02, color=color.blue),
        cylinder(pos=C, axis=B_p - C, radius=0.02, color=color.blue)
    ])
    return tensegrity


def animated_tensegrity():
    scene.width = 400
    scene.height = 525
    # scene.camera.pos = vector(5, 5, 3)
    # scene.camera.axis = vector(-1, -1, 0)
    # scene.camera.up = vector(0, 0, 1)


    r = 2.
    l = 5.
    d_th = 0.
    th_0 = np.pi * 2. / 3.
    h = np.sqrt(l ** 2 - 2 * r * r * (1 - np.cos(d_th)))
    A, A_p = vector(r, 0, 0), vector(r * np.cos(d_th), r * np.sin(d_th), h)
    B, B_p = vector(r * np.cos(th_0), r * np.sin(th_0), 0), vector(r * np.cos(d_th + th_0),
                                                                   r * np.sin(d_th + th_0), h)
    C, C_p = vector(r * np.cos(-th_0), r * np.sin(-th_0), 0), vector(r * np.cos(d_th - th_0),
                                                                     r * np.sin(d_th - th_0), h)

    # axis, not animated
    cylinder(pos=vector(-5, 0, 0), axis=vector(10, 0, 0), radius=0.005, color=color.orange)
    cylinder(pos=vector(0, -5, 0), axis=vector(0, 10, 0), radius=0.005, color=color.orange)
    cylinder(pos=vector(0, 0, -5), axis=vector(0, 0, 10), radius=0.005, color=color.orange)

    ref = cylinder(pos=vector(0, 0, h), axis=A_p - vector(0, 0, h), radius=0.005, color=color.yellow)
    # struts, will be animated
    strut_A = cylinder(pos=A, axis=A_p - A, radius=0.1)
    strut_B = cylinder(pos=B, axis=B_p - B, radius=0.1)
    strut_C = cylinder(pos=C, axis=C_p - C, radius=0.1)

    # bottom tendons, will not need to be animated
    cylinder(pos=A, axis=B - A, radius=0.02, color=color.red)
    cylinder(pos=B, axis=C - B, radius=0.02, color=color.red)
    cylinder(pos=C, axis=A - C, radius=0.02, color=color.red)

    # top tendons, will get animated
    ttendon_A = cylinder(pos=A_p, axis=B_p - A_p, radius=0.02, color=color.green)
    ttendon_B = cylinder(pos=B_p, axis=C_p - B_p, radius=0.02, color=color.green)
    ttendon_C = cylinder(pos=C_p, axis=A_p - C_p, radius=0.02, color=color.green)

    # side tendons, will get animated
    stendon_A = cylinder(pos=A, axis=C_p - A, radius=0.02, color=color.blue)
    stendon_B = cylinder(pos=B, axis=A_p - B, radius=0.02, color=color.blue)
    stendon_C = cylinder(pos=C, axis=B_p - C, radius=0.02, color=color.blue)
    for i in range(181):
        rate(30)
        d_th = 10. * np.pi / 6. * i / 180
        h = np.sqrt(l ** 2 - 2 * r * r * (1 - np.cos(d_th)))
        A, A_p = vector(r, 0, 0), vector(r * np.cos(d_th), r * np.sin(d_th), h)
        B, B_p = vector(r * np.cos(th_0), r * np.sin(th_0), 0), vector(r * np.cos(d_th + th_0),
                                                                       r * np.sin(d_th + th_0), h)
        C, C_p = vector(r * np.cos(-th_0), r * np.sin(-th_0), 0), vector(r * np.cos(d_th - th_0),
                                                                         r * np.sin(d_th - th_0), h)

        strut_A.pos = A
        strut_A.axis = A_p - A
        strut_B.pos = B
        strut_B.axis = B_p - B
        strut_C.pos = C
        strut_C.axis = C_p - C

        ttendon_A.pos = A_p
        ttendon_A.axis = B_p - A_p
        ttendon_B.pos = B_p
        ttendon_B.axis = C_p - B_p
        ttendon_C.pos = C_p
        ttendon_C.axis = A_p - C_p

        stendon_A.pos = A
        stendon_A.axis = C_p - A
        stendon_B.pos = B
        stendon_B.axis = A_p - B
        stendon_C.pos = C
        stendon_C.axis = B_p - C

        ref.pos = vector(0, 0, h)
        ref.axis = A_p - vector(0, 0, h)


def main():
    animated_tensegrity()


if __name__ == '__main__':
    main()
