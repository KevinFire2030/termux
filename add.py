def sum_to_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
        print(f"1부터 {i}까지의 합: {total}")
    return total

# 1부터 10000까지의 합 계산
final_sum = sum_to_n(10000)

print(f"\n최종 결과: 1부터 10000까지의 합은 {final_sum}입니다.")
