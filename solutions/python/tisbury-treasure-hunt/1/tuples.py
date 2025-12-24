def get_coordinate(record):
    """
 
    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return record[1]
def convert_coordinate(coordinate):
    """
 
    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """
    return tuple(coordinate)
def compare_records(azara_record, rui_record):
    """
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """
    return tuple(azara_record[1]) == rui_record[1]
def create_record(azara_record, rui_record):
    """
 
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """
    return azara_record + rui_record if compare_records(azara_record, rui_record) else 'not a match'
def clean_up(combined_record_group):
    """
 
    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    combined_records = tuple(tuple([i[0]])+i[2:] for i in combined_record_group)
    report = "\n".join(str(record) for record in combined_records) + "\n"
    return report