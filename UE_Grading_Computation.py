text = "Zenos | GRADING"
formatted_string = "%50s" % (text)
print ( formatted_string, "|")

def calculate_average_score(count):
    total = 0
    for n in range(1, count + 1):
        print(f"For Activity {n}:")
        score = input("Enter Score: ")
        try:
            score = int(score)
        except ValueError:
            reset()
        total_score = input("Enter Total Score: ")
        try:
            total_score = int(total_score)
        except ValueError:
            reset()
        convert = (score / total_score) * 50 + 50
        total += convert
    return total / count

def calculate_percentage_score(average):
    return average * 0.2

def calculate_quiz_average_score(quiz):
    total = 0
    for n in range(1, quiz + 1):
        print(f"For Quiz {n}:")
        score = input("Enter Score: ")
        try:
            score = int(score)
        except ValueError:
            reset()
        total_score = input("Enter Total Score: ")
        try:
            total_score = int(total_score)
        except ValueError:
            reset()
        convert = (score / total_score) * 50 + 50
        total += convert
    return total / quiz

def calculate_quiz_percentage_score(average):
    return average * 0.35

def calculate_midterm_exam_score(midterm_exam, total_exam_score):
    average = (midterm_exam / total_exam_score) * 50 + 50
    return average

def calculate_midterm_exam_percentage_score(average):
    return average * 0.4

def calculate_non_academic_score(non_acad, total_non_acad):
    average = (total_non_acad / non_acad) * 50 + 50
    return average

def calculate_non_academic_percentage_score(average):
    return average * 0.05

def calculate_grade(Final_Grade):
    if Final_Grade > 98:
        return "1.00"
    elif Final_Grade > 95:
        return "1.25"
    elif Final_Grade > 92:
        return "1.50"
    elif Final_Grade > 89:
        return "1.75"
    elif Final_Grade > 86:
        return "2.00"
    elif Final_Grade > 83:
        return "2.25"
    elif Final_Grade > 80:
        return "2.50"
    elif Final_Grade > 77:
        return "2.75"
    elif Final_Grade > 75:
        return "3.00"
    elif Final_Grade > 70:
        return "4.00"
    else:
        return "5.00"

def calculate_average(Prelim, Tentative_Mid):
    weighted_average = (1/3) * Prelim + (2/3) * Tentative_Mid
    return weighted_average

def grading():
    f = input("Enter Grading (Prelim, Midterm, Finals): ")
    if f == "Prelim":
        pre()
    elif f == "Midterm":
        main()
    elif f == "Finals":
        fi()
    else:
        print("Invalid")
        grading()
def reset():
    grading()

def continue_prelim():
    pre()

def continue_midterm():
    main()

def continue_final():
    fi()
    
def prelim_calculation():
    w =input ("Continue Grading Calculation(Y) or Reset(N)?")
    if w == "Y":
        continue_prelim()
    elif w == "N":
        reset()
    else:
        print ("Invalid!, Choose Again")
        prelim_calculation()

def midterm_calculation():
    w =    w =input ("Continue Grading Calculation(Y) or Reset(N)?")
    if w == "Y":
        continue_midterm()
    elif w == "N":
        reset()
    else:
        print ("Invalid!, Choose Again")
        midterm_calculation()

def final_calculation():
    w =input ("Continue Grading Calculation(Y) or Reset(N)?")
    if w == "Y":
        continue_prelim()
    elif w == "N":
        reset()
    else:
        print ("Invalid!, Choose Again")
        final_calculation()
        
