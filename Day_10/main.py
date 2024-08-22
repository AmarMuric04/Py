# def my_function():
#     result = 3 * 2
#     return result


# print(my_function())


def format_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()


formated_name = format_name("amar", "muric")

# print(formated_name)


def format_name(first_name, last_name):
    """Return a formatted first and last name."""
    if first_name == "" or last_name == "":
        return "Fill out the inputs next time..."
    return first_name.title() + " " + last_name.title()


print(
    format_name(input("What's your first name?: "), input("What's your last name?: "))
)
