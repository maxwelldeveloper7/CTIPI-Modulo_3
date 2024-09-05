// funcionario.ts
import { Pessoa } from './pessoa';

export class Funcionario extends Pessoa {
    constructor(nome: string, idade: number, public cargo: string) {
        super(nome, idade);
    }

    descrever(): string {
        return `${this.nome}, ${this.idade} anos, Cargo: ${this.cargo}`;
    }
}

