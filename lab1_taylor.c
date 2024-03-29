
#include <stdio.h>
#include <stdlib.h>

double fatorial(int termos) 
{
   double aux;
   aux = termos;
   while(termos > 1)
   {
      aux = aux * (termos - 1);
      termos--;
   }

   return (aux);
}

double potencia(double base, int expoente) 
{
   double resultado;
   int i;

   resultado = 1;
   if(expoente == 0) return 1;
   for(i = 0;i < expoente; i++) resultado = resultado * base;
   return (resultado);
}


double serie_seno(double x, int termos)
{
   int i;
   double resultado;
   resultado = 0;

   for(i = 0; i < termos;i++)
   {
      resultado += potencia(-1, i) * potencia(x, 2*i + 1) / fatorial(2*i + 1);
   }

   return (resultado);
}

double seno(double x)
{
   int termos = 100;
   return serie_seno(x, termos);
}


void verificaPositivo(double seno){
    if(seno>=0){
        digitalWrite(5, HIGH);}
    else{
        digitalWrite(5,LOW);}
}


void setup() {
  // put your setup code here, to run once:

}

void main() {
  float contagem = 0;
  float limite = 6.28;
  float pontos = 1000.00;
  double resultadoSeno;
  
  while(contagem<=limite)
  {
    resultadoSeno = seno(contagem);
    verificaPositivo(resultadoSeno)
    contagem = contagem + (limite/pontos) ;           
  }

}
