def any_arrows(arrows):
    for arrow in arrows:
        if 'damaged' in arrow and not arrow['damaged']:
            return True
    return False

#NOT FINISHED