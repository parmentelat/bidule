# see below how to choose between these 2 forms in an entry point
# from bidule.machine import Machine
from .machine import Machine

def main():
    machine = Machine()
    print(machine)
    # an entry point is expected to return 0 when everything goes fine
    return 0

# this is a common pattern to run the main function
#
# if __name__ == '__main__':
#     main()
#
# however for gory reasons, if you want this to work,
# you cannot use the relative import above, instead you must do
#
# from bidule.machine import Machine
#
# so for this reason we comment this out
# the right way to run main() is to define a script in pyproject.toml
