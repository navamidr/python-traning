Score={"alice":85,"Bob":90,"charlie":78}
print("highest:",max(Score,key=Score.get))
print("lowest:",min(Score,key=Score.get))