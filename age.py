from datetime import datetime

# ইনপুট নেওয়া
birth_date = input(" (YYYY-MM-DD): ")
death_date = input(" (YYYY-MM-DD): ")

# তারিখ পার্স করা
birth = datetime.strptime(birth_date, "%Y-%m-%d")
death = datetime.strptime(death_date, "%Y-%m-%d")

# সময়ের পার্থক্য হিসাব করা
life_span = death - birth

# মোট সেকেন্ড
total_seconds = life_span.total_seconds()

# বছর, দিন, ঘণ্টা, মিনিট, সেকেন্ড বের করা
years = int(total_seconds // (365.25 * 24 * 3600))
remaining_secs = total_seconds % (365.25 * 24 * 3600)

days = int(remaining_secs // (24 * 3600))
remaining_secs %= (24 * 3600)

hours = int(remaining_secs // 3600)
remaining_secs %= 3600

minutes = int(remaining_secs // 60)
seconds = int(remaining_secs % 60)

# আউটপুট
print(f":")
print(f"{years} ")
print(f"{days} ")
print(f"{hours} ")
print(f"{minutes} ")
print(f"{seconds} ।")