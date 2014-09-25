__author__ = 'adamb'

from settings import *


def driveToUNC(p, switchToFwdSlash=False):
    """
    @param p: path
    @param switchToFwdSlash: RV requires forward slashes in rvlink:// when in browser mode
                             (if you want to keep the link readible)
    """
    for share, letter in DRIVE_MAP.iteritems():
        if letter in p:
            p = p.replace(letter, ('//'+SERVER+'/'+SHARES[share]))
            if switchToFwdSlash:
                p = p.replace('\\', '/')
            return p
    return p