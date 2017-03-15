# supermarket spider configuration file
# author Gal

from datetime import datetime
import pytz

time = datetime.now(tz=pytz.timezone('Asia/Jerusalem')).strftime("%Y%m%d")
home_dir = "/home/gal"
