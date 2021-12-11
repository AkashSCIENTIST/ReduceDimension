from numpy import array, matmul,cov
from numpy.linalg import svd

class ReduceDimensions():
  def __init__(self, arr):
    self.__array = array(arr)
  
  def get(self, ndims):
    if (ndims < 1):
      raise Exception("Dimension cannot be lesser than 1")

    self.__ndims = ndims
    covMatrix = cov(self.__array)
    U, S, VT = svd(covMatrix)

    if (ndims > U.shape[0]):
      raise Exception("Given Dimension exceeds Original Dimension")

    U_Reduced = U[:, 0:self.__ndims]
    A_Reduced = matmul(U_Reduced.T, self.__array)
    self.__reduced = A_Reduced
  
    return self.__reduced

  def getLastReduced(self):
    return self.__reduced

  def shape(self):
    return self.__reduced.shape

  def dim(self):
    return self.__ndims
