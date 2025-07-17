# Date Preprocessing
def convert_date(value):
    if isinstance(value, (int, float)):
        excel_epoch = datetime.datetime(1899, 12, 30)
        return excel_epoch + datetime.timedelta(days=value)
    else:
        try:
            return pd.to_datetime(value, dayfirst=True)
        except ValueError:
            return pd.to_datetime(value, format='%d-%m-%y %H:%M')
