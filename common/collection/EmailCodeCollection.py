from common.collection import BaseCollection


class EmailCodeCollection(BaseCollection):
    """
    邮箱验证码集合

    :param user_id: 用户id
    :param code: 验证码
    :param expire_time: 过期时间

    """

    __collection_name__ = "email_code"

    code: str
    expire_time: int  #  过期时间

    def __init__(self, user_id, code, expire_time, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.code = code
        self.expire_time = expire_time

    def _repr_(self):
        """
        用于返回一个对象的“官方”字符串表示
        """
        return f"<EmailCodeCollection {str(self._id)}>"
