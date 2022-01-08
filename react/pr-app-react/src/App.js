import React, { useState } from 'react';
import './components/Tasks';
import './App.css';
import Tasks from './components/Tasks';

const App = () => {

  //let mensagem = "hello world";
  const [tasks, setTasks] = useState(
    
    {

      id : '1',
      tittle : 'Estudar Programação',
      completed : false,
    
    },
    {

      id : '2',
      tittle : 'ler livros',
      completed : true,

    },

  );

  return (
    <>  
      <div className='container'>
        <Tasks tasks = {tasks} />
      </div>
      </>
  )

};

export default App;