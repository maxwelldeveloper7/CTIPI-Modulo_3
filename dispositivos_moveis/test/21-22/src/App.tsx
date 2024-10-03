import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function Botao(){
  function handleClick(){
    alert("Botão clicado!")
  }
  return <button onClick={handleClick}>Clique aqui</button>
}

function CampoTexto(){
  function handleChange(event: any){
    console.log(event.target.value);
  }
  return <input type="text" onChange={handleChange} />
}

function Formulario(){
  function handleSubmit(event: any){
    event.preventDefault();
    alert("Formulário enviado!");
  }
  return <form onSubmit={handleSubmit}>
    <CampoTexto />
    <button type="submit">Enviar</button>
  </form>
}

function Teclado(){
  function handleKeyDown(event: any){
    console.log(`Tecla pressionada: ${event.key}`);
  }
  return <input type="text" onKeyDown={handleKeyDown} />
}

const frutas1 = ["Maçã", "Banana", "Laranja", "Uva"];

const frutas2= [
  {id:1, nome: "Maçã"},
  {id:2, nome: "Banana"},
  {id:3, nome: "Laranja"},
];

function ListaDeFrutas(){
  return (
    <ul>
      {frutas2.map( (fruta) => (
        <li key={fruta.id}>{fruta.nome}</li>
      ))}
    </ul>
  )
}

const produtos = [
  {id:1, nome: "Camiseta", preco: 10.99},
  {id:2, nome: "Calça", preco: 15.99},
  {id:3, nome: "Bermuda", preco: 20.99},
];

function TabelaDeProdutos(){
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Preço</th>
        </tr>
      </thead>
      <tbody>
        {produtos.map( (produto) => (
          <tr key={produto.id}>
            <td>{produto.id}</td>
            <td>{produto.nome}</td>
            <td>{produto.preco}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}


function App() {
  return <TabelaDeProdutos /> 
  
}

export default App;
