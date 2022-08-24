def msg(status: str, code: int, message: str):
    return {
        'status': status,
        'code': code,
        'message': message,
    }


def rsp(success: bool, statusCode: int, messages: list, data: dict):
    return {
        'statusCode': statusCode,
        'success': success,
        'messages': messages,
        'data': data,
    }
