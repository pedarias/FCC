import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  arr = np.array(list).reshape((3,3))
  
  hor0 = arr[0]
  hor1 = arr[1]
  hor2 = arr[2]

  ver0 = arr[:,0]
  ver1 = arr[:,1]
  ver2 = arr[:,2]

  flattened = arr.copy()

  return {
  'mean': [[ver0.mean(), ver1.mean(), ver2.mean()], [hor0.mean(), hor1.mean(), hor2.mean()], flattened.mean()],
  'variance': [[ver0.var(), ver1.var(), ver2.var()], [hor0.var(), hor1.var(), hor2.var()], flattened.var()],
  'standard deviation': [[ver0.std(), ver1.std(), ver2.std()], [hor0.std(), hor1.std(), hor2.std()], flattened.std()],
  'max': [[ver0.max(), ver1.max(), ver2.max()], [hor0.max(), hor1.max(), hor2.max()], flattened.max()],
  'min': [[ver0.min(), ver1.min(), ver2.min()], [hor0.min(), hor1.min(), hor2.min()], flattened.min()],
  'sum': [[ver0.sum(), ver1.sum(), ver2.sum()], [hor0.sum(), hor1.sum(), hor2.sum()], flattened.sum()],
  }