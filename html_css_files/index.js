// Promise 1
const promiseOne = new Promise(function (resolve, reject){
   setTimeout(function(){
      console.log('Async task is complete');
      resolve()
   }, 1000)
})

promiseOne.then(function(){
   console.log('Promise consumed');
})


// Promise 2
new Promise(function(resolve,reject){
   setTimeout(function(){
      console.log("Async 2 created");
      resolve()
   }, 1000)
}).then(function(){
   console.log("Promise 2 consumed");
})


// Promise 3
const promiseThree = new Promise(function(resolve, reject){
   setTimeout(function(){
      resolve({name: "Pritam", age: 20})
   }, 1000)
})

promiseThree.then(function(user){
   console.log(user);
})



// Promise 4
const promiseFour = new Promise(function(resolve, reject){
   setTimeout(function(){
      let error = false
      if(!error){
         resolve({name: "Pritam", age: 20})
      }else{
         reject('ERROR: some error occured')
      }
   }, 1000)
})

promiseFour.then((user) => {
   console.log(user);
   return user.name
}).then((username) => {
   console.log(username);
}).catch((error) => {
   console.log(error);
}).finally(() => console.log("Either the promise resolved or rejected"))



// Promise 5
const promiseFive = new Promise(function(resolve, reject){
   setTimeout(function(){
      let error = true
      if(!error){
         resolve({name: "Shreya", age: 21})
      }else{
         reject('ERROR: 404 error not found')
      }
   }, 1000)
})

async function consumePromiseFive(){
   try{
      const response = await promiseFive
      console.log(response);
   }catch(error){
      console.log(error);
   }
}

consumePromiseFive()



// Using Fetch 
// async function getUsers(){
//    try{
//       const response = await fetch('https://randomuser.me/api/')
//       const data = await response.json()
//       console.log(data);
//    }catch(error){
//       console.log('E:',error);
//    }
// }

// getUsers()



fetch('https://randomuser.me/api/').then((response) => {
   return response.json()
}).then((data) => {
   console.log(data);
}).catch((error) => console.log(error))