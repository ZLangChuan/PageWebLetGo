import ast
import json
import re


class NaningJsonUtil:
    """
    用于处理和JSON格式有关的工具类
    """

    @staticmethod
    def load_json_file(file_path) -> dict:
        """
        从文件中加载JSON数据
        :param file_path: 文件路径
        :return: JSON数据
        """
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)
            return json_data

    @staticmethod
    def replace_json_by_prompt(json_str: str | bytes, prompt: dict) -> str:
        """
        根据prompt替换json中的占位符

        :param json_str: JSON字符串
        :param prompt: 占位符和替换值的字典
        :return: 替换后的JSON字符串
        """
        if type(json_str) == bytes:
            json_str = json_str.decode("utf-8")
        json_str = json_str.replace("\n", "").replace("\r", "").replace(" ", "")

        pattern = r"\$\{([^}]+)\}"
        # 查找所有匹配项
        matches = re.findall(pattern, json_str)

        for matche in matches:
            placeholder, type_name = ast.literal_eval(matche)
            value = prompt.get(placeholder, "")
            if type_name == "str":
                if value is None:
                    value = ""
                json_str = json_str.replace(f"${{{matche}}}", f'"{value}"')
            elif type_name == "int":
                json_str = json_str.replace(f"${{{matche}}}", f"{value}")
        return json_str
