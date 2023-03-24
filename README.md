# Lab 01 - Avaliações de Dispositvos Embarcados

## Objetivo

Avaliar o desempenho e analisar a arquitetura de diversos dispositvos embarcados.

## Procedimentos

### 1. Série de Taylor 

Utilizando a linguagem C foi implementado a função seno com base na série de Taylor. Considerado até o décimo termo da série. A a senoide com 1000 pontos de 0 a 2*pi. 

Série elaborada: 

![image](https://user-images.githubusercontent.com/50549048/227561873-a1d41c0e-212a-4cba-8043-efdf35cebf5b.png)

Código em C:

```C
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

```

## 2. Avaliação do ATmega2560 (Arduino)

### Dispositivo

O ATmega2560 é um microcontrolador baseado em arquitetura RISC desenvolvido pela empresa Microchip Technology e amplamente utilizado na plataforma Arduino.

Processador: O ATmega2560 possui uma arquitetura RISC de 8 bits com palavra de 16 bits. Ele é baseado no conjunto de instruções AVR e possui um conjunto de 135 instruções. O clock máximo é de 16 MHz, o que resulta em uma taxa de 16 MIPS (milhões de instruções por segundo).

Memórias: O ATmega2560 possui 256 KB de memória flash para armazenamento de programas, 8 KB de memória SRAM para armazenamento de dados, e 4 KB de memória EEPROM para armazenamento não-volátil de dados. Além disso, ele possui uma memória de inicialização de 1 KB usada para armazenar o bootloader. A tecnologia de memória utilizada é a NOR flash.

Lista de periféricos: O ATmega2560 possui uma ampla variedade de periféricos integrados, incluindo 4 UARTs, 6 timers de 16 bits, 1 timer de 8 bits, 16 canais ADC de 10 bits, 2 interfaces SPI, 1 interface I2C, 1 interface USB, 1 interface Ethernet, 1 interface CAN, entre outros.

Potência consumida: A potência consumida pelo ATmega2560 varia de acordo com a frequência do clock e o tipo de operação realizada. Em standby, ele consome cerca de 100 μA a 200 μA, dependendo da tensão de alimentação. Em operação máxima, ele pode consumir até 30 mA em 5V.

Custo unitário: O custo unitário do ATmega2560 varia de acordo com o fornecedor e a quantidade de unidades compradas. Em média, o preço unitário fica em torno de US$ 8 a US$ 10 para compras de 100 unidades.

### Resultados

A série de Taylor foi aplicada ao arduino, conforme implementação em C, e então o dispostivo foi conectado a um osciloscópio. Conforme captura abaixo, foram obtidas uma frequência de 347.22mHz

![image](https://user-images.githubusercontent.com/50549048/227561513-74df5c03-a15b-44c5-9a5c-51a671e08ed8.png)

### Avaliação do ESP32

### Dispositivo

O ESP32 (WROOM-32) é um microcontrolador baseado em arquitetura RISC desenvolvido pela empresa Espressif Systems e amplamente utilizado em projetos de IoT.

Processador: O ESP32 possui uma arquitetura RISC de 32 bits com palavra de 32 bits. Ele é baseado no conjunto de instruções Xtensa LX6 da empresa Tensilica e possui dois núcleos. O clock máximo é de 240 MHz, o que resulta em uma taxa de 600 MIPS (milhões de instruções por segundo).

Memórias: O ESP32 possui 4 MB de memória flash para armazenamento de programas e dados, 520 KB de memória SRAM para armazenamento de dados, e 8 KB de memória RTC para armazenamento de dados em tempo real. Além disso, ele possui uma memória de inicialização de 448 KB usada para armazenar o bootloader. A tecnologia de memória utilizada é a NOR flash.

Lista de periféricos: O ESP32 possui uma ampla variedade de periféricos integrados, incluindo Wi-Fi 802.11 b/g/n, Bluetooth 4.2 BR/EDR e BLE, 18 canais ADC de 12 bits, 2 DACs de 8 bits, 2 interfaces SPI, 2 interfaces I2C, 3 UARTs, 2 interfaces I2S, 16 PWMs, entre outros.

Potência consumida: A potência consumida pelo ESP32 varia de acordo com a frequência do clock e o tipo de operação realizada. Em standby, ele consome cerca de 5 μA em modo sleep profundo e 20 μA em modo sleep leve. Em operação máxima, ele pode consumir até 260 mA em 3.3V.

Custo unitário: O custo unitário do ESP32 varia de acordo com o fornecedor e a quantidade de unidades compradas. Em média, o preço unitário fica em torno de US$ 3 a US$ 4 para compras de 100 unidades.

### Resultados 

A série de Taylor foi aplicada ao ESP32, conforme implementação em C, e então o dispostivo foi conectado a um osciloscópio. Conforme captura abaixo, foram obtidas uma frequência de 7.251Hz

![image](https://user-images.githubusercontent.com/50549048/227568108-a13c2782-99b0-433f-b849-01fe5d6e55f1.png)

### Avaliação do STM32F4

### Dispositivo

O STM32F4 é um microcontrolador baseado na arquitetura ARM Cortex-M4, desenvolvido pela empresa STMicroelectronics.

Processador: O STM32F4 possui um processador baseado na arquitetura ARM Cortex-M4, que é uma arquitetura RISC de 32 bits com palavra de 32 bits. Ele possui um único núcleo, com clock máximo de 168 MHz, o que resulta em uma taxa de 210 MIPS (milhões de instruções por segundo).

Memórias: O STM32F4 possui 1 MB de memória flash para armazenamento de programas e dados, 192 KB de memória SRAM para armazenamento de dados, e 4 KB de memória EEPROM para armazenamento não-volátil de dados. Além disso, ele possui uma memória de inicialização de 256 bytes usada para armazenar o bootloader. A tecnologia de memória utilizada é a NOR flash.

Lista de periféricos: O STM32F4 possui uma ampla variedade de periféricos integrados, incluindo 3 ADCs de 12 bits, 2 DACs de 12 bits, 2 interfaces USB, 4 interfaces USART, 4 interfaces SPI, 3 interfaces I2C, 15 timers, entre outros.

Potência consumida: A potência consumida pelo STM32F4 varia de acordo com a frequência do clock e o tipo de operação realizada. Em standby, ele consome cerca de 20 μA a 50 μA, dependendo da tensão de alimentação. Em operação máxima, ele pode consumir até 125 mA em 3.3V.

Custo unitário: O custo unitário do STM32F4 varia de acordo com o fornecedor e a quantidade de unidades compradas. Em média, o preço unitário fica em torno de US$ 5 a US$ 7 para compras de 100 unidades.

### Resultado 

A série de Taylor foi aplicada ao STM32F4, conforme implementação em C, e então o dispostivo foi conectado a um osciloscópio. Conforme captura abaixo, foram obtidas uma frequência de 60.621mHz

![image](https://user-images.githubusercontent.com/50549048/227570013-941569e5-528c-4b0b-bd2b-b2067e8eb19b.png)

## Comparação entre os resultados.

O dispositivo que obteve o melhor desempenho em relação ao tempo de execução do algoritmo foi o ESP-32, que teve um tempo de execução de 7.251Hz. Isso significa que ele conseguiu executar o algoritmo mais rapidamente em comparação aos outros dois dispositivos.

A diferença de desempenho pode ser explicada por uma série de fatores, como a arquitetura do processador, a quantidade e velocidade das memórias cache e RAM, a frequência de clock do processador, a presença de instruções SIMD (Single Instruction Multiple Data), a qualidade do compilador utilizado para gerar o código executável, a eficiência do sistema operacional em gerenciar os recursos do dispositivo, entre outros.

No caso específico desses dispositivos, a diferença de desempenho pode estar relacionada à arquitetura do processador, que é bastante diferente entre eles. O primeiro dispositivo utiliza um processador baseado na arquitetura AVR, que é bastante simples e não possui recursos avançados de otimização de desempenho. O terceiro dispositivo, por sua vez, utiliza um processador baseado na arquitetura ARM Cortex-M3, que é mais avançada que a AVR, mas ainda assim é menos poderosa do que a arquitetura Cortex-M4 utilizada pelo segundo dispositivo.

O código utilza recursividade e loops que podem ter sido interpretados diferentemente por cada dispositivo.

Além disso, a diferença de desempenho também pode estar relacionada à quantidade e velocidade das memórias cache e RAM utilizadas em cada dispositivo, bem como à frequência de clock do processador. Dispositivos com mais cache e RAM, bem como processadores com frequências de clock mais elevadas, tendem a ter melhor desempenho em tarefas que exigem alto processamento.

```
| Dispositivo  | Núcleos | Clock     | Memórias                 | Resultado |
|--------------|---------|-----------|--------------------------|-----------|
| Arduino      | 1       | 16MHz     | 256 KB Flash, 8 KB SRAM  | 347.22mHz |
| ESP32        | 2       | 240MHz    | 4 MB Flash, 520 KB  SRAM | 7.251Hz   |
| STM32F4      | 1       | 168MHz    | 1 MB Flash, 192 KB  SRAM | 60.621mHz |

```
