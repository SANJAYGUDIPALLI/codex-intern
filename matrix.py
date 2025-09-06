import numpy as np

def input_matrix(name="Matrix"):
    """Function to take matrix input from user."""
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter elements row-wise for {name}:")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:  # validation
            print(f"Please enter exactly {cols} elements.")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        elements.append(row)
    return np.array(elements)


def display_matrix(matrix, title="Result"):
    """Function to display matrix neatly."""
    print(f"\n{title}:")
    print(matrix)


def matrix_operations():
    while True:
        print("\n===== Matrix Operations Tool =====")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Transpose of a Matrix")
        print("5. Determinant of a Matrix")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A + B, "Addition Result")
            else:
                print("Error: Matrices must have the same dimensions for addition.")

        elif choice == "2":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                display_matrix(A - B, "Subtraction Result")
            else:
                print("Error: Matrices must have the same dimensions for subtraction.")

        elif choice == "3":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                display_matrix(np.matmul(A, B), "Multiplication Result")
            else:
                print("Error: Number of columns of Matrix A must equal rows of Matrix B.")

        elif choice == "4":
            A = input_matrix("Matrix")
            display_matrix(A.T, "Transpose")

        elif choice == "5":
            A = input_matrix("Matrix")
            if A.shape[0] == A.shape[1]:  # square matrix
                det = np.linalg.det(A)
                print(f"\nDeterminant of the matrix: {det:.2f}")
            else:
                print("Error: Determinant can only be calculated for square matrices.")

        elif choice == "6":
            print("Exiting Matrix Operations Tool. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    matrix_operations()
