(ns hello-world.menu
  (:require [clojure.string :as str])
  (:require [hello-world.db :as db]))

(defn displayCourses [courseDB]
  (println "Courses:")
  (doseq [course courseDB]
    (println course)))

(defn displayStudents [studDB]
  (println "Students:")
  (doseq [student studDB]
    (println student)))

(defn displayGrades [gradeDB]
  (println "Grades:")
  (doseq [grade gradeDB]
    (println grade)))

(defn displayStudentRecord [studDB courseDB gradeDB]
  (print "Enter student ID: ")
  (flush)
  (let [student-id (read-line)]
    (let [student (first (filter #(= student-id (nth % 0)) studDB))]
      (println (str "[" (nth student 0) " " (nth student 1) "]"))
      (doseq [grade (filter #(= student-id (nth % 0)) gradeDB)]
        (let [course-id (nth grade 1)
              course (db/getCourseById course-id courseDB)] ; Use db/getCourseById from hello-world.db namespace
          (println (str "[" (str/join " " (rest course)) " " (nth grade 2) " " (nth grade 3) "]")))))))

(defn calculateGPA [studDB courseDB gradeDB]
  (print "Enter student ID: ")
  (flush)
  (let [student-id (read-line)
        student-grades (filter #(= student-id (nth % 0)) gradeDB)]
    (let [numeric-grades (map #(db/convertGradeToNumeric (nth % 3)) student-grades)
          course-credits (map #(-> (db/getCourseById (nth % 1) courseDB)
                                   (nth 3)
                                   (Double/parseDouble)) student-grades)
          weighted-grades (map #(* %1 %2) numeric-grades course-credits)
          total-credits (apply + course-credits)]
      (if (empty? student-grades)
        (println "No grades found for the student.")
        (println (str "GPA: " (format "%.2f" (/ (apply + weighted-grades) (apply + course-credits)))))))))


(defn calculateCourseAverage [courseDB gradeDB]
  (print "Enter course ID: ")
  (flush)
  (let [course-id (read-line)
        course-grades (filter #(= course-id (nth % 1)) gradeDB)]
    (let [numeric-grades (map #(db/convertGradeToNumeric (nth % 3)) course-grades)]
      (if (empty? course-grades)
        (println "No grades found for the course.")
        (let [average (/ (apply + numeric-grades) (count numeric-grades))]
          (let [[_ prefix course-number _] (db/getCourseById course-id courseDB)]
            (let [semester (->> course-grades
                                (map #(nth % 2))
                                (distinct)
                                (first))]
              (println [(str prefix " " course-number) semester (format "%.2f" average)]))))))))

(defn displayMenu [studDB courseDB gradeDB]
  (loop []
    (println "*** SIS Menu ***")
    (println "------------------")
    (println "1. Display Courses")
    (println "2. Display Students")
    (println "3. Display Grades")
    (println "4. Display Student Record")
    (println "5. Calculate GPA")
    (println "6. Course Average")
    (println "7. Exit") 
    (println "Enter an option: ")

 (let [choice (read-line)]
    (cond
      (= choice "1") (do
                       (displayStudents studDB)
                       (recur))
      (= choice "2") (do
                       (displayCourses courseDB)
                       (recur))
      (= choice "3") (do
                       (displayGrades gradeDB)
                       (recur)) 
       (= choice "4") (do
                       (displayStudentRecord studDB courseDB gradeDB)
                       (recur))
      (= choice "5") (do
                       (calculateGPA studDB courseDB gradeDB)
                       (recur)) 
      (= choice "6") (do
                       (calculateCourseAverage courseDB gradeDB)
                       (recur))
      
      (= choice "7") (do
                       (println "Thank you for using this platform!")
                       (System/exit 0))
      :else (do
              (println "Invalid option. Please try again.")
              (recur))))))

 

  
