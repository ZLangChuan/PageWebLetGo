from datetime import datetime, timedelta, timezone


class NaningDatetimeUtil:

    @staticmethod
    def get_now_time(
        tz=None, need_format: bool = False, format="%Y-%m-%d %H:%M:%S"
    ) -> str:
        """
        获取当前时间

        :prama format: 时间格式
            %Y: 年
            %m: 月
            %d: 日
            %H: 时
            %M: 分
            %S: 秒
        """
        if need_format:
            return datetime.now(tz=tz).strftime(format)
        else:
            return datetime.now(tz=tz)

    @staticmethod
    def get_now_time_milliseconds() -> int:
        """
        获取当前时间戳
        """
        return

    @staticmethod
    def get_last_time_seconds() -> int:
        """
        获取上个月的 1日时间戳
        """
        # 获取当前日期
        now_data = datetime.now()

        # 获取当前年份和月份
        now_year = now_data.year
        now_month = now_data.month
        # 如果当前月份为1月，则年份减1，月份为12月
        if now_month == 1:
            now_year -= 1
            now_month = 12
        else:
            now_month -= 1
        # 获取上个月的1日时间戳
        return int(datetime(now_year, now_month, 1, 0, 0, 0, 0).timestamp())


if __name__ == "__main__":
    print(NaningDatetimeUtil.get_now_time(need_format=True))
    print(NaningDatetimeUtil.get_last_time_seconds())
