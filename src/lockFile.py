"""MEG system lockfile parser

Can be used to parse the lock file and preform operations on the lockfile
Only interacts with the lockfile, does not preform any git actions
Does not check permissions before actions are taken

All file paths are relitive to the repository directory
Working directory should be changed by the git module
"""

import json
import os.path
import time

class LockFile:
    """Parse a lockfile and preform locking operations
    """

    def __init__(self, filepath):
        """Open a lockfile and initalize class with it
        Args:
            filepath (string): path to the lockfile
        """
        self.update(filepath)

    def addLock(self, filepath, username):
        """Adds the lock to the lockfile
        Args:
            filepath (string): path to the file to lock
            username (string): name of locking user
        """
        self._lockData["locks"].append({
            "file": filepath,
            "user": username,
            "date": time.time()
        })
        json.dump(self._lockData, open(self._filepath, 'w'))

    def removeLock(self, filepath):
        """Remove any lock for the given file
        Args:
            filepath (string): path to the file to unlock
        """
        for entry in self._lockData["locks"]:
            if(entry["file"] == filepath):
                self._lockData["locks"].remove(entry)
        json.dump(self._lockData, open(self._filepath, 'w'))

    def findLock(self, filepath):
        """Find if there is a lock on the file
        Args:
            filepath (string): path of file to look for
        Returns:
            (dictionary): lockfile entry for the file
            (None): There is no entry
        """
        for entry in self._lockData["locks"]:
            if(entry["file"] == filepath):
                return entry
        return None

    @property
    def locks(self):
        """Returns the list of locks
        """
        return self._lockData["locks"]

    def update(self, filepath=None):
        """Updates this object with the current data in the lockfile

        If the file doesn't exist, create one

        Args:
            filepath (string): path to the lockfile
        """
        if(filepath is None):
            filepath = self._filepath
        else:
            self._filepath = filepath
            if(not os.path.exists(filepath)):
                self._locks = {
                    "comment": "MEG System locking file, avoid manually editing",
                    "locks": []
                }
                newFile = open(filepath, 'w')
                newFile.write(json.dumps(self._locks))
                newFile.close()

        try:
            self._lockData = json.load(open(filepath))
        except json.decoder.JSONDecodeError:
            #Lock file couldn't be found, or is corrupted
            #TODO: do something here
            pass


        

