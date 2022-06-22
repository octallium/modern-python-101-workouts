def swap_case(my_string: str) -> str:
    return "".join(
        [s.capitalize() if s.islower() == True else s.lower() for s in my_string]
    )


print(swap_case("WwW.OctaLliUm.coM"))
