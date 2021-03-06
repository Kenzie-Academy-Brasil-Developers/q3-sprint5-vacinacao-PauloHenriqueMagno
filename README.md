# API de Vacinação

Essa api cria e acessa vacinas contra COVID-19 aplicadas e a sua próxima dose.

## Endpoints

| Metodo | Endpoint |
|---|---|
| `GET` | /vaccinations |
| `POST` | /vaccinations |

### **GET /vaccinations**

  Essa endpoint não requer autenticação, nenhum parametro e corpo de requisição.

  **Parâmetros opcionais:**

  | Parâmetro | Valor | Valor Pré-definido | Descrição |
  |:----|:----:|:----:|:----|
  | page | Numero | 1 | O numero da página atual |
  | per_page | Numero | 5 | O numero de items por página |

  **Exemplo de resposta da requisição:**

  ```
  {
    "page": 1,
    "vaccinations": [
      {
        "cpf": "01234567893",
        "first_shot_date": "Fri, 11 Feb 2022 18:38:48 GMT",
        "health_unit_name": "Santa Rita",
        "name": "Chrystian",
        "second_shot_date": "Thu, 12 May 2022 18:38:48 GMT",
        "vaccine_name": "Pfizer"
      },
      {
        "cpf": "1234567893",
        "first_shot_date": "Fri, 11 Feb 2022 18:55:34 GMT",
        "health_unit_name": "Santa Rita",
        "name": "Chrystian",
        "second_shot_date": "Thu, 12 May 2022 18:55:34 GMT",
        "vaccine_name": "Pfizer"
      },
      {
        "cpf": "11234567893",
        "first_shot_date": "Fri, 11 Feb 2022 18:55:34 GMT",
        "health_unit_name": "Santa Rita",
        "name": "Chrystian",
        "second_shot_date": "Thu, 12 May 2022 18:55:34 GMT",
        "vaccine_name": "Pfizer"
      }
    ]
  }
  ```

### **POST /vaccinations**

  Essa endpoint não é protegida e não requer nenhum parametro.

  É obrigatório no corpo da requisição os seguintes valores:
  
  | Valor | Tipo | Exemplo |
  |:----|:---:|:---:|
  | cpf | String | "11234567893" |
  | name | String | "Chrystian" |
  | vaccine_name | String | "Pfizer" |
  | health_unit_name | String | "Santa Rita" |
  
  Será ignorado qualquer outro valor além dos citados acima.  
 
  Os valores devem ser compatíveis com as seguintes regras:
  * cpf deve conter exatamente 11 caracteres.
  * cpf deve ser unico.

  Será levantado uma mensagem de erro caso:
  * Algum valor seja de outro tipo a não ser string.
  * Algum valor obrigatório estiver faltando.
  * Alguma regra não seja seguida.

  **Exemplo:**
  
  Corpo da requisição:
  ```
    {
      "cpf": "11234567893",
      "name": "Chrystian",
      "vaccine_name": "Pfizer"
      "health_unit_name": "Santa Rita",
    }
  ```

  Resposta:
  ```
    {
      "cpf": "11234567893",
      "first_shot_date": "Fri, 11 Feb 2022 18:55:34 GMT",
      "health_unit_name": "Santa Rita",
      "name": "Chrystian",
      "second_shot_date": "Thu, 12 May 2022 18:55:34 GMT",
      "vaccine_name": "Pfizer"
    }
  ```