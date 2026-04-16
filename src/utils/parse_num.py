from text_to_num import text2num

def parse_num(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return text2num(str(value), "es")