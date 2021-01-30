import pytest
from flood_fill import Img

def test_img_init():
    data = [[1, 0, 0],
            [0, 1, 0], 
            [0, 3, 2]]
    img1 = Img(data)
    assert img1.img == data

def test_is_pos_valid():
    data = [[1, 0, 0],
            [0, 1, 0], 
            [0, 3, 2]]
    img1 = Img(data)
    assert img1.is_pos_valid((1, 1)) == True

def test_neighboors():
    data = [[1, 0, 0],
            [0, 1, 0], 
            [0, 3, 2]]
    img1 = Img(data)
    assert img1.get_neighboors((0, 1)) == [(0, 0), (0, 2), (1, 1)]

def test_inplace_flood_fill():
    data = [[1, 0, 0],
            [0, 1, 0], 
            [0, 3, 2]]
    img1 = Img(data)
    tata = [[1, 7, 7],
            [0, 1, 7], 
            [0, 3, 2]]
    img1.inplace_flood_fill((0, 1), 7) 
    assert img1.img == tata

def test_inplace_flood_fill2():
    data = [[1, 0, 0],
            [0, 1, 0], 
            [0, 0, 0]]
    img1 = Img(data)
    tata = [[1, 7, 7],
            [7, 1, 7], 
            [7, 7, 7]]
    img1.inplace_flood_fill((0, 1), 7) 
    assert img1.img == tata

def test_inplace_flood_fill_identity():
    data = [[1, 0, 0],
            [0, 1, 0], 
            [0, 0, 0]]
    img1 = Img(data)
    img1.inplace_flood_fill((1, 1), 1) 
    assert img1.img == data

