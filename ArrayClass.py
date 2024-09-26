# Graeson Brickner

# U 2 Lab 2
# BAZINGA

import ctypes

class DynamicArray:
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)

  def __make_array(self, c):
    """return new array with capacity c"""
    return (c * ctypes.py_object)()
  
  def append(self, toAppend):
    if self.__n + 1 > self.__capacity:
      self.__resize()

    self.__A[self.__n] = toAppend
    self.__n += 1

  def __resize(self):
    newArray = self.__make_array(self.__capacity * 2)
    for i, item in enumerate(self.__A):
      newArray[i] = item
    self.__A = newArray

    self.__capacity *= 2
  
  def get_cap(self):
    return self.__capacity

  def __str__(self):
    if self.__n == 0:
      return "[]"

    out = '['
    for i, element in enumerate(self.__A):
      try:
        out += str(element) + ', '
        temp = self.__A[i+1]
      except:
        break
    return out[:-2] + ']'

  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
      raise IndexError("invalid index")
    
    return self.__A[k]

  def __len__(self):
    return self.__n