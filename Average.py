def average(arr):
   distinct_heights = set(arr)
   total_sum = sum(distinct_heights)
   count = len(distinct_heights)
   avg = total_sum / count
   return round(avg, 3)



if __name__ == "__main__":
  arr = [154,161,167,170,171,174,176,182]
  result = average(arr)
  print(result)