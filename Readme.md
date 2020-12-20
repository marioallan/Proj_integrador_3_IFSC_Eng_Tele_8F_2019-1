# Projeto Integrador 3 - Controles de cargas apartir do KWh da unidade consumidora

### IFSC - Campus São José - Engenharia de Telecomunicações - 8ª Fase - 2019-1 

### Alunos: 
[**Mário Allan Lehmkuhl de Abreu**](https://bit.ly/3iAEHkJ)\
[**Lucas Thiesen**](https://bit.ly/2SERbxz) 

### Proposta

O objetivo do projeto é obter um controle de cargas de equipamentos elétricos (ar-condicionado, chuveiro, aquecedor, etc) de um ambiente com o intuito de reduzir o consumo de energia dos mesmos, desligando-os se necessário. O controle é feito através da analise do kWh consumido e registrado no relógio medidor de luz da unidade consumidora.

O controle será efetuado através de um microcontrolador que irá receber a informação via wifi e irá saber se a carga pode ser acionada ou não. Para determinar se a carga poderá ser acionada, será utilizado como parametro um limiar de kWh definido pelo usuário que irá ser comparado ao kWh atual da unidade consumidora, caso o consumo atual já seja maior ou igual ao limiar pré-definido, as cargas controladas pelo sistema não poderão ser acionadas pelo usuário, fazendo com que o usuário economize energia.

Para a captura do consumo atual, optamos pela opção menos invasiva a rede elétrica do usuário, não colocando nenhum tipo de equipamento na saída do relógio, e fazendo com que não seja necessário o acionamento de um serviço especializado para instalar o sistema. Para que isso seja possível será utilizada uma solução de visão computacional e uma camera IP. A câmera IP deve enviar uma imagem do relogio num intervalo pré definido de tempo para um servidor de aplicação. No servidor ao receber a imagem, será atrelado a unidade consumidora um valor numérico indicando o consumo em kWh, o valor será inferido da imagem a partir de um algoritmo de visão computacional. Ao obter o valor da imagem o sistema irá comparar o valor retirado da imagem ao limiar préviamente configurado pelo cliente, caso maior ou igual o servidor acionará o serviço de atuação na rede.

[**Relatório**](https://github.com/marioallan/Proj_integrador_3_IFSC_Eng_Tele_8F_2019-1/blob/master/PJI3_Relatorio_Final_2019_1.pdf)
