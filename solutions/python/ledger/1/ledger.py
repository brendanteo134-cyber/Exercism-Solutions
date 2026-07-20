import datetime
class LedgerEntry(object):
    def __init__(self, date, description, change):
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change
    def __eq__(self, other):
        return (self.date == other.date
                or self.change == other.change
                or self.description == other.description)
    def __lt__(self, other):
        return (self.date < other.date
                or self.change < other.change
                or self.description < other.description)
create_entry = LedgerEntry
def format_entries(currency, locale, entries):
    return "\n".join(format_iter(currency, locale, entries))
def format_iter(currency, locale, entries):
    header = {
        "en_US": "Date|Description|Change",
        "nl_NL": "Datum|Omschrijving|Verandering"
    }[locale].split("|")
    yield TableFormat().header(*header)
    for entry in sorted(entries):
        date = DateFormatter().format(entry.date, locale)
        change = CurrencyFormatter().format(entry.change / 100.0, currency, locale)
        yield TableFormat().row(date, entry.description, change)
def wrap(field, width):
    return f"{field[:width-3]}..." if len(field) > width else field
class TableFormat:
    def header(self, date, desc, change):
        return f"{wrap(date, 10):<10} | {wrap(desc, 25):<25} | {wrap(change, 13):<13}"
    def row(self, date, desc, change):
        return f"{wrap(date, 10):<10} | {wrap(desc, 25):<25} | {wrap(change, 13):>13}"
class CurrencyFormatter:
    def format(self, value, currency, locale):
        symbol = {"USD": "$", "EUR": "€"}[currency]
        return getattr(self, f"_polish_{locale[:2]}")(f"{value:,.2f}", symbol)
    def _polish_en(self, text, symbol):
        if text.startswith("-"):
            return f"({symbol}{text[1:]})"
        return f" {symbol}{text} "
    def _polish_nl(self, text, symbol):
        swap_symbols = dict(zip(",.", ".,"))
        text = "".join(swap_symbols.get(s, s) for s in text)
        return f"{symbol} {text} "
class DateFormatter:
    def format(self, date, locale):
        snowflake_formats = { "en_US": "%m/%d/%Y" }
        sane_person_format = "%d-%m-%Y"
        return date.strftime(snowflake_formats.get(locale, sane_person_format))