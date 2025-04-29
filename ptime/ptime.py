from datetime import datetime

# 示例字符串
date_str = "2023-10-05 14:30:00"

# 解析为 datetime 对象
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime object:", date_obj)

# 格式化为指定格式的字符串
date_str = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted string:", date_str)

# 获取当前时间戳（第一种方式）
date_obj = datetime.now()
converted_timestamp = date_obj.timestamp()
print("Timestamp from datetime:", converted_timestamp)

# 时间戳转为 datetime 对象
date_obj = datetime.fromtimestamp(converted_timestamp)
print("Datetime object from timestamp:", date_obj)

# 格式化为指定格式的字符串
date_str = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted string:", date_str)



import time

# 获取当前时间戳(第一种方式)
timestamp = time.time()
print("Current timestamp:", timestamp)

# 格式化为指定格式的字符串
date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print("Formatted string:", date_str)
