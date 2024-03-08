def add_years_to_date(date, n_years):
    out = date.replace(year=date.year + n_years)
    return out
