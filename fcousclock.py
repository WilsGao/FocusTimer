import time

def focus_timer(duration):
    print("專注時鐘開始！")
    while duration:
        mins, secs = divmod(duration, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print("剩餘時間:", timeformat, end='\r')
        time.sleep(1)
        duration -= 1
    print("\n專注時間結束！")

if __name__ == "__main__":
    focus_duration = int(input("請輸入專注時間（以秒為單位）: "))
    focus_timer(focus_duration)
