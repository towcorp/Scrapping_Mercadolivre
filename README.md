# Scrapping_Mercadolivre
### Scraping data from MercadoLivre

  Accessing the MercadoLivre search list by product and collecting key data:
 
  - title
 
  - description
 
  - price
 
  - condition / sold amount 
 
  - photo link
 
  - collected page link
 
  ### How to run the application
 
  1. Place the link of the search page to be searched in "start_urls = ['paste here']"
 
  2. If necessary, modify the allowed domains according to the search in "allowed_domains = ['product.mercadolivre.com.br', 'lista.mercadolivre.com.br']"
 
  3. Open the terminal (CMD or PowerShell of your choice) and run the program and save the file in csv or json according to your preference
  
          - scrapy runspider mercadolivre.py -o mercado_livre.csv -t csv 
        
          - scrapy runspider mercadolivre.py -o mercado_livre.json -t json
  

---
### Raspagem de dados do Mercado livre

 Acessando lista de busca no mercado livre por produto e coletando principais dados:
 
 - titulo
 
 - descrição
 
 - preço
 
 - Condição / quantidade vendida
 
 - link de fotos
 
 - link da pagina coletada
 
 ### Como rodar a aplicação
 
 1. Coloque o link da pagina de busca a ser pesquisada em  "start_urls = ['cole aqui']"
 
 2. Se necessario modifique os dominios permitidos de acordo com a busca em "allowed_domains = ['produto.mercadolivre.com.br', 'lista.mercadolivre.com.br']"
 
 3. Abra o terminal(CMD ou PowerShell a escolha) e rode o programa e salve o arquivo em csv ou json de acordo com sua preferencia
 
        - scrapy runspider mercadolivre.py -o mercado_livre.csv -t csv 
        
        - scrapy runspider mercadolivre.py -o mercado_livre.json -t json
