import sys


def get_row_clauses(num):
    """Gets row clauses for N-Queens SAT problem formula.

    :param int num: board dimension.
    :return list: formula with row clauses.
    """
    formula = []
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
            
    return formula


def get_column_clauses(num):
    """Gets column clauses for N-Queens SAT problem formula.

    :param int num: board dimension.
    :return list: formula with column clauses.
    """
    formula = []
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
            
    return formula


def generate_board(num):
    """Generates N-Queens board.

    :param int num: board dimension.
    :return list: N-Queens board
    """
    board = []    
    for i in range(num):
        row = []
        for j in range(num):
            row.append((j + 1) + i * num)
        board.append(row)
        
    return board

def get_diagonal_clauses(num, board):
    """Gets diagonal clauses for N-Queens SAT problem formula.

    :param int num: board dimension.
    :param list board: N-Queens board.
    :return list: formula with diagonal clauses.
    """
    formula = []
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
                
    return formula


def write_cnf_formula(formula, file, num):
    """Writes N-Queens formula clauses to CNF file.

    :param list formula: formula with N-Queens clauses.
    :param str file: filename to be written.
    :param int num: board dimension.
    """
    with open(file, 'w') as f:
        f.write(f"c {file}\nc\np cnf {num * num} {len(formula)}\n")
        for clause in formula:
            temp = " ".join(map(str, clause))
            f.write(f"{temp}\n")

def main():
    """Generates the CNF file for the N-Queens SAT problem.
    """
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    
    row_formula = get_row_clauses(num)
    column_formula = get_column_clauses(num)
    board = generate_board(num)
    diagonal_formula = get_diagonal_clauses(num, board)

    formula = [*row_formula, *column_formula, *diagonal_formula]
    
    write_cnf_formula(formula, "nqueen.cnf", num)
        

if __name__ == '__main__':
    main()
    