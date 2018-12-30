"""
Python closures takes in a variable in the outer scope and retains the binding to it.
todo : better documentation
"""


def sequence_generator(seed_num=1, num_of_terms=10):
    def sequence():
        """
        Note that seed_num and num_of_terms comes in from the Enclosing scope
        """
        print('-'*100)
        print(f"Building {num_of_terms} sequence for {seed_num}")
        for index in range(1, num_of_terms+1):
            print(seed_num*index)
        print('-'*100)

    return sequence


three_sequence = sequence_generator(3, 10)
three_sequence()


three_sequence = sequence_generator(5, 5)
three_sequence()

# magic property __closure__
print("__closure__ property is None for global functions : ", sequence_generator.__closure__)

print("__closure__ property shows closure variables : ", three_sequence.__closure__)
