score = int(input("점수를 입력하세요 (0~100): "))

if score >= 90:
    print("등급: A")
elif score >= 80:
    print("등급: B")
else:
    print("등급: C (노력이 필요합니다)")
