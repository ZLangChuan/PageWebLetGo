from enum import Enum


class StatusEnum(Enum):
    """
    状态码枚举类
    """

    SUCCESSES = (200, "操作成功")
    ERROR = (500, "系统错误")
    FAIL = (400, "操作失败")

    USER_NO_EXIST = (10001, "用户不存在")
    USER_PASSWORD_ERROR = (10002, "用户名或密码错误")
    USER_ALREADY_EXIST = (1003, "用户已存在")  # 用户已经存在
    USER_LOGIN_ERROR = (1004, "用户登录失败")
    USER_PASSWORD_OR_EMAIL_ERROR = (1006, "邮箱或密码错误")
    USER_NOT_ID = (1005, "用户没有唯一的ID")
    USER_NOT_LOGIN = (1008, "用户未登录")

    TOKEN_ERROR = (1001, "token错误")
    TOKEN_EXPIRE = (1002, "当前令牌已经过期")
    TOKEN_NO_EXIST = (1003, "token不存在")


    REGIEST_TWO_PASSWORD_ERROR = (1007, "两次密码不一致")

    EMAIL_IS_USER = (1006, "邮箱已被注册")

    STORY_NO_EXIST = (20001, "故事不存在")
    STORY_DELETE_ERROR = (20002, "故事删除失败")
    STORY_ADD_ERROR = (20003, "故事添加失败")
    STORY_UPDATE_ERROR = (20004, "故事更新失败")

    SUBSCOPE_NO_EXIST = (30001, "该分镜不存在")
    SUBSCOPE_DELETE_ERROR = (30002, "分镜删除失败")
    SUBSCOPE_ADD_ERROR = (30003, "分镜添加失败")
    SUBSCOPE_UPDATE_ERROR = (30004, "分镜更新失败")
    SUBSCOPE_FIND_ERROR = (30005, "分镜查询失败")
    SUBSCOPE_NO_NUM = (30006, "分镜数量不足")
    SUBSCOPE_NO_ID = (30007, "分镜没有唯一的ID")

    PROMPT_NO_EXIST = (40001, "该提示词不存在")
    PROMPT_DELETE_ERROR = (40002, "提示词删除失败")
    PROMPT_ADD_ERROR = (40003, "提示词添加失败")
    PROMPT_UPDATE_ERROR = (40004, "提示词更新失败")
    PROMPT_FIND_ERROR = (40005, "提示词查询失败")
    PROMPT_NO_NUM = (40006, "提示词数量不足")
    PROMPT_NO_ID = (40007, "提示词没有唯一的ID")
    PROMPT_ID_NOT_MATCH = (40008, "提示词ID不匹配")

    COMFYUI_NO_CREATE_WORK = (50001, "无法想Comfy提交任务")
    COMFYUI_NO_EXIST_WORK = (50002, "ComfyUI任务不存在")
    COMFYUI_NOT_GET_KSAMPLER = (50003, "无法获取Comfyui的采样器信息")

    FILE_TYPE_ERROR = (60001, "文件类型错误")
    FILE_SIZE_ERROR = (60002, "文件大小错误")

    COMFYUI_URL_ADD_ERROR = (70001, "绘画服务器地址添加失败")
    COMFYUI_URL_DELETE_ERROR = (70002, "绘画服务器地址删除失败")
    COMFYUI_URL_FIND_ERROR = (70003, "绘画服务器地址查询失败")
    COMFYUI_URL_NO_EXIST = (70004, "绘画服务器地址不存在")
    COMFYUI_URL_UPDATE_ERROR = (70005, "绘画服务器地址更新失败")
    COMFYUI_URL_ID_ERROR = (70006, "绘画服务器地址ID错误")
    COMFYUI_URL_QUERY_ERROR = (70007, "绘画服务器地址查询失败")
    COMFYUI_NODE_NAME_ERROR = (70008, "绘画服务器节点名称错误")
    COMFYUI_URL_NOT_USE = (70009, "没有可用的绘画服务器地址")

    COMFYUI_CREATE_TASK_ERROR = (80001, "创建绘画任务失败")

    IMG_NOT_EXIST = (90001, "图片不存在")

    CATEGORIZE_ADD_ERROR = (100001, "分类添加失败")
    CATEGORIZE_DELETE_ERROR = (100002, "分类删除失败")
    CATEGORIZE_UPDATE_ERROR = (100003, "分类更新失败")
    CATEGORIZE_FIND_ERROR = (100004, "分类查询失败")


if __name__ == "__main__":
    a = StatusEnum.CATEGORIZE_ADD_ERROR
    print(type(a))
    print(isinstance(a, Enum))
    print(a.value)
    print(a.name)
    print(type(a))
