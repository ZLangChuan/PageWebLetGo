from enum import Enum

from common.enums.StatusEnum import StatusEnum
from common.schemas.HyperDataSchema import HyperDataSchema


class HyperDataUtil:

    def __init__(self) -> None:

        self.__status = StatusEnum.SUCCESSES.value[0]
        self.__message = StatusEnum.SUCCESSES.value[1]
        self.__data = {}
        self.__order_dict = {}

    @property
    def hyper_data(self) -> HyperDataSchema:
        _dict = {
            "status": self.__status,
            "message": self.__message,
            "data": self.__data,
        }
        _dict.update(self.__order_dict)
        return HyperDataSchema().load(_dict)

    @property
    def status_message(self):
        return self.__status_message

    @status_message.setter
    def status_message(self, value: StatusEnum = StatusEnum.SUCCESSES):
        assert isinstance(value, Enum), "status_message must be StatusEnum"
        self.__status = value.value[0]
        self.__message = value.value[1]

    @property
    def data(self):
        pass

    @data.setter
    def data(self, value: dict = {}):
        self.__data = value

    @property
    def order_dict(self):
        pass

    @order_dict.setter
    def order_dict(self, value: dict = {}):
        assert isinstance(value, dict), "order_dict must be Dict"
        self.__order_dict = value

    def create_schema(
        self, status_message: StatusEnum = StatusEnum.SUCCESSES, data: dict = {}, **args
    ) -> HyperDataSchema:
        """
        创建一个 schema的实例

        :param `status_message`: 状态枚举类
        :param `data`: 数据
        :param `args`: 更多的棉花糖字段
        """
        # 做数据校验
        assert isinstance(status_message, Enum), "status_message must be StatusEnum"
        # assert isinstance(data, dict) , "order_dict must be Dict"
        assert isinstance(args, dict), "order_dict must be Dict"

        # 封装为字典类型
        dict_ = {
            "status": status_message.value[0],
            "message": status_message.value[1],
            "data": data,
        }
        dict_.update(args)

        schema = HyperDataSchema().load(dict_)
        return schema

    def check_flag(
        self,
        flag: int | bool,
        status_enum_error: StatusEnum = StatusEnum.ERROR,
        data: dict = {},
        order_dict: dict = {},
    ) -> HyperDataSchema:
        """
        根据标识去返回Hyper data 该类主要是减少 if 语句的编写

        :param `flag`: 唯一标识
        :param `status_enum_error`: 错提示误的enum类
        :param `data`: 响应的数据格式
        :param `order_dict`: 更多的棉花糖字段
        """
        if flag:
            return self.create_schema(
                status_message=StatusEnum.SUCCESSES, data=data, **order_dict
            )
        return self.create_schema(status_message=status_enum_error)

    