def count_distinct_stamps(stamps):
    distinct_stamps = set()
    for stamp in stamps:
        distinct_stamps.add(stamp)
    return len(distinct_stamps)
if __name__ == "__main__":
   N = int(input().strip())
   stamps = []
   for _ in range(N):
        stamp = input().strip()
        stamps.append(stamp)
   result = count_distinct_stamps(stamps)
   print(result)
