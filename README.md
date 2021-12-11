# ReduceDimension

### Example Program

```python
from ReduceDimensions import ReduceDimensions

if __name__ == "__main__":
  arr = [
        [1,2,3,0],
        [4,5,6,3],
        [7,8,9,5]
  ]

  rd = ReduceDimensions(arr)
  print(rd.get(2), rd.getLastReduced(), rd.shape(), rd.dim(), sep="\n")
  ```
  
### Output
  
```powershell
(2, 3) (3, 4)
[[ -7.36231979  -9.07838309 -10.7944464   -4.96355392]
 [  2.70115667   2.46636584   2.231575     2.20525111]]
[[ -7.36231979  -9.07838309 -10.7944464   -4.96355392]
 [  2.70115667   2.46636584   2.231575     2.20525111]]
(2, 4)
2
```

### Exceptions

Resultant dimesnion will be in range from 1 to number of rows in given matrix. If mentioned other numbers are mentioned, the program throws Exception.
