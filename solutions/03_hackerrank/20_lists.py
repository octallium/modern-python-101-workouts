N = int(input())

my_list: list[int] = []


for _ in range(N):
    op: list[str] = input().split()
    cmd = op[0]
    args = tuple(map(int, (op[1:])))

    if cmd == "print":
        print(my_list)
    else:
        stmt = f"my_list.{cmd}{args}"
        # print(stmt)
        eval(stmt)
