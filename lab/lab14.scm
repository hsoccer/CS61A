;; Scheme ;;
(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (begin
        (define (helper curr res)
          (if (> curr n)
            res
            (helper (+ curr 1) (combiner res (term curr)))
          )
        )
        (helper 1 start)
      )
  )
)

;;; Tests
(define (identity x) x)
(accumulate * 1 5 identity)
; expect 120

(define (square x) (* x x))
(accumulate + 0 5 square)
; expect 55

(define (how-many-dots s)
  (if (not (pair? s))
    0
    (+ (if (and (not (null? (cdr s))) (not (pair? (cdr s))))
          1
          0
       )
       (how-many-dots (cdr s))
       (how-many-dots (car s))
    )
  )
)

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7))))))))
; expect 0



(define (swap s)
  (cond
    ((null? s) nil)
    ((null? (cdr s)) (cons (car s) nil))
    (else (cons (car (cdr s)) (cons (car s) (swap (cdr (cdr s))))))
  )
)

;;; Tests

(swap (list 1 2 3 4))
; expect (2 1 4 3)
(swap (list 1 2 3 4 5))
; expect (2 1 4 3 5)