def pre():
    d = input("Enter Subject (Computing, Art, Ethics, MMW, Programming): ")
    if d == "x":
        reset()
    if d == "Computing":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
            
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int (midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nPrelim Grade: ", Tentative_Mid)
        grade = calculate_grade(Tentative_Mid)
        print ("You Got:", grade)

        prelim_calculation()

    elif d == "Art":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
            
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int (midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nPrelim Grade: ", Tentative_Mid)
        grade = calculate_grade(Tentative_Mid)
        print ("You Got:", grade)

        prelim_calculation()

    elif d == "Ethics":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
            
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int (midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nPrelim Grade: ", Tentative_Mid)
        grade = calculate_grade(Tentative_Mid)
        print ("You Got:", grade)

        prelim_calculation()

    elif d == "MMW":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
            
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int (midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nPrelim Grade: ", Tentative_Mid)
        grade = calculate_grade(Tentative_Mid)
        print ("You Got:", grade)

        prelim_calculation()

    elif d == "Programming":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
            
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int (midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nPrelim Grade: ", Tentative_Mid)
        grade = calculate_grade(Tentative_Mid)
        print ("You Got:", grade)

        prelim_calculation()

    else:
        print("Choose Again!")
        pre()
    
def main():
    d = input("Enter Subject (Computing, Art, Ethics, MMW, Programming): ")
    if d == "Computing":
        count = input("\nEnter how many Activities: ")
        try:
            count= int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz= int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Midterm Grade: ", Tentative_Mid)

        Prelim = int(input("Enter Prelim Grade: "))
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        midterm_calculation()
        
    elif d == "Art":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Midterm Grade: ", Tentative_Mid)

        Prelim = input("Enter Prelim Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        midterm_calculation()
        
    elif d == "Ethics":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Midterm Grade: ", Tentative_Mid)

        Prelim = input("Enter Prelim Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        midterm_calculation()

        
    elif d == "MMW":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Midterm Grade: ", Tentative_Mid)

        Prelim = input("Enter Prelim Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        midterm_calculation()

    elif d =="Programming":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Midterm Grade: ", Tentative_Mid)

        Prelim = input("Enter Prelim Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        midterm_calculation()
        
    else:
        print("Invalid Subject")
        main()

def fi():
    d = input("Enter Subject (Computing, Art, Ethics, MMW, Programming): ")
    if d == "Computing":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Final Grade: ", Tentative_Mid)

        Prelim = input("Enter Midterm Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        final_calculation()

    elif d == "Art":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Final Grade: ", Tentative_Mid)

        Prelim = input("Enter Midterm Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        final_calculation()

    elif d == "Ethics":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Final Grade: ", Tentative_Mid)

        Prelim = input("Enter Midterm Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        final_calculation()
        
    elif d == "MMW":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Final Grade: ", Tentative_Mid)

        Prelim = input("Enter Midterm Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        final_calculation()

    elif d == "Programming":
        count = input("\nEnter how many Activities: ")
        try:
            count = int(count)
        except ValueError:
            reset()
        average = calculate_average_score(count)
        p1 = calculate_percentage_score(average)
        print("\nAverage score:", average)
        print("Percentage score:", p1)

        quiz = input("\nEnter how many Quizzes: ")
        try:
            quiz = int(quiz)
        except ValueError:
            reset()
        average1 = calculate_quiz_average_score(quiz)
        p2 = calculate_quiz_percentage_score(average1)
        print("\nAverage score:", average1)
        print("Percentage score:", p2)

        midterm_exam = input("\nEnter Exam Score: ")
        try:
            midterm_exam = int(midterm_exam)
        except ValueError:
            reset()
        total_exam_score = input("Enter Total Exam Score: ")
        try:
            total_exam_score = int(total_exam_score)
        except ValueError:
            reset()
        average4 = calculate_midterm_exam_score(midterm_exam, total_exam_score)
        p3 = calculate_midterm_exam_percentage_score(average4)
        print("\nAverage score:", average4)
        print("Percentage score:", p3)

        non_acad = input("\nEnter Non-Academic Score: ")
        try:
            non_acad = int(non_acad)
        except ValueError:
            reset()
        total_non_acad = input("Enter Total Non-Academic Score: ")
        try:
            total_non_acad = int(total_non_acad)
        except ValueError:
            reset()
        ave = calculate_non_academic_score(non_acad, total_non_acad)
        p4 = calculate_non_academic_percentage_score(ave)
        print("\nAverage score:", ave)
        print("Percentage score:", p4)

        Tentative_Mid = p1+p2+p3+p4
        print ("\nTentative Final Grade: ", Tentative_Mid)

        Prelim = input("Enter Midterm Grade: ")
        try:
            Prelim = int(Prelim)
        except ValueError:
            reset()
        Final_Grade = calculate_average (Prelim, Tentative_Mid)
        print("Final Grade: ", Final_Grade)
        grade = calculate_grade(Final_Grade)
        print("\n")
        print("You Got", grade)
        print("\n")
        final_calculation()

    else:
        print("Choose Again!")
        fi()
        
if __name__ == "__main__":
    grading()


