import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function Saudacao(props: any){
  return <h1>Olá, {props.nome}!</h1>
}

function Contador(){
  const [contador, setContador] = useState(0);
  return (
    <div>
      <p>Você clicou {contador} vezes</p>
      <button onClick={() => setContador(contador + 1)}>Clique aqui</button>
    </div>
  )
}

function App() {
  return <Contador />
}

export default App;
