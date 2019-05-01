# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:13:40 2019

@author: Mateusz
"""

from common import square, cube, darkBlue, white, width, height
import numpy as np
import pygame as pg
import sys


class Render():
    def __init__(self, width=800, height=600):
        """Create a window with given resolution"""
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        self.screen.fill(darkBlue)

        self.vertices = cube * 100

        self.thetaX = 0
        self.thetaY = 0
        self.thetaZ = 0

    def scale(self, figure, factor):
        figure * factor

    def translate(self, figure, translate=[width / 2, height / 2]):
        for vertex in figure:
            vertex[0] += translate[0]
            vertex[1] += translate[1]

    def create_rotation_matrix_X(self, theta=0.0):
        return np.array([
                [1, 0, 0],
                [0, np.cos(theta), -np.sin(theta)],
                [0, np.sin(theta), np.cos(theta)]
                ])

    def rotateX(self, vertex):
        """
        From linear algebra we get:
        (A * B^T)^T = B^T^T * A^T = B * A^T
        """
        return np.matmul(vertex, self.create_rotation_matrix_X(self.thetaX).T)

    def create_rotation_matrix_Y(self, theta=0.0):
        return np.array([
                [np.cos(theta), 0, np.sin(theta)],
                [0, 1, 0],
                [-np.sin(theta), 0, np.cos(theta)]
                ])

    def rotateY(self, vertex):
        """
        From linear algebra we get:
        (A * B^T)^T = B^T^T * A^T = B * A^T
        """
        return np.matmul(vertex, self.create_rotation_matrix_Y(self.thetaY).T)

    def create_rotation_matrix_Z(self, theta=0.0):
        return np.array([
                [np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]
                ])

    def rotateZ(self, vertex):
        """
        From linear algebra we get:
        (A * B^T)^T = B^T^T * A^T = B * A^T
        """
        return np.matmul(vertex, self.create_rotation_matrix_Z(self.thetaZ).T)

    def orthogonal_projection_matrix(self):
        self.projectionZ = np.array([[1, 0, 0],
                                    [0, 1, 0]])

    def perspective_projection_matrix(self):
        pass

    def draw(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill(darkBlue)

            for vertex in self.vertices:
                x, y, z = self.rotateY(vertex)
                self.screen.fill(white, (x, y, 8, 8))

            self.thetaX += 0.001
            self.thetaY += 0.001
            self.thetaZ += 0.001

            pg.display.flip()
