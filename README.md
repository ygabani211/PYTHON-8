# 🔢 NumPy Array Analyzer

A beginner-friendly, menu-driven Python project built with **NumPy**. It
lets you create 1D, 2D, and 3D arrays, perform mathematical operations,
combine arrays, search and sort values, filter data, and calculate basic
statistics.

> **Project goal:** Practice Python functions, classes, loops,
> conditionals, exception handling, and NumPy array operations in one
> interactive project.

------------------------------------------------------------------------

## ✨ Features

### 1. Create a NumPy Array

Choose the array type you want to create:

-   **1D Array** --- enter a list of numbers.
-   **2D Array** --- enter the number of rows and columns, then provide
    the required elements.
-   **3D Array** --- enter the three dimensions, then provide the
    required elements.

### 2. Mathematical Operations

Enter a second array with the same shape as the original array and
choose:

-   Addition (`+`)
-   Subtraction (`-`)
-   Multiplication (`*`)
-   Division (`/`)

### 3. Combine or Split Arrays

-   **Combine:** Stack the original and second arrays vertically using
    `numpy.vstack()`.
-   **Split:** This option is currently under construction and needs
    axis/splitting logic.

### 4. Search, Sort, and Filter

-   **Search:** Find a value and display its matching index positions
    using `numpy.where()`.
-   **Sort:** Sort array values along the last axis using
    `numpy.sort()`.
-   **Filter:** Display values greater than a threshold.

### 5. Aggregates and Statistics

Calculate:

-   Sum --- `numpy.sum()`
-   Mean --- `numpy.mean()`
-   Median --- `numpy.median()`
-   Standard deviation --- `numpy.std()`
-   Variance --- `numpy.var()`

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   **Python 3** --- programming language
-   **NumPy** --- numerical computing and array operations

------------------------------------------------------------------------

## 📋 Requirements

-   Python 3 installed on your computer
-   NumPy library

------------------------------------------------------------------------

## 🚀 Installation and Setup

### Step 1: Get the project

Download or clone this repository:

``` bash
git clone https://github.com/your-username/your-repository-name.git
```

Or download the repository as a ZIP file and extract it.

### Step 2: Open the project folder

``` bash
cd your-repository-name
```

### Step 3: Install NumPy

``` bash
python -m pip install numpy
```

If your system uses `python3`, run:

``` bash
python3 -m pip install numpy
```

### Step 4: Run the program

Save the Python source code as `numpy_analyzer.py`, then run:

``` bash
python numpy_analyzer.py
```

If needed, use:

``` bash
python3 numpy_analyzer.py
```

------------------------------------------------------------------------

## 🧭 How to Use

When the program starts, it displays the main menu:

  -----------------------------------------------------------------------
  Menu option                         What it does
  ----------------------------------- -----------------------------------
  1\. Create a NumPy Array            Creates a 1D, 2D, or 3D array

  2\. Perform Mathematical Operations Performs arithmetic with a second
                                      same-shaped array

  3\. Combine or Split Arrays         Combines arrays vertically; split
                                      is not implemented yet

  4\. Search, Sort, or Filter Arrays  Searches for a value, sorts, or
                                      filters values

  5\. Compute Aggregates and          Calculates summary statistics
  Statistics                          

  6\. Exit                            Closes the program
  -----------------------------------------------------------------------

### Example: Create a 1D array

1.  Select **1 --- Create a NumPy Array**.
2.  Select **1 --- 1D Array**.
3.  Enter numbers separated by spaces, for example:

``` text
10 20 30 40 50
```

The program converts the input into a NumPy array.

### Example: Create a 2D array

Choose 2 rows and 3 columns, then enter 6 values:

``` text
1 2 3 4 5 6
```

The resulting array is:

``` text
[[1 2 3]
 [4 5 6]]
```

### Example: Find statistics

For the array `[10, 20, 30, 40, 50]`:

  Operation     Result
  ----------- --------
  Sum              150
  Mean              30
  Median            30

------------------------------------------------------------------------

## 📁 Suggested Project Structure

``` text
NumPy-Array-Analyzer/
│
├── numpy_analyzer.py
├── README.md
└── screenshots/
    └── add-your-screenshots-here
```

The `screenshots/` folder is optional. Add your own screenshots there if
you want to show the program's output on GitHub.

------------------------------------------------------------------------

## 🧠 Python and NumPy Concepts Practiced

-   Classes and objects
-   Constructor (`__init__`)
-   Instance methods and `self`
-   `if`, `elif`, and `else`
-   `while` loops
-   User input with `input()`
-   Exception handling with `try` and `except`
-   NumPy arrays and array shapes
-   Reshaping arrays with `reshape()`
-   Stacking arrays with `vstack()`
-   Searching with `where()`
-   Sorting with `sort()`
-   Filtering with Boolean indexing
-   Statistical functions

------------------------------------------------------------------------

## ⚠️ Notes and Current Limitations

-   Create the array before selecting options 2--5.
-   For 2D and 3D arrays, enter exactly the number of elements
    requested.
-   Mathematical operations require the second array to have the same
    shape as the original array.
-   The combine option uses vertical stacking, so the arrays must be
    compatible for `vstack()` (in particular, their column dimensions
    must match).
-   The split option currently displays an under-construction message;
    array splitting is not implemented yet.
-   Division by zero and invalid input should be handled carefully. The
    current program may need extra validation for these cases.

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Implement array splitting with `numpy.split()` or
    `numpy.array_split()`.
-   Add checks for division by zero.
-   Improve input validation and error messages.
-   Add options to save and load arrays.
-   Add more statistical operations and visualizations.
-   Create a graphical user interface.

------------------------------------------------------------------------

## 👨‍💻 Author

**Your Name**

If you found this project useful, consider giving the repository a ⭐ on
GitHub.

------------------------------------------------------------------------

## 📄 License

This project is available for learning and educational use. Add a
license file to the repository if you want to specify formal reuse and
distribution permissions.
