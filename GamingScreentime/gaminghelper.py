from datetime import datetime,date, timedelta
import csv

def logging():
    input("Start: ")
    start = datetime.now()
    input("End: ")
    end = datetime.now()
    difference = end - start
    print("Time started:",  start)
    print("Time ended:", end)
    print("Session length:", difference)
    with open("gamingdata.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["date","start_time","end_time","duration"])
        writer.writerow({"date": date.today(), "start_time": start, "end_time": end, "duration": difference.total_seconds()})

def calclog():
    today_duration = timedelta(minutes = 0)
    week_duration = timedelta(minutes=0)
    day_of_week = datetime.today().weekday() + 1
    start_of_week = date.today() - timedelta(days=date.today().weekday())
    end_of_week = date.today()  + timedelta(days=(6 - date.today().weekday()))
    with open("gamingdata.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if date.fromisoformat(row["date"]) == date.today():
                today_duration += timedelta(seconds=float(row["duration"]))
            if start_of_week <= date.fromisoformat(row["date"]) <= end_of_week:
                week_duration += timedelta(seconds=float(row["duration"]))
    weekly_average = week_duration / day_of_week
    print("Today so far:", today_duration)
    print("Daily average for this week so far:", weekly_average)
    print("This week total so far:", week_duration)    