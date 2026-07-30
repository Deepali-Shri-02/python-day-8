def get_student_details():
    """Prompts the user to enter the student's name and marks for 5 subjects."""
    name = input("Enter student name: ")
    marks = []
    
    print("Enter marks for 5 subjects (out of 100 each):")
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"  Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("  Invalid input! Marks must be between 0 and 100.")
            except ValueError:
                print("  Invalid input! Please enter a numerical value.")
                
    return name, marks

def calculate_results(marks):
    """Calculates the total marks and overall percentage assuming 100 marks per subject."""
    total = sum(marks)
    percentage = (total / 500) * 100
    return total, percentage

def determine_grade(percentage):
    """Assigns a letter grade from A to F based on the percentage scored."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'F'

def display_report(name, marks, total, percentage, grade):
    """Prints a clean, formatted report card for the student."""
    print("\n" + "="*40)
    print(f"{"STUDENT REPORT CARD":^40}")
    print("="*40)
    print(f"Student Name : {name}")
    print("-"*40)
    
    # Display subject-wise breakdown
    for idx, mark in enumerate(marks, start=1):
        print(f"Subject {idx}    : {mark:.2f} / 100")
        
    print("-"*40)
    print(f"Total Marks  : {total:.2f} / 500")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Final Grade  : {grade}")
    print("="*40)

def main():
    """Main execution function to run the grade calculator system."""
    # 1. Collect inputs
    name, marks = get_student_details()
    
    # 2. Process data
    total, percentage = calculate_results(marks)
    grade = determine_grade(percentage)
    
    # 3. Output complete result
    display_report(name, marks, total, percentage, grade)

# Run the program
if __name__ == "__main__":
    main()
