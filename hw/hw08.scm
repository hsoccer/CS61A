; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    (else 1)
  )
)

(define (ordered? s)
  (if (null? (cdr s))
    true
    (if (<= (car s) (car (cdr s)))
      (ordered? (cdr s))
      false
    )
  )
)

(define (nodots s)
  (cond
    ((not (pair? s))
      (cons s nil)
    )
    ((null? (cdr s))
      s
    )
    ((not (pair? (cdr s)))
      (if (pair? (car s))
        (cons (nodots (car s)) (nodots (cdr s)))
        (cons (car s) (nodots (cdr s)))
      )
    )
    (else
    (if (pair? (car s))
      (cons (nodots (car s)) (nodots (cdr s)))
      (cons (car s) (nodots (cdr s)))
    )
    )
  )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond
      ((empty? s)
        false
      )
      ((= (car s) v)
        true
      )
      (else
        (contains? (cdr s) v)
      )
    )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond
      ((empty? s)
        (list v)
      )
      ((= (car s) v)
        s
      )
      ((< v (car s))
        (cons v s)
      )
      (else
        (cons (car s) (add (cdr s) v))
      )
    )
)

(define (intersect s t)
    (cond
      ((or (empty? s) (empty? t))
        nil
      )
      ((= (car s) (car t))
        (cons (car s) (intersect (cdr s) (cdr t)))
      )
      ((< (car s) (car t))
        (intersect (cdr s) t)
      )
      (else
        (intersect s (cdr t))
      )
    )
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond
      ((empty? s)
        t
      )
      ((empty? t)
        s
      )
      ((= (car s) (car t))
        (cons (car s) (union (cdr s) (cdr t)))
      )
      ((< (car s) (car t))
        (cons (car s) (union (cdr s) t))
      )
      (else
        (cons (car t) (union s (cdr t)))
      )
    )
)

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
  (define (helper base power total)
    (if (= power 0)
      total
      (helper base (- power 1) (* total base))
    )
  )
  (helper b n 1)
)

(define (filter pred lst)
  (define (helper condition l result)
    (cond
      ((null? l)
        result
      )
      ((condition (car l))
        (helper condition (cdr l) (append result (list (car l))))
      )
      (else
        (helper condition (cdr l) result)
      )
    )
  )
(helper pred lst '())
)
