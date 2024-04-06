# Functions with variable-length arguments (*args)
# args is a tuple.



# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge=""

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word+" "

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)



# ----------------------------------------------------
# Functions with variable-length keyword arguments (**kwargs)
# kwargs is a dictionary.
# -------------------------------------------------------
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, values in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key+ ": " + values)

    print("\nEND REPORT")

# First call to report_status()
report_status(name="Misbah", department="CS", status="final year")

# Second call to report_status()
report_status(name="Maadeha", department="web developer", status="last year")