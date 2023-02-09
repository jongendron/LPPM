import datetime
from os import SEEK_SET
from typing import TextIO

# NOTE: '.seek()'s offset parameter can only take values from .tell() command

def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    #invoice_parts = invoice_number.split("-")
    #return (int(invoice_parts[0]), int(invoice_parts[1])) # does the same
    year, number = invoice_number.split("-")
    return int(year), int(number)


def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.
    Only works when 'invoice_number' is value based on 'parse_invoice_number()'.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    year, number = parse_invoice_number(invoice_number) 
    current_year = get_year()

    # check if current year is greater than previous invoice
    if(current_year > year):
        number = 1
    else:
        number += 1
    
    new_invoice = f'{get_year():04d}-{number:04d}'
    #invoice = "{:04d}-{:04d}".format(get_year(), number)
    return new_invoice

def remove_blanks(infile: TextIO, ofile: TextIO) -> None:
    """Remove blank lines from the specified text file."""
    result = ""
    for line in infile:
        if not line.isspace():
            result += line
    # remove trailing '\n'
    #result = result.rstrip('\n')
    #infile.seek(0)  
    ofile.write(result)

def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_ptr: int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk. Only works if there
    are no blank lines at the end of the file.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_ptr: The position of the start of the last
    line in the file. This will be obtained by the previous
    call to 'record_invoice'.
    :return: The position of the start of the last line in the file.
        This can be used in subsequent calls to 'record_invoice'.
    """
    # Restore the file pointer to start (less efficient)
    #last_line_ptr = 0
    # Set file pointer to end (more efficient)
    #invoice_file.seek(last_line_ptr, 0) # same as below
    invoice_file.seek(last_line_ptr, SEEK_SET)

    last_row = ''
    for line in invoice_file:
        print('*', end='') # TODO: deleted after testing
        last_row = line
    if last_row:
    #if last_row != '' and last_row != '\t' and last_row != '\n':
        #invoice_number, _, _ = last_row.split('\t') # _ is unused argument from unpacking
        invoice_number = last_row.split('\t')[0]
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        # if file is empty, we'll start numbering at 1.
        year = get_year()
        new_invoice_number = f'{year:04d}-{1:04d}'

    # store file pointer
    last_line_ptr = invoice_file.tell()
    
    # write the new line
    print(f'{new_invoice_number}\t{company}\t{amount}', file=invoice_file)
    #print("\t".join((new_invoice_number, company, amount)))
    return last_line_ptr


data_file = 'invoices.csv' # original data file
output_file = 'invoices_nowhite.csv' # file to write to

# remove blanks and write to new file
# NOTE: you can only append to end of python
# file when r+ mode is activated, so we
# have to remove blank lines and
# save to new file
with open(data_file, 'r+') as invoices,\
    open(output_file, 'w') as output:
    remove_blanks(invoices, output)

# check your changes
with open(output_file, 'r+') as invoices:
    for line in invoices:
        print(f'line: {repr(line)}')

# write new invoice
#with open(data_file, 'r+') as invoices:
with open(output_file, 'r+') as invoices:
    last_line = record_invoice(invoices,\
        'ACME Roadrunner', 18.40)

    last_line = record_invoice(invoices,\
        'Squirel Storage', 350.18, last_line)
    

# Test code:
# current_year = get_year()
# test_data = [
#     ('2019-0005', (2019, 5), f'{current_year}-0001'),
#     (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
#     (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
#     (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
# ]

# for test_string, result, next_number in test_data:
#     parts = parse_invoice_number(test_string)
#     if parts == result:
#         print(f'{test_string} parsed successfully')
#     else:
#         print(f'{test_string} failed to parse. Expected {result} got {parts}')

#     new_number = next_invoice_number(test_string)
#     if next_number == new_number:
#         print(f'New number {new_number} generated correctly for {test_string}')
#     else:
#         print(f'New number {new_number} is not correct for {test_string}')

#     print('-' * 80)

