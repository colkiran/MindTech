
l1 = list(range(1, 31))
print(f"l1 :{l1}")

print("-" * 60)
res_even = list(filter(lambda x: x % 2 == 0, l1))
print(f"Even :{res_even}")

print("-" * 60)
res_odd = list(filter(lambda x: x % 2 == 1, l1))
print(f"Even :{res_odd}")

print("-" * 60)
st = "the quick brown fox jumps over the lazy dog"
res = list(filter(lambda wrd : len(wrd) > 3, st.split()))
print(f"res :{res}")
