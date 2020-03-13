"""MEG system file locking

To be used to lock files, unlock files, override locks, and view locks
Will confirm user roles and preform required git operations

All file paths are relitive to the repository directory
Working directory should be changed by the git module

TODO: add interaction with git and role modules
"""

from lockFile import LockFile

LOCKFILE_NAME = ".meglock"

class Locking:
    """Used to prefrom all locking operations
    To be used to lock files, unlock files, override locks, and view locks
    Will confirm user roles and preform required git operations
    """

    def __init__(self, user, roles, repoManager):
        """
        Args:
            user (string): username of user
            roles (object): currenlty unimplented object that manages roles TODO
            repoManager (object): currenlty unimplented object that manages git TODO
        """
        self._lockFile = LockFile(LOCKFILE_NAME)
        self.user = user
        self.roles = roles
        self.repoManager = repoManager

    def addLock(self, filepath):
        """Sync the repo, adds the lock, sync the repo
        Args:
            filepath (string): path to the file to lock
        Returns:
            (bool): was lock sucessfuly added
        """
        self.updateLocks()
        if(not self._lockFile.findLock(filepath) is None):
            return False
        else:
            self._lockFile.addLock(filepath, self.user)
            self.updateLocks()
            return True
        

    def removeLock(self, filepath):
        """Sync the repo, remove a lock from a file, and sync again
        Args:
            filepath (string): path to file to unlock
        Returns:
            (bool): is there still a lock (was the user permitted to remove the lock)
        """
        self.updateLocks()
        lock = self._lockFile.findLock(filepath)
        if(lock is None):
            return True
        elif(lock["user"] == self.user):
            self._lockFile.removeLock(filepath)
        else:
            if(False): #TODO check that user role can remove other user's locks
                self._lockFile.removeLock(filepath)
            else:
                return False
        self.updateLocks()
        return True
        

    def findLock(self, filepath):
        """Find if there is a lock on the file, does not automatily sync the lock file
        Args:
            filepath (string): path of file to look for
        Returns:
            (dictionary): lockfile entry for the file
            (None): There is no entry
        """
        return self._lockFile.findLock(filepath)

    @property
    def locks(self):
        return self._lockFile.locks

    def updateLocks(self):
        #TODO: sync
        self._lockFile.update()