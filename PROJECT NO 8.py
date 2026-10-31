import numpy as np

class NumPyAnalyzer:
    def __init__(self):
        self.array = None

    def display_welcome(self):
        print("\nWelcome to the NumPy Analyzer!")
        print("==================================")

    def main_menu(self):
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        return input("Enter your choice: ")

    def check_array_exists(self):
        if self.array is None:
            print("No array found! Please create an array first.")
            return False
        return True
    
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                elements = input("Enter elements separated by space: ")
                self.array = np.array(list(map(int, elements.split())))
            elif choice == '2':
                rows = int(input("\nEnter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total_elements = rows * cols
                elements = input(f"Enter {total_elements} elements for the array separated by space: ")
                self.array = np.array(list(map(int, elements.split()))).reshape(rows, cols)
            elif choice == '3':
                x = int(input("\nEnter the dimension 1 (e.g., depth): "))
                y = int(input("Enter the dimension 2 (e.g., rows): "))
                z = int(input("Enter the dimension 3 (e.g., columns): "))
                total_elements = x * y * z
                elements = input(f"Enter {total_elements} elements for the array separated by space: ")
                self.array = np.array(list(map(int, elements.split()))).reshape(x, y, z)
            else:
                print("Invalid choice.")
                return

            print("\nArray created successfully:")
            print(self.array)
        except ValueError:
            print("Error: Please ensure you entered valid integers and the correct number of elements.")

    def math_operations(self):
        if not self.check_array_exists(): return
        
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice: ")

        try:
            total_elements = self.array.size
            elements = input(f"\nEnter the same-size array elements ({total_elements} elements separated by space): ")
            second_array = np.array(list(map(int, elements.split()))).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)
            print("\nSecond Array:")
            print(second_array)

            if choice == '1':
                result = self.array + second_array
                print("\nResult of Addition:")
            elif choice == '2':
                result = self.array - second_array
                print("\nResult of Subtraction:")
            elif choice == '3':
                result = self.array * second_array
                print("\nResult of Multiplication:")
            elif choice == '4':
                result = self.array / second_array
                print("\nResult of Division:")
            else:
                print("Invalid choice.")
                return
            
            print(result)
        except ValueError:
            print("Error: Array shapes do not match or invalid input.")

    def combine_split(self):
        if not self.check_array_exists(): return
        
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                total_elements = self.array.size
                elements = input(f"\nEnter the elements of another array to combine ({total_elements} elements separated by space): ")
                second_array = np.array(list(map(int, elements.split()))).reshape(self.array.shape)

                print("\nOriginal Array:")
                print(self.array)
                print("\nSecond Array:")
                print(second_array)

                combined = np.vstack((self.array, second_array))
                print("\nCombined Array (Vertical Stack):")
                print(combined)
            except ValueError:
                print("Error: Invalid input or shape mismatch.")
                
        elif choice == '2':
            print("Split feature is under construction or requires specific axis parameters.")

    def search_sort_filter(self):
        if not self.check_array_exists(): return
        
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = input("Enter your choice: ")

        if choice == '2':
            print("\nOriginal Array:")
            print(self.array)
            sorted_array = np.sort(self.array, axis=-1) 
            print("\nSorted Array:")
            print(sorted_array)
            print("(Sorting applied row-wise.)")
        elif choice == '1':
            val = int(input("Enter value to search: "))
            indices = np.where(self.array == val)
            if len(indices[0]) > 0:
                print(f"Value {val} found at indices: {indices}")
            else:
                print(f"Value {val} not found.")
        elif choice == '3':
            val = int(input("Enter threshold value (filter elements > value): "))
            print("\nFiltered Array:")
            print(self.array[self.array > val])

    def aggregates_statistics(self):
        if not self.check_array_exists(): return
        
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        choice = input("Enter your choice: ")

        print("\nOriginal Array:")
        print(self.array)

        if choice == '1':
            print(f"\nSum of Array: {np.sum(self.array)}")
        elif choice == '2':
            print(f"\nMean of Array: {np.mean(self.array)}")
        elif choice == '3':
            print(f"\nMedian of Array: {np.median(self.array)}")
        elif choice == '4':
            print(f"\nStandard Deviation of Array: {np.std(self.array):.4f}")
        elif choice == '5':
            print(f"\nVariance of Array: {np.var(self.array):.4f}")
        else:
            print("Invalid choice.")

    def run(self):
        self.display_welcome()
        while True:
            choice = self.main_menu()
            if choice == '1':
                self.create_array()
            elif choice == '2':
                self.math_operations()
            elif choice == '3':
                self.combine_split()
            elif choice == '4':
                self.search_sort_filter()
            elif choice == '5':
                self.aggregates_statistics()
            elif choice == '6':
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = NumPyAnalyzer()
    app.run()