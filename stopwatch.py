from datetime import datetime

start = datetime.strptime("4:25:40", "%H:%M:%S")
end = datetime.strptime("11:40:10", "%H:%M:%S")

difference = end - start
print(difference)