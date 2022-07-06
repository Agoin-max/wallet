import sys
import time


class TimerContextManager(object):
    """
    用上下文管理器计时,可对代码片段计时,检测执行效率
    """

    def __init__(self):
        self.line = sys._getframe().f_back.f_lineno
        self.file_name = sys._getframe(1).f_code.co_filename  # 哪个文件调了用此方法

    def __enter__(self):
        self.start_at = int(time.time() * 1000)  # 毫秒级

    def __exit__(self, exc_type, exc_val, exc_tb):
        spend_time = int(time.time() * 1000) - self.start_at
        print(f"对下面代码片段：{self.file_name}: {self.line}, 执行耗时： {spend_time} 毫秒")
