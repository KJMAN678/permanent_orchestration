import logging
import datetime
import time
from display_time import display_time # 追加した自作ライブラリ

def main(name: str) -> str:

    dtime = display_time.display_time_now()     # 追加
    now_time = dtime.time_now()
    logging.warning(f"Activity {now_time}")
    print("テスト中")
    time.sleep(5)
    # return f'Hello {name}!'
    return f'{name}!'