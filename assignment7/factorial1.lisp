(defun factorial(n)
    "Returns the factorial of given number"
    (setq prod 1)
    (loop for i from 1 to n
        do(setq prod (* prod i))
    )
    (return-from factorial prod)
)


(princ "Enter the number: ")
(write (factorial (read)))