def calculadora(operacao):
    def soma(a, b):
        return a+b
    
    def subtracao(a, b):
        return a - b
    
    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b 
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtracao
        case "*":
            return multiplicacao
        case "/":
            return divisao

soma = calculadora("+")
print(soma(10, 10))     # 20

sub = calculadora("-")
print(sub(20, 10))      # 10

mult = calculadora("*")
print(mult(5, 10))      # 50

div = calculadora("/")
print(div(100, 10))     # 10.0