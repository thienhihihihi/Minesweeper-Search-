import time
from input_data import test_cases
from collections import deque
import copy
import sys
def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols
def is_goal(player_board):
    
    # Kiểm tra nếu không còn ô nào có giá trị -2 trong player_board
    for row in player_board:
        if -2 in row:
            return False
    return True
 

def Checked(current_player,i,j):
    
    rows = len(current_player)
    cols = len(current_player[0])
    count_neg2=0
    count_neg1=0
    for row in range(i-1,i+2):
        for col in range(j-1,j+2):
            if (is_valid(row,col,rows,cols)):
                 if current_player[row][col] == -2:
                    count_neg2 += 1
                 elif current_player[row][col] == -1:
                    count_neg1 += 1
                
    
    
    
    if(current_player[i][j]==0):
        return True
    
    if (current_player[i][j] == count_neg2 and count_neg1==0 ):
        return True
    if (current_player[i][j]==count_neg1):
        return True
    if (current_player[i][j]>count_neg1):
        
        if(current_player[i][j]-count_neg1==count_neg2):
            return True
    return False
                
def is_number(value):
    return isinstance(value, (int, float))


def canAssign(current_player,row,col):
    
    rows = len(current_player)
    cols = len(current_player[0])
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            
            if i==row and j==col:
                
                continue
            
            if(is_valid(i,j,rows,cols) and (is_number(current_player[i][j])==True and current_player[i][j]>=0) ):
                
                check_valid=Checked(current_player,i,j)
                
                if (check_valid==1):                    
                    return 1
                
    
            
    
    
    return 0
    


 
def generateMatrix(current_player,hidden_board,rows,cols):
    ans=[]
    
    
    
    
    for i in range (rows):
        for j in range (cols):
            
            if (current_player[i][j]==-2 and canAssign(current_player,i,j) ):
                
                temp=copy.deepcopy(current_player)
                
                temp[i][j]=hidden_board[i][j]
                
                ans.append(temp)
    
    return ans
                 
 
 
 
 

import copy

def bfs(player_board, hidden_board, rows, cols):
    queue = []
    visited = set()
    parent = {}

    # Chuyển trạng thái ban đầu thành chuỗi
    initial_state_str = matrix_to_string(player_board)

    # 🟢 In ma trận ban đầu của người chơi
    print("Ma trận ban đầu của người chơi:")
    for row in player_board:
        print(row)
    print("\n=========================\n")

    # Thêm trạng thái ban đầu vào hàng đợi và đặt cha của nó là None
    queue.append(copy.deepcopy(player_board))
    parent[initial_state_str] = None

    while queue:    
        current_player = queue.pop(0)
        current_state_str = matrix_to_string(current_player)
        visited.add(current_state_str)

        # Kiểm tra nếu trạng thái hiện tại đạt goal
        if is_goal(current_player):
            print("Number of states: ", len(queue) + len(visited))
            print("Trạng thái cuối cùng:")
            for row in current_player:
                print(row)

            # 🔥 Tính toán dung lượng bộ nhớ đã sử dụng 🔥
            memory_usage = (
                sys.getsizeof(queue) + 
                sys.getsizeof(visited) + 
                sys.getsizeof(parent) + 
                sum(sys.getsizeof(state) for state in queue) +
                sum(sys.getsizeof(state) for state in visited) +
                sum(sys.getsizeof(state) for state in parent)
            )
            print(f"\nDung lượng bộ nhớ đã sử dụng: {memory_usage / 1024:.2f} KB\n")

            print("\nCác bước truy vết:")

            # Truy vết lại các bước từ trạng thái goal về trạng thái ban đầu
            path = []
            state_str = current_state_str
            while state_str is not None:
                path.append(string_to_matrix(state_str, rows, cols))
                state_str = parent[state_str]

            # In ra đường đi từ trạng thái ban đầu đến goal
            path.reverse()
            for idx in range(len(path) - 1):
                current_state = path[idx]
                next_state = path[idx + 1]

                # Xác định ô nào thay đổi
                for i in range(rows):
                    for j in range(cols):
                        if current_state[i][j] != next_state[i][j]:
                            old_value = current_state[i][j]
                            new_value = next_state[i][j]

                        # Nếu giá trị mới là -999, hiển thị 'O' thay vì -999
                            if new_value == -999:
                                new_value = 'E'

                            print(f"Bước {idx + 1}: Thay đổi ô ({i}, {j}) từ {old_value} thành {new_value}")
                            break

                # In trạng thái sau thay đổi
                print("Trạng thái sau thay đổi:")
                for row in next_state:
                    print([cell if cell != -999 else 'E' for cell in row])  # Thay -999 bằng 'O'
                print()

            return

        # Sinh các trạng thái tiếp theo từ trạng thái hiện tại
        generate = generateMatrix(current_player, hidden_board, rows, cols)
        for item in generate:
            item_str = matrix_to_string(item)
            if item_str not in parent:
                queue.append(item)
                parent[item_str] = current_state_str

    print("Không tìm thấy giải pháp!")


