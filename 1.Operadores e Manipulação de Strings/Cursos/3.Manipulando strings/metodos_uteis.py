# MAIUSCULA, MINUSCULA E TITULO
curso = "pYtHoN"

print(curso.upper())  # PYTHON
print(curso.lower())  # python
print(curso.title())  # Python

# REMOVER ESPAÇOS EM BRANCO
curso = "   Python "

print(curso.strip()) # "Python"
print(curso.lstrip()) # "Python "
print(curso.rstrip()) # "   Python"

# JUNÇÕES E CENTRALIZAÇÃO
curso = "Python"

print(curso.center(len(curso) + 4, '#'))  ##Python##
print(".".join(curso))  # P.y.t.h.o.n