
import json
import requests

import logging
import logging.handlers as handlers
import uvicorn

from datetime import datetime
# 해당 카프카 로그 파일 경로를 받아서 로거를 반환하는 함수
# handler 추가 필요


def get_logger(logfile_path: str) -> logging.Logger:
    # 로거 이름을 고유하게 설정 (여기서는 파일 경로를 사용하되, 고유성을 보장함)
    logger = logging.getLogger('log/' + logfile_path)

    if not logger.hasHandlers():  # 핸들러가 없을 때만 추가
        logFormatter = logging.Formatter('[%(asctime)s][%(levelname)s]-%(message)s')
        logHandler = handlers.TimedRotatingFileHandler(filename='log/'+logfile_path, when='midnight', interval=1, backupCount=14, encoding='utf8')
        logHandler.setFormatter(logFormatter)
        logger.setLevel(logging.INFO) # 로그 레벨 설정 : INFO 레벨 로그 출력 (디버그 출력 안됌)
        logger.addHandler(logHandler)

    return logger

# ...args : 가변, 여러개의 추가인자를 전달 console.log와 같은 형태


def access_log():
    ''' 엑세스 로그 포맷은 다음과 같이 지정'''
    logger = logging.getLogger('uvicorn_access')  # 로거 이름을 지정
    # logger = logging.getLogger(')

    if not logger.hasHandlers():  # 핸들러가 없을 때만 추가
        console_formatter = uvicorn.logging.ColourizedFormatter(
            "{asctime} - {message}",
            style="{", use_colors=True)
        handler = logging.handlers.TimedRotatingFileHandler('log/uvicorn_access', when='midnight', interval=1, backupCount=1)
        handler.setFormatter(console_formatter)
        logger.addHandler(handler)

    return logger


def condition_of_sent_to_notification(error_stack):
    # error가 100개가 쌓였거나 하루가 지나 면서 에러가 0개가 아닐때
    first_condition = ((len(error_stack) + 1) % 100 == 0 or datetime.now().hour == 0) and len(error_stack) > 0
    return first_condition


def sent_to_slack(url, message):

    payload = {
        'text': message
    }

    res = requests.post(
        url, 
        data=json.dumps(payload), 
        headers={'Content-Type': 'application/json'}
    )

    return res