# Hàm chuyển ma trận thành chuỗi
def matrix_to_string(matrix):
    return ",".join(map(str, [cell for row in matrix for cell in row]))


# Hàm chuyển chuỗi thành ma trận
def string_to_matrix(string, rows, cols):
    elements = string.split(",")  # Chia chuỗi thành danh sách
    flat_list = [int(e) if e.lstrip('-').isdigit() else -999 for e in elements]  # Thay 'O' bằng -999
    matrix = [flat_list[i * cols:(i + 1) * cols] for i in range(rows)]  # Chuyển thành ma trận
    return matrix




def g(matrix):
    row = len(matrix)
    col = len(matrix[0])
    total_opened = 0  # Biến lưu tổng số ô đã mở

    for i in range(row):
        for j in range(col):
            if (matrix[i][j]=='O' or matrix[i][j]=='S' or matrix[i][j]==-999 or matrix[i][j] >= 0   ):  # Kiểm tra ô đã mở và có giá trị >= 0
                total_opened += 1    # Cộng dồn số ô đã mở

    return total_opened

def h(matrix,num_mines):
    row = len(matrix)
    col = len(matrix[0])
    total_flagged = 0  # Biến lưu tổng số ô được gắn cờ
    probability=0
    
    hide=0
    
    for i in range(row):
        for j in range(col):
            
            if matrix[i][j] == -1:  # Kiểm tra ô có giá trị -1 (ô đã được gắn cờ)
                total_flagged += 1  # Cộng dồn số ô được gắn cờ
            
    

                        

    return total_flagged
            
    
def Astart(matrix,num_mines):
    f=h(matrix,num_mines)+g(matrix)
    return f

import sys

