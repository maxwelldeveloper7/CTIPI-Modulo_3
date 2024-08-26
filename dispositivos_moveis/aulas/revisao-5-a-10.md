## **Introdução ao TypeScript: Benefícios e Conceitos Básicos**
![](./assets/revisao.jpeg)
Imagine que você está construindo um castelo de blocos. Cada bloco tem um formato e um tamanho específicos, certo? Agora, imagine se você pudesse definir as regras para que cada bloco se encaixe perfeitamente. Isso é o que o TypeScript faz para o seu código JavaScript!

TypeScript é como uma versão "turbinada" do JavaScript. Ele permite que você escreva código mais seguro e previsível, ajudando a evitar erros antes mesmo de você rodar o programa. Isso porque o TypeScript adiciona "tipos" ao seu código. Com os tipos, você pode dizer ao seu código: "Ei, esse bloco deve ser um número!" ou "Essa peça deve ser um texto!". Isso te ajuda a evitar problemas como tentar misturar blocos que não se encaixam.

### **Benefícios do TypeScript:**
1. **Detecção de Erros Mais Cedo:** Encontre erros no seu código antes mesmo de executá-lo.
2. **Manutenção Facilitada:** Com os tipos, você entende melhor o que cada parte do seu código faz, facilitando mudanças no futuro.
3. **Ferramentas Poderosas:** Aproveite autocompletes, refatorações automáticas e muito mais.

## **Configuração do TypeScript no Projeto**

Agora que você sabe o quão incrível o TypeScript pode ser, que tal configurá-lo no seu projeto?

### **Passo 1: Instalando o TypeScript**
Primeiro, precisamos instalar o TypeScript no seu projeto. Para isso, abra o terminal e digite:

```bash
npm install typescript --save-dev
```

### **Passo 2: Inicializando o TypeScript**
Agora que o TypeScript está instalado, vamos iniciar um projeto TypeScript. Execute o seguinte comando:

```bash
npx tsc --init
```

Isso vai criar um arquivo chamado `tsconfig.json`, onde você pode configurar como o TypeScript deve funcionar no seu projeto.

### **Passo 3: Configurando Scripts de Execução**
Quer facilitar sua vida? Vamos configurar um script para rodar seu código TypeScript automaticamente! No seu `package.json`, adicione:

```json
"scripts": {
  "dev": "ts-node-dev src/index.ts"
}
```

Agora, sempre que você quiser rodar seu código TypeScript, basta usar:

```bash
npm run dev
```

## **Tipos Básicos, Interfaces e Funções em TypeScript**

### **Tipos Básicos**
Os tipos em TypeScript são como etiquetas que você coloca em suas variáveis, dizendo o que elas são. Aqui estão os principais:

- `string`: para textos (ex.: "Olá, mundo!")
- `number`: para números (ex.: 42)
- `boolean`: para verdadeiro ou falso (ex.: true, false)
- `array`: uma lista de itens (ex.: [1, 2, 3])

Exemplo:

```typescript
let nome: string = "João";
let idade: number = 25;
let aprovado: boolean = true;
```

### **Interfaces**
Interfaces são como planos de construção para objetos. Elas definem a estrutura que um objeto deve ter.

Exemplo:

```typescript
interface Pessoa {
  nome: string;
  idade: number;
  aprovada: boolean;
}

let aluno: Pessoa = {
  nome: "Maria",
  idade: 22,
  aprovada: true,
};
```

### **Funções**
Funções em TypeScript também podem ter tipos. Você pode definir o tipo dos parâmetros e o tipo do valor retornado.

Exemplo:

```typescript
function saudar(nome: string): string {
  return `Olá, ${nome}!`;
}

console.log(saudar("Pedro"));
```

## **Classes e Interfaces Avançadas em TypeScript**

### **Classes**
Classes em TypeScript são como plantas baixas para criar objetos. Elas podem ter propriedades e métodos.

Exemplo:

```typescript
class Animal {
  nome: string;
  idade: number;

  constructor(nome: string, idade: number) {
    this.nome = nome;
    this.idade = idade;
  }

  emitirSom(): void {
    console.log("Som do animal");
  }
}

let cachorro = new Animal("Rex", 5);
cachorro.emitirSom(); // Som do animal
```

### **Interfaces Avançadas**
As interfaces podem ser estendidas para combinar várias estruturas de dados.

Exemplo:

```typescript
interface Movel {
  mover(): void;
}

interface Voador {
  voar(): void;
}

class Passaro implements Movel, Voador {
  mover(): void {
    console.log("O pássaro está andando");
  }

  voar(): void {
    console.log("O pássaro está voando");
  }
}

let papagaio = new Passaro();
papagaio.mover();
papagaio.voar();
```

## **Exercícios de Fixação**

### **1. Introdução ao TypeScript**
- **Exercício 1.1:** Explique com suas palavras o que é TypeScript e como ele melhora o desenvolvimento em comparação com o JavaScript puro.

### **2. Configuração do TypeScript no Projeto**
- **Exercício 2.1:** Configure um novo projeto TypeScript do zero, seguindo os passos descritos.
- **Exercício 2.2:** Crie um script `dev` em seu `package.json` que execute o arquivo `src/index.ts` usando o `ts-node-dev`.

### **3. Tipos Básicos, Interfaces e Funções em TypeScript**
- **Exercício 3.1:** Crie variáveis usando os tipos `string`, `number`, `boolean`, e `array`.
- **Exercício 3.2:** Defina uma interface para um objeto `Carro` que tem as propriedades `marca`, `modelo` e `ano`. Crie um objeto que siga essa interface.
- **Exercício 3.3:** Escreva uma função que receba dois números e retorne a soma deles. Não esqueça de tipar os parâmetros e o retorno da função.

### **4. Classes e Interfaces Avançadas em TypeScript**
- **Exercício 4.1:** Crie uma classe `Pessoa` que tenha propriedades `nome` e `idade`, e um método que imprima uma saudação.
- **Exercício 4.2:** Defina uma interface `Veiculo` com um método `acelerar`. Crie uma classe `Moto` que implemente essa interface e execute o método `acelerar`.

Esses exercícios ajudarão a solidificar os conceitos básicos e avançados do TypeScript, proporcionando uma base sólida para explorar mais esse poderoso recurso no desenvolvimento web. Boa codificação! 🚀