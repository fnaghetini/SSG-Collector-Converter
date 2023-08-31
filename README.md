# SSG-Collector-Converter

## Descrição
Aplicativo que converte dados da coletora de campo do Curto Prazo da Vale Sossego em templates de importação do Sample Station.

## Utilização do Aplicativo
 A figura abaixo mostra a interface do aplicativo:

 [app_ui](https://github.com/fnaghetini/SSG-Collector-Converter/edit/main/img/app_ui.png)

 - No campo **Ano**, selecione o ano em que o plano de perfuração foi realizado
 - No campo **Datum**, selecione o datum adequado das coordenadas adquiridas em campo
 - No campo **Tipo de Amostra**, selecione o tipo de amostra em questão

### Gerando templates - Amostras Programadas
1. Para gerar os templates de amostras programadas, clique no botão **Gerar Templates (PROG)**;
2. Na janela do Explorador de Arquivos do Windows, selecione a pasta que contenha os arquivos .txt da coletora, ou seja, aqueles que contém apenas as coordenadas PROGRAMADAS;
3. Se não ocorrer nenhum erro, serão gerados dois templates por arquivo .txt na mesma pasta selecionada no item anterior:
    - **Samples**: contém os dados de cabeçalho das amostras (nomenclatura: `Nome do plano de perfuração + _prog_samples.csv`)
    - **Coordinates**: contém os dados de coordenadas PROGRAMADAS das amostras (nomenclatura: `Nome do plano de perfuração + _prog_coordinates.csv`)

**ATENÇÃO:** A pasta selecionada no item 2 deve conter apenas arquivos .txt no formato da coletora, caso contrário ocorrerá erro na execução do aplicativo.

### Gerando templates - Amostras Locadas e Executadas
1. Para gerar os templates de amostras locadas e executadas, clique no botão **Gerar Templates (LOCD e EXEC)**;
2. Na janela do Explorador de Arquivos do Windows, selecione a pasta que contenha os arquivos .csv da coletora, ou seja, aqueles que contém apenas as coordenadas LOCADAS e EXECUTADAS;
3. Se não ocorrer nenhum erro, serão gerados dois templates por arquivo .csv na mesma pasta selecionada no item anterior:
    - **Samples**: contém os dados de cabeçalho das amostras (nomenclatura: `Nome do plano de perfuração + _locd_exec_samples.csv`)
    - **Coordinates**: contém os dados de coordenadas LOCADAS (se houver) e EXECUTADAS das amostras (nomenclatura: `Nome do plano de perfuração + _locd_exec_coordinates.csv`)

**ATENÇÃO:** A pasta selecionada no item 2 deve conter apenas arquivos .csv no formato da coletora, caso contrário ocorrerá erro na execução do aplicativo.
