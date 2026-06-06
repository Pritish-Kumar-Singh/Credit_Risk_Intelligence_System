import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

MYSQL_USER = "root"
MYSQL_PASSWORD = quote_plus("Pritish@123")
MYSQL_HOST = "localhost"
MYSQL_DATABASE = "credit_risk_db"

# Read correctly
df = pd.read_csv(
    "data/raw/default of credit card clients.csv",
    header=1
)

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
)

df.to_sql(
    "credit_risk_raw",
    con=engine,
    if_exists="replace",
    index=False
)

print(df.shape)
print(df.columns.tolist())