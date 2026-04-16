import sqlite3
from typing import List, Tuple

def top_departments(db_path: str) -> List[Tuple[str, float]]:
    """Task 1: Top 3 departments by total salary expenditure"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = """
        SELECT 
            d.name AS dept_name,
            SUM(e.salary) AS total_salary
        FROM departments d
        JOIN employees e ON d.dept_id = e.dept_id
        GROUP BY d.dept_id, d.name
        ORDER BY total_salary DESC
        LIMIT 3;
    """
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    conn.close()
    return result


def employees_with_projects(db_path: str) -> List[Tuple[str, str]]:
    """Task 2: Employees with their project names"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = """
        SELECT 
            e.name AS employee_name,
            p.name AS project_name
        FROM employees e
        INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
        INNER JOIN projects p ON pa.project_id = p.project_id
        ORDER BY e.name, p.name;
    """
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    conn.close()
    return result


def salary_rank_by_department(db_path: str) -> List[Tuple[str, str, float, int]]:
    """Task 3: Salary rank within each department using RANK()"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = """
        SELECT 
            e.name AS employee_name,
            d.name AS dept_name,
            e.salary,
            RANK() OVER (PARTITION BY e.dept_id ORDER BY e.salary DESC) as rank
        FROM employees e
        JOIN departments d ON e.dept_id = d.dept_id
        ORDER BY d.name ASC, rank ASC;
    """
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    conn.close()
    return result
if __name__ == "__main__":
    db_path = "drill.db"
    print("Task 1:", top_departments(db_path))
    print("Task 2:", employees_with_projects(db_path))
    print("Task 3:", salary_rank_by_department(db_path))