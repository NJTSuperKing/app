import datetime
import keyboard

def get_next_business_day():
    today = datetime.date.today()
    next_day = today
    while next_day.weekday() >= 5:  # 5 is Saturday and 6 is Sunday
        next_day += datetime.timedelta(days=1)
    return next_day

def format_date(date):
    return date.strftime("%B %d, %Y")

def replace_ddd():
    next_business_day = get_next_business_day()
    formatted_date = format_date(next_business_day)
    # Erase the last 4 characters (*ddd)
    for _ in range(4):
        keyboard.send("backspace")
    # Type the formatted date
    keyboard.write(formatted_date)

def main():
    # Hook the function to be called when '*ddd' is typed
    keyboard.add_word_listener('*ddd', lambda: replace_ddd(), triggers=['*ddd'], match_suffix=True)

    # Block the program and keep it running
    keyboard.wait()

if __name__ == "__main__":
    main()
