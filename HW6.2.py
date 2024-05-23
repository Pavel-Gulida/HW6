
inputSeconds = int(input("Enter a seconds: "))

days = str(inputSeconds // 60 // 60 // 24)
hours = str(inputSeconds // 60 // 60 % 24).zfill(2)
minutes = str(inputSeconds // 60 % 60).zfill(2)
seconds = str(inputSeconds % 60).zfill(2)

print(f"{days} days, {hours}:{minutes}:{seconds}")

