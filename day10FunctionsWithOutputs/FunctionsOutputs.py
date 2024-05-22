# Functions with Outputs
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


def my_function():
    result = 3 * 2
    return result


print(format_name("jEAn", "louis"))
