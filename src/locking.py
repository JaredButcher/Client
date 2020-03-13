"""MEG system file locking

To be used to lock files, unlock files, override locks, and view locks
Will conferm user roles and preform required git operations
"""

from lockFile import LockFile

class Locking:
    def __init__(self, user, roles, gitManager):
        pass

    def addLock(self, filepath):
        pass

    def removeLock(self, filepath):
        pass

    def findLock(self, filepath):
        pass

    def getLocks(self):
        pass