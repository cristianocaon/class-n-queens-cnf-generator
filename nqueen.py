import sys


def main():
    """Generates the CNF file for the n-queens problem.
    """
    
    formula = []
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    
    # Row restriction
    for i in range(num):
        chosen = 1
        for _ in range(num):
            clause = []
            for k in range(1, num + 1):
                if k == chosen:
                    clause.append(k + i * num)
                else:
                    clause.append(-1* (k + i * num))
            chosen += 1
            clause.append(0)
            formula.append(clause)
        
    # Column restriction
    for i in range(1, num + 1):
        chosen = i
        for _ in range(num):
            clause = []
            for k in range(i, num * num + 1, num):
                if k == chosen:
                    clause.append(k)
                else:
                    clause.append(-1 * k)
            chosen += num
            clause.append(0)
            formula.append(clause)
        
    # Board generation for diagonal restriction
    board = []    
    for i in range(num):
        row = []
        for j in range(num):
            row.append((j + 1) + i * num)
        board.append(row)
            
    # Diagonal restriction 
    valid_y = range(num)
    for i in range(num):
        for j in range(num):
            diag1 = [board[k][k-i+j] for k in range(num) if k-i+j in valid_y]
            diag2 = [board[k][i+j-k] for k in range(num) if i+j-k in valid_y]
            if len(diag1) > 1:
                for index, number in enumerate(diag1):
                    if number != board[i][j]:
                        diag1[index] = number * -1
                diag1.append(0)
                formula.append(diag1)
            if len(diag2) > 1:
                for index, number in enumerate(diag2):
                    if number != board[i][j]:
                        diag2[index] = number * -1
                diag2.append(0)
                formula.append(diag2)

    # Save formula into CNF
    with open("nqueen.cnf", 'w') as file:
        file.write(f"c nqueen.cnf\nc\np cnf {num * num} {len(formula)}\n")
        for clause in formula:
            temp = " ".join(map(str, clause))
            file.write(f"{temp}\n")
        

if __name__ == '__main__':
    main()
    