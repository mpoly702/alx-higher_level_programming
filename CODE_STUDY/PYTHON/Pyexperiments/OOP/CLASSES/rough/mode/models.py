#!/usr/bin/env python3
import datetime
import uuid
#A Base class
class BaseModel:
    def __init__(self, id=None, created_at=None, updated_at=None):
        self._id = id
        self._created_at = created_at
        self._updated_at = updated_at
        self.id = None
        self.created_at = None
        self.updated_at = None
    
    def _get_id(self) -> uuid.UUID:
        return self._id
    
    def _set_id(self, idd: uuid.UUID = None) -> None:
        if idd is None:
            idd = uuid.uuid4()
        if self._id is None:
            self._id = idd
    id = property(_get_id, _set_id, 
                  "this property updates and retrieves id")

    def _get_created_at(self) -> datetime.datetime:
        return self._created_at
    
    def _set_created_at(self, time: datetime.datetime = None) -> None:
        if time is None:
            time = datetime.datetime.now()
        if self._created_at is None:
            self._created_at = time
    created_at = property(_get_created_at, _set_created_at, 
                            "this property updates and retrieves current time")
    
    def _get_updated_at(self) -> datetime.datetime:
        return self._updated_at
    
    def _set_updated_at(self, update: datetime.datetime = None) -> None:
        if update is None:
            update = datetime.datetime.now()
        if self._updated_at is None:
            self._updated_at = update
    updated_at = property(_get_updated_at, _set_updated_at, "this property sucks")

user = BaseModel()
print("ID:", user.id)
print("Created at:", user.created_at)
print("Updated at:", user.updated_at)
