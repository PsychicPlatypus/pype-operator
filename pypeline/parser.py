def parse_line(str_: str) -> str:
    if "|>" not in str_:
        return str_
    str_arr = [i for i in str_]
    for i in range(len(str_arr) - 1):
        if str_arr[i] + str_arr[i + 1] == "|>":
            before_pipe = str_arr[:i]
            first_parenthesis = str_arr.index("(")

            bef_par_sa = str_arr[: first_parenthesis + 1]
            aft_par_sa = str_arr[first_parenthesis + 1 :]
            str_arr = bef_par_sa + before_pipe + aft_par_sa
            str_arr = ["" if j <= i + 1 else str_arr[j] for j in range(len(str_arr))]

    return "".join(str_arr)


"""
0 |> abs()

->

abs(0)
"""
print(parse_line("0 |> abs() |> abs(0)"))
