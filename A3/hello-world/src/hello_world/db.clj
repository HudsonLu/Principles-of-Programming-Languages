(ns hello-world.db
  (:require [clojure.string :as str]))

(defn loadData [filename]
  (let [file-contents (slurp filename)
        lines (str/split-lines file-contents)]
    (map #(str/split % #"\|") lines)))

(defn getCourseById [course-id courseDB]
  (first (filter #(= (first %) course-id) courseDB)))

(defn replaceCourseIdWithCourseName [grade course]
  (assoc grade 1 (last course)))

(defn convertGradeToNumeric [grade]
  (case grade
    "A+" 4.3
    "A"  4.0
    "A-" 3.7
    "B+" 3.3
    "B"  3.0
    "B-" 2.7
    "C+" 2.3
    "C"  2.0
    "C-" 1.7
    "D"  1.0
    "F"  0.0
    ))
