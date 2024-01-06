def find_needle(haystack):
    for i in haystack:
        if i == 'needle':
            return f"found the needle at position {haystack.index('needle')}"