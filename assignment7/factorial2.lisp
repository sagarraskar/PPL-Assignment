(defun factorial(n)
    "Returns the factorial of given number"
   
    (if (< n 0)
        (return-from factorial "Invalid Input")
    )

    (if (or (= 1 n) (= 0 n))
        (return-from factorial 1)
    )
    
    (return-from factorial (* n (factorial (- n 1))))
)

(princ "Enter the number: ")
(write (factorial (read)))