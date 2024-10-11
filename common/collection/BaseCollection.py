from bson import ObjectId


class BaseCollection:
    """
    对于 `MongoDB` 的 `Collection` 的基础实体类

    :param _id: `str` - `MongoDB` 的 `Collection` 的 `_id`
    """

    _id: ObjectId
    __collection_name__: str

    def __init__(self, _id: str, *args, **kwargs):
        self._id = _id

    def set_id(self, _id: str | ObjectId):
        if type(_id) == str:
            self._id = ObjectId(_id)
        elif type(_id) == ObjectId:
            self._id = _id
        else:
            raise TypeError(f"Type of _id must be str or ObjectId, but got {type(_id)}")
