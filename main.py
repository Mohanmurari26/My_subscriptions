monday = {"TOI": 3, "HINDU": 2.5, "ET": 4, "BM": 1.5, "HT": 2}
tuesday = {"TOI": 3, "HINDU": 2.5, "ET": 4, "BM": 1.5, "HT": 2}
wednesday = {"TOI": 3, "HINDU": 2.5, "ET": 4, "BM": 1.5, "HT": 2}
thursday = {"TOI": 3, "HINDU": 2.5, "ET": 4, "BM": 1.5, "HT": 2}
friday = {"TOI": 3, "HINDU": 2.5, "ET": 4, "BM": 1.5, "HT": 2}
saturday = {"TOI": 5, "HINDU": 4, "ET": 4, "BM": 1.5, "HT": 4}
sunday = {"TOI": 6, "HINDU": 4, "ET": 10, "BM": 1.5, "HT": 4}
week_list = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]

weekly_budget = int(input())
sum = 0
for i in week_list:
    result = set()
    for j in list(i.keys()):
            sum += i[j]

if int(sum) >= weekly_budget:
    print("time is not sufficient to solve this!!!")


