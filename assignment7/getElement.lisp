(defun getElement (n list)
  "Return the nth element of the list"
  (car (nthcdr n list))
)

(write-line "Enter the list with parenthesis: ")
(setq l (read))

(write-line "Enter the position: ")
(setq n (read))

(write-line "The element is: ")
(write (getElement n l))
