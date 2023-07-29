class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return "\n".join(" ".join(str(val) for val in row) for row in self.data)

    def __eq__(self, other):
        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            return False
        return self.data == other.data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц должны быть одинаковыми для сложения.")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        
        return result

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Умножение поддерживается только с объектом Matrix.")
        
        if self.cols != other.rows:
            raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице.")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result



if __name__ == "__main__":
    
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]
    
    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    matrix3 = Matrix(3, 2)
    matrix3.data = [[2, 4], [6, 8], [10, 12]]

   
    print("Матрица 1:")
    print(matrix1)

    print("\nМатрица 2:")
    print(matrix2)

    print("\nМатрица 3:")
    print(matrix3)

    
    print("\nМатрица 1 равна Матрице 2?", matrix1 == matrix2)
    print("Матрица 1 равна Матрице 3?", matrix1 == matrix3)

   
    try:
        sum_matrix = matrix1 + matrix2
        print("\nСумма Матрицы 1 и Матрицы 2:")
        print(sum_matrix)
    except ValueError as e:
        print("\nОшибка при сложении матриц:", e)

 
    try:
        mul_matrix = matrix1 * matrix3
        print("\nУмножение Матрицы 1 на Матрицу 3:")
        print(mul_matrix)
    except ValueError as e:
        print("\nОшибка при умножении матриц:", e)