def astart(player_board, hidden_board, rows, cols, num_mines):
    openlist = []
    closeList = []
    parent = {}

    # 🟢 In ma trận ban đầu trước khi bắt đầu thuật toán
    print("Ma trận ban đầu của người chơi:")
    for row in player_board:
        print(row)
    print("\n=========================\n")

    openlist.append([Astart(player_board, num_mines), player_board])
    
    

    while len(openlist):
        current_player = openlist.pop(0)
        closeList.append(current_player[1])
        
        # Kiểm tra nếu đã đạt mục tiêu
        if is_goal(current_player[1]):
            
            print("Number of state: ", len(openlist) + len(closeList))
            print("Trạng thái cuối cùng:")
            for row in current_player:
                print(row)
            # 🔥 Tính toán dung lượng bộ nhớ đã sử dụng 🔥
            memory_usage = (
                sys.getsizeof(openlist) +
                sys.getsizeof(closeList) +
                sys.getsizeof(parent) +
                sum(sys.getsizeof(state) for _, state in openlist) +
                sum(sys.getsizeof(state) for state in closeList) +
                sum(sys.getsizeof(state) for state in parent)
            )
            print(f"\nDung lượng bộ nhớ đã sử dụng: {memory_usage / 1024:.2f} KB\n")

            # Truy vết lại các bước từ goal về start
            path = []
            state_str = matrix_to_string(current_player[1])  
            while state_str is not None:
                path.append(string_to_matrix(state_str, rows, cols))  
                state_str = parent.get(state_str)  
                
            # Đảo ngược path để có đường đi từ start đến goal
            path.reverse()
            
            # In các bước trong quá trình truy vết
            for idx in range(len(path) - 1):
                current_state = path[idx]
                next_state = path[idx + 1]
                
                for i in range(rows):
                    for j in range(cols):
                        if current_state[i][j] != next_state[i][j]:
                            old_value = current_state[i][j]
                            new_value = next_state[i][j]

                        # Nếu giá trị mới là -999, hiển thị 'O' thay vì -999
                            if new_value == -999:
                                new_value = 'E'

                            print(f"Bước {idx + 1}: Thay đổi ô ({i}, {j}) từ {old_value} thành {new_value}")
                            break
                
                print("Trạng thái sau thay đổi:")
                for row in next_state:
                    print([cell if cell != -999 else 'E' for cell in row])
                print()
            
            return
        
        # Sinh các trạng thái tiếp theo từ trạng thái hiện tại
        generate = generateMatrix(current_player[1], hidden_board, rows, cols)
        
        for item in generate:
            item_str = matrix_to_string(item)
            if item_str not in closeList and item_str not in [subitem[1] for subitem in openlist]:
                openlist.append([Astart(item, num_mines), item])
                parent[item_str] = matrix_to_string(current_player[1])
                
        # Sắp xếp openlist theo giá trị f(n) từ nhỏ đến lớn
        openlist.sort(key=lambda x: int(x[0]), reverse=True)
    
    print("Không tìm thấy giải pháp!")

def print_test_cases():
    """In ra danh sách các test case và cho phép người dùng chọn."""
    print("Danh sách các test case:")
    for idx, test_case in enumerate(test_cases):
        print(f"Test case {idx + 1}: {test_case['rows']}x{test_case['cols']} board")
    print()






def select_algorithm():
    """In danh sách giải thuật và cho phép người dùng chọn."""
    print("Chọn giải thuật để thực hiện:")
    print("1. BFS")
    print("2. A*")
    print()
    while True:
        try:
            algo_choice = int(input("Nhập số (1 hoặc 2): "))
            if algo_choice in (1, 2):
                return algo_choice
            else:
                print("Vui lòng nhập số 1 hoặc 2.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")




if __name__ == "__main__":
    # Hiển thị danh sách các test case
    print_test_cases()

    # Yêu cầu người dùng chọn test case
    while True:
        try:
            test_case_idx = int(input("Chọn test case (nhập số thứ tự): ")) - 1
            if 0 <= test_case_idx < len(test_cases):
                break
            else:
                print("Vui lòng chọn một test case hợp lệ.")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

    # Lấy test case được chọn
    test_case = test_cases[test_case_idx]
    rows = test_case["rows"]
    cols = test_case["cols"]
    num_mines=test_case["num_mines"]
    hidden_board = test_case["hidden_board"]
    player_board = test_case["player_board"]

    # Hiển thị tùy chọn giải thuật
    algo_choice = select_algorithm()

    # Chạy thuật toán đã chọn
    start = time.time()
    if algo_choice == 1:
        print("\nĐang chạy giải thuật BFS...")
        bfs(player_board, hidden_board, rows, cols)
    elif algo_choice == 2:
        print("\nĐang chạy giải thuật A*...")
        astart(player_board, hidden_board, rows, cols,num_mines)
    end = time.time()

    print(f"\nExecution time: {end - start:.3f} seconds")
    