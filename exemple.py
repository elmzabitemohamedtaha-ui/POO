import datetime 
from datetime import date
now=date.today()

born = datetime.date(2008,3,20)
print(f"{now.year - born.year}ans.")

