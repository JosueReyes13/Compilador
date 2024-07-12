import AnalizadorLexico
import AnalizadorSintactico
import AnalizadorSemantico

texto_input = '''constante entero TAM=10;
entero i, j, k=10; vec[TAM]={12, -1, 0, 99, 18, 23, 55, 10, 25, 30};
palabra p="Hola";
logico band=falso;
constante decimal PI=3.141592;

nulo ordBurbuja(entero *arr, entero n) {
	entero i, j, tmp;
  desde i=0 hasta n-2 incr 1
     j=i+1;
     mientras que j<=n-1 {
        si arr[i] > arr[j] hacer {
           tmp = arr[i];
           arr[i] = arr[j];
			  arr[j] = tmp;
        }
        j = j + 1;
      }
}
nulo impVec(entero *arr, entero n) {
	entero i=0;
  imprime("vec=[");
  repite {
     imprime(arr[i], ", ");
     i =  i+ 1;
  } hasta que i == n;
  imprimenl(arr[n-1], "]");
}

entero facRec(entero num) {
   si num == 0 o num == 1 hacer regresa 1;
   sino regresa num * facRec(num-1);
}

logico compara(decimal a, decimal b) {
    regresa a > b;
}

decimal areaCir(decimal radio) {
    regresa PI*radio^2;
}

palabra concatena(palabra a, palabra b) {
    regresa a + " " + b;
}

nulo principal() {
   imprime("Dame numero: ");
   lee(i);
   imprimenl("Factorial(", i, ")=", facRec(i)); 
}'''

tokens = AnalizadorLexico.Lexer(texto_input)
tokens = tokens.lexer()
print('\n')
print('\n')
print(texto_input)
print('\n')
print('\n')
try:
   sintactico = AnalizadorSintactico.SyntacticAnalyzer(tokens)
   sintactico.programa()
except StopIteration:
   pass