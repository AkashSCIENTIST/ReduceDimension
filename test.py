from ReduceDimensions import ReduceDimensions

if __name__ == "__main__":
  arr = [
        [1,2,3,0],
        [4,5,6,3],
        [7,8,9,5]
  ]

  rd = ReduceDimensions(arr)
  print(rd.get(2), rd.getLastReduced(), rd.shape(), rd.dim(), sep="\n")
