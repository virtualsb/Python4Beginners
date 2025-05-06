hour = int(input("Enter start hour (0-23): "))
minute = int(input("Enter start minute (0-59): "))
duration = int(input("Enter event duration in minutes: "))

total_minutes = hour * 60 + minute + duration

end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(f"The event will end at {end_hour:02d}:{end_minute:02d}")