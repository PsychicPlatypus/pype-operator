from pipe import pypeline


@pypeline
def test():
    stuff = "dzenis"

    stuff >> str.capitalize() >> str.upper >> str.lower >> print()


test()
