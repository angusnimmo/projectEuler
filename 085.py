import math

def rectangle_count(m, n):
    return (m*n*(n+1)*(m+1)) // 4

def main():
    rectangle_target = 2 * 10**6
    upperbound = int((4*rectangle_target)**0.25)
    best_mn = (0,0)
    best_diff = rectangle_target - rectangle_count(best_mn[0], best_mn[1])

    for m in range(1, upperbound+1):
        n = (4*rectangle_target/(m*(m+1)))**0.5
        n_floor = math.floor(n)
        n_ceil = math.ceil(n)
        floor_diff = abs(rectangle_target - rectangle_count(m, n_floor))
        ceil_diff = abs(rectangle_target - rectangle_count(m, n_ceil))
        
        if floor_diff < best_diff:
            best_mn = (m, n_floor)
            best_diff = floor_diff
        
        if ceil_diff < best_diff:
            best_mn = (m, n_ceil)
            best_diff = ceil_diff
            
    print(best_mn[0] * best_mn[1])
    
if __name__ == "__main__":
    main()
