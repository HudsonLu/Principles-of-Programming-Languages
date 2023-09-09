; Hudson Xingcheng Lu 
; 40254326 Assignment3

;Please look into HowtoRunMyCode.txt

(ns hello-world.core
  (:gen-class)
  (:require [hello-world.db :as db])
  (:require [hello-world.menu]))

(def studDB (db/loadData "studs.txt"))
(def courseDB (db/loadData "courses.txt"))
(def gradeDB (db/loadData "grades.txt"))

(hello-world.menu/displayMenu studDB courseDB gradeDB)
