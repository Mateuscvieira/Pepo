# Pepo 0.1
Pet project de assistente pessoal, tentando automatizar coisas para facilitar minha vida. Pretendo atualizar sempre que surgir uma nova ideia. O nome é o nome do meu primeiro cachorro.

## Funcionalidades

Pepo 0.1: <ol>
  <li> Procura alterações na pasta designada, checa a extensão do arquivo que foi modificado e coloca esse arquivo em uma nova pasta (dentro de outro diretório designado) com o nome da extensão do arquivo. Assim, eventualmente todos os PDFs estarão em uma pasta de PDF, todos os PNGs em uma pasta de PNG, etc.; </li>
  <li> Grava registros de todas as alterações em um arquivo .txt designado (default Pepo_logs.txt). </li>
</ol>

## Bugs conhecidos

Pepo 0.1: <ol>
  <li> Colocar a pasta destino "new_directory" dentro da pasta que está sendo vigiada dá crash por entrar num ciclo eterno de modificar-mover-modificar-mover...;
  <li> O programa tenta duas vezes mover o mesmo arquivo (não tem efeito no resultado final), enchendo o terminal de logs duplicados (não tem efeito no arquivo de registros).
  </ol>

## Arquivos

<ul>
  <li> main.py: Executa todo o funcionamento do programa; </li>
  <li> organizer.py: Script definindo a classe que organiza os arquivos como descrito acima; </li>
  <li> logger.py: Script definindo a classe que faz os registros de mudanças; </li>
  <li> config.json: Json com as configurações necessárias para o funcionamento; </li>
  <li> Pepo_logs.txt: Arquivo default para gravar as alterações. </li>
</ul>

## Utilização

Passo a passo:

<ol>
  <li>Modificar config.json para encaixar no seu sistema de arquivos. Avisos: não alterar os nomes das variáveis; "new_directory" tem que ter um pai distinto de "file_to_watch"; "log_path" pode ir para onde quiser, mas o nome do arquivo precisa ser Pepo_logs.txt;</li>
  <li>Executar main.py do modo que preferir.</li>
</ol>
